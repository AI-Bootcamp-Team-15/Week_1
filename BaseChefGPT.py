import os
from openai import OpenAI

class BaseChefGPT:
    def __init__(self):        
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        self.messages = []
        self.name = "Base chef"
        self.description = ""

    def run(self, user_input = None):        
        """
        A function that runs a chatbot using the specified model to respond to user input.
        
        Parameters:
            user_input (str): The user input to be used in the conversation. Defaults to None.
        
        Returns:
            str: The collected conversation string.
        """
        if user_input is None:
            print("")
            user_input = input("How can " + self.name + " assist you today?\n")
    
        model = "gpt-3.5-turbo"

        while True:
            self.messages.append(
                {
                    "role": "user",
                    "content": user_input
                }
            )

            stream = self.client.chat.completions.create(
                model=model,
                messages=self.messages,
                stream=True,
            )
            collected_messages = []
            print("---- Response ----")
            for chunk in stream:
                chunk_message = chunk.choices[0].delta.content or ""
                print(chunk_message, end="")
                collected_messages.append(chunk_message)
            
            collected_string = "".join(collected_messages)
            self.messages.append(
                {
                    "role": "system",
                    "content": collected_string
                }
            )
            if (not "?" in collected_string.lower()):
                break
            else:
                print("")
                user_input = input()

        return collected_string