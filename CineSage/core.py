from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model="mistral-small-2506", temperature=0.9, max_tokens=100)

prompt = ChatPromptTemplate([
    ("system", 
     """
You are an professional movie information extractor assistant. You will be given a paragraph about a movie. Your task is to extract the following details from the paragraph and provide them in a structured format and in a clean readabale format.

From the given paragraph, identify and extract the following details:

Movie Name:
Release Year:
Director:
Genre:
Main Cast:
Plot / Story Premise:
Themes:
Notable Features (visual effects, music, awards, etc.):
Setting:

Short Summary : 

"""), 
("human", 
 """
Extract information from this paragraph : 

{paragraph}
""")
])

para = input("Give your paragraph: ")

final_prompt = prompt.invoke({"paragraph": para})

response = model.invoke(final_prompt)

print(response.content)