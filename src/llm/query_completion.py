import os
import openai
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

openai.api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(model='text-davinci-003',temperature=0.9)
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)
print(llm)
chain = LLMChain(llm=llm, prompt=prompt)

print(chain.run("colorful socks"))