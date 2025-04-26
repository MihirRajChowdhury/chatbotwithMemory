import os
# Set pydantic compatibility mode
# os.environ["LANGCHAIN_PYDANTIC_V1"] = "1"

import warnings
from langchain._api import LangChainDeprecationWarning
warnings.simplefilter("ignore", category=LangChainDeprecationWarning)

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
groq_api_key = os.environ["GROQ_API_KEY"]
from langchain_groq import ChatGroq

# Initialize the chatbot
chatbot = ChatGroq(model_name="llama-3.1-8b-instant")

from langchain_core.messages import HumanMessage

# Simple conversation example
messagesToTheChatbot = [
    HumanMessage(content="My favorite color is blue."),
]

response = chatbot.invoke(messagesToTheChatbot)

print("\n----------\n")
print("My favorite color is blue.")
print("\n----------\n")
print(response.content)
print("\n----------\n")

response = chatbot.invoke([
    HumanMessage(content="What is my favorite color?")
])

print("\n----------\n")
print("What is my favorite color?")
print("\n----------\n")
print(response.content)
print("\n----------\n")

# Try using the original import paths since that's what you have installed
from langchain.chains import LLMChain
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import HumanMessagePromptTemplate
from langchain_core.prompts import MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from langchain.memory import FileChatMessageHistory

memory = ConversationBufferMemory(
    chat_memory=FileChatMessageHistory("messages.json"),
    memory_key="messages",
    return_messages=True
)

prompt = ChatPromptTemplate(
    messages=[
        MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

chain = LLMChain(
    llm=chatbot,
    prompt=prompt,
    memory=memory,
    verbose=True
)

response = chain.invoke({"content": "hello!"})

print("\n----------\n")
print("hello!")
print("\n----------\n")
print(response["text"])
print("\n----------\n")

response = chain.invoke({"content": "my name is Julio"})

print("\n----------\n")
print("my name is Julio")
print("\n----------\n")
print(response["text"])
print("\n----------\n")

response = chain.invoke({"content": "what is my name?"})

print("\n----------\n")
print("what is my name?")
print("\n----------\n")
print(response["text"])
print("\n----------\n")