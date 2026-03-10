from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage,  HumanMessage

model = ChatMistralAI(model="mistral-small-2506", temperature=0.9, max_tokens=100)

print("Choose your AI mode")
print("press 1 for Funny mode")
print("press 2 for Sad mode")
print("press 3 for Sarcastic mode")

choice = int(input("Enter your choice: "))

if choice == 1:
    mode = "You are a funny AI agent."
elif choice == 2:
    mode = "You are a sad AI agent. You respond with empathy to the user."
elif choice == 3:
    mode = "You are a sarcastic AI agent. You respond with wit and humor to the user."

messages =[
    SystemMessage(content=mode),
]


print ("-------------------- Welcome type 0 to exit the application --------------------")
 
while True:
    prompt = input("You: ")
    messages.append(HumanMessage(content=prompt))
    if prompt == "0":
        break

    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))

    print("Bot:", response.content)