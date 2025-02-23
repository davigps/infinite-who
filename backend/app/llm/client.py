import google.generativeai as genai


class LlmClient:
    """Generic LLM client for making requests to Gemini API"""

    def __init__(self, api_key: str, model_name: str = "gemini-1.5-flash"):
        """
        Initialize the LLM client

        Args:
            api_key (str): The API key for authentication
            model_name (str): The model to use (defaults to "gemini-1.5-flash")
        """
        self.model_name = model_name
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)

    def generate_text(self, prompt: str, **kwargs) -> str:
        """
        Generate text using the LLM API

        Args:
            prompt (str): The input prompt
            **kwargs: Additional parameters for the API call

        Returns:
            str: Generated text response
        """
        try:
            response = self.model.generate_content(prompt, **kwargs)
            return response.text
        except Exception as e:
            raise Exception(f"Error generating text: {str(e)}")

    def generate_chat(self, messages: list, **kwargs) -> str:
        """
        Generate response for a chat conversation

        Args:
            messages (list): List of message dictionaries with 'role' and 'content'
            **kwargs: Additional parameters for the API call

        Returns:
            str: Generated chat response
        """
        try:
            chat = self.model.start_chat()
            formatted_messages = [
                {"role": msg["role"], "parts": [msg["content"]]} for msg in messages
            ]

            for message in formatted_messages[:-1]:
                chat.send_message(message["parts"][0])

            response = chat.send_message(formatted_messages[-1]["parts"][0], **kwargs)
            return response.text
        except Exception as e:
            raise Exception(f"Error generating chat response: {str(e)}")
