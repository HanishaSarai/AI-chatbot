from dotenv import load_dotenv, parser
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model="mistral-small-2506", temperature=0.9, max_tokens=100)


class Movie(BaseModel):
    movie_name: str
    release_year: str
    director: Optional[str]
    genre: List[str]
    main_cast: List[str]
    plot: Optional[str]
    themes: List[str]
    notable_features: Optional[List[str]]
    setting: Optional[str]
    short_summary: str

parser = PydanticOutputParser(pydantic_object=Movie)

prompt = ChatPromptTemplate([
    ("system", 
     """
You are an professional movie information extractor assistant. You will be given a paragraph about a movie. Your task is to extract the following details from the paragraph and provide them in a structured format and in a clean readabale format.

{format_instructions}

"""), 
("human", 
 """ 
{paragraph}
""")
])

para = input("Give your paragraph: ")

final_prompt = prompt.invoke({"paragraph": para,
                              "format_instructions": parser.get_format_instructions()})

response = model.invoke(final_prompt)

print(response.content)