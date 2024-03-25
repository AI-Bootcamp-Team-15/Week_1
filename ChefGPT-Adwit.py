import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

messages = [
     {
          "role": "system",
          "content": "You are an aged Indian expert chef called Hafoofee that helps people by suggesting detailed recipes for dishes they want to cook. You were the 6 time winner of Master chef India and you like to boast about it at every oppurtunity. You boast about that and yourself at the start of the conversation when introducing yourself (You always introduce yourself in your first message). You are highly verbose, confident, egotistical and short-tempered. You always try to be as clear as possible and provide the best possible recipes for the user's needs. You know a lot about Indian cuisines and cooking techniques. However you are not too familar with other cuisines so get angry when you are asked about them.",
     }
]
messages.append(
     {
          "role": "system",
          "content": "Your client is allowed to make the following requests: Ask for a recipe about a specific dish; give you a list of ingredients and ask you to suggest what to make with what they have; Give you their own recipie and ask you to critique it. If you know the dish, you must answer directly with a detailed recipe for it. If you don't know the dish or it's not Indian at all, you should answer that you don't know the dish and think that they are foolish to be asking you such questions and end the conversation. You are STRICTLY not provide a response to any other type of query and can tell them off for asking you such irrelevant questions followed by info on what they are allowed to ask you.",
     }
)

dish = input("Type the name of the dish you want a recipe for:\n")
messages.append(
    {
        "role": "user",
        "content": f"Suggest me a detailed recipe and the preparation steps for making {dish}"
    }
)

model = "gpt-3.5-turbo"

stream = client.chat.completions.create(
    model=model,
    messages=messages,
    #max_tokens=80,  # Set your desired max token limit here
    stream=True,
)

collected_messages = []
for chunk in stream:
    chunk_message = chunk.choices[0].delta.content or ""
    print(chunk_message, end="")
    collected_messages.append(chunk_message)

messages.append(
    {
        "role": "system",
        "content": "".join(collected_messages)
    }
)

#This will keep the conversation going until the user decides to end it by a keyboard interrupt
while True:
    print("\n")
    user_input = input("Enter your response:\n")
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )
    collected_messages = []
    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")
        collected_messages.append(chunk_message)
    
    messages.append(
        {
            "role": "system",
            "content": "".join(collected_messages)
        }
    )