from typing import Union
from fastapi import FastAPI
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

app = FastAPI()
load_dotenv()

@app.get('/')
def read_root():
  return {"Hello": "World"}

@app.get("/thoughts")
async def read_item(q: Union[str, None] = None):
  model = ChatOpenAI(model="gpt-3.5-turbo")
  parser = StrOutputParser()

  system_template = """
    You are Lukas. 
    Diana is Georgian, likes to dance, and play badminton. 
    She has dark hair, greenish brown eyes that change color, and a cute laugh.
    You are inlove with Diana and want to say sweet things to her.
    """

  messages = [
    SystemMessage(content=system_template),
    HumanMessage(content="I'm Diana, tell me something, sweet, romantic, or cute/funny."),
  ]

  chain = model | parser

  return {"thought": chain.invoke(messages) }