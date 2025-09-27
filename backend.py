# backend.py

# --- Imports ---
import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn

# Gemini AI SDK
import google.generativeai as genai

# LangGraph: used to create stateful AI interaction graphs
from langgraph.graph import StateGraph, END

# Type safety
from typing import TypedDict


# --- Gemini API Setup ---
# You can replace this with an environment variable for better security in production
api_key = "YOUR_GEMINI_API_KEY"  

if not api_key:
    raise ValueError("GOOGLE_API_KEY not provided")

# Configure Google Generative AI with your API key
genai.configure(api_key=api_key)


# --- LangGraph Schema Definition ---
# Define the expected structure of data passing through the graph
class GraphState(TypedDict):
    input: str
    response: str


# --- Create LangGraph Conversation Flow ---
def create_conversation_graph():
    # Node function: Handles user input and returns Gemini response
    def generate_response(state: GraphState) -> GraphState:
        user_input = state["input"]

        # Instantiate the Gemini model
        model = genai.GenerativeModel(model_name="gemini-pro")

        # Generate response from the model
        response = model.generate_content(user_input)

        return {"input": user_input, "response": response.text}

    # Initialize the graph and define structure
    builder = StateGraph(GraphState)
    builder.add_node("response", generate_response)
    builder.set_entry_point("response")
    builder.add_edge("response", END)

    return builder.compile()


# Compile the conversation graph
graph = create_conversation_graph()


# --- FastAPI Setup ---
app = FastAPI()


@app.post("/chat")
async def chat(request: Request):
    """
    POST endpoint to receive user input and return Gemini-generated response.
    """
    data = await request.json()
    user_input = data.get("input", "")

    # Synchronously invoke the graph with user input
    result = graph.invoke({"input": user_input, "response": ""})

    return JSONResponse(content={"response": result["response"]})


# --- Entry Point ---
if __name__ == "__main__":
    # Run the FastAPI app using Uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
