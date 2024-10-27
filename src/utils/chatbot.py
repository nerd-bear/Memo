from groq import Groq
from src.utils.helper import *

config = load_config("config.json")

client = Groq(
    api_key=config["groq_token"],
)


class ChatBot:
    def __init__(self, system_prompt: str = None):
        """
        Initialize ChatBot with an optional system prompt.
        
        Args:
            system_prompt (str, optional): Initial system prompt to set the AI's behavior
        """
        # Initialize conversation history with system prompt if provided
        self.conversation_history = []
        if system_prompt:
            self.set_system_prompt(system_prompt)
    
    def set_system_prompt(self, system_prompt: str) -> None:
        """
        Set or update the system prompt.
        Clears existing conversation history and sets new system prompt.
        
        Args:
            system_prompt (str): The system prompt to set
        """
        # Clear existing history and set new system prompt
        self.conversation_history = [{
            "role": "system",
            "content": system_prompt
        }]
    
    def get_response(self, user_input: str):
        """
        Get a response from the AI model.
        
        Args:
            user_input (str): The user's input message
        
        Returns:
            str: The AI's response
        """
        # Append user message
        self.conversation_history.append({
            "role": "user",
            "content": user_input
        })
        
        chat_completion = client.chat.completions.create(
            messages=self.conversation_history,
            model="llama-3.1-70b-versatile",
        )
        
        bot_response = chat_completion.choices[0].message.content
        # Append assistant response
        self.conversation_history.append({
            "role": "assistant",
            "content": bot_response
        })
        
        return bot_response
    
    def reset_conversation(self) -> None:
        """
        Reset the conversation history while preserving the system prompt.
        """
        if self.conversation_history and self.conversation_history[0]["role"] == "system":
            system_prompt = self.conversation_history[0]
            self.conversation_history = [system_prompt]
        else:
            self.conversation_history = []
    
    def send_msg(self, user_input: str) -> str:
        """
        Send a message and get a response.
        
        Args:
            user_input (str): The user's input message
            
        Returns:
            str: The AI's response
        """
        response = self.get_response(user_input)
        return response