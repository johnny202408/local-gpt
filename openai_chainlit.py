import chainlit as cl
from openai import OpenAI
import os

# Simple OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# No global state, no session variables

@cl.on_message
async def on_message(message: str):
    """This function is called when the user sends a message"""
    
    try:
        # Generate a response using OpenAI
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message}
            ]
        )
        
        # Get the content from the response
        content = response.choices[0].message.content
        
        # Create and send a new message with the response content
        response_message = cl.Message(content=content)
        await response_message.send()
        
    except Exception as e:
        # Print detailed error for debugging
        print(f"ERROR: {type(e).__name__} - {str(e)}")
        
        # Create a simple error message
        error_message = cl.Message(content="Sorry, I encountered an error.")
        await error_message.send()

@cl.on_chat_start
async def on_chat_start():
    """This function is called when a new chat starts"""
    message = cl.Message(content="Hello! How can I help you today?")
    await message.send()