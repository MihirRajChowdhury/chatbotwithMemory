
##################################### OLD WAY TO WRITE LANGCHAIN WITH LEGACY CHAINS ####

# import warnings

# from langchain._api import LangChainDeprecationWarning

# warnings.simplefilter("ignore", category=LangChainDeprecationWarning)

# import os
# from dotenv import load_dotenv, find_dotenv
# _ = load_dotenv(find_dotenv())
# openai_api_key = os.environ["OPENAI_API_KEY"]

# GROQ_API_KEY = os.environ["GROQ_API_KEY"]
# from langchain_groq import ChatGroq;
# chatbot = ChatGroq(model_name="llama-3.1-8b-instant")

# from langchain_core.messages import HumanMessage

# messagesToTheChatbot = [
#     HumanMessage(content="My favorite color is blue."),
# ]

# response = chatbot.invoke(messagesToTheChatbot)

# print("\n----------\n")

# print("My favorite color is blue.")

# print("\n----------\n")
# print(response.content)

# print("\n----------\n")

# response = chatbot.invoke([
#     HumanMessage(content="What is my favorite color?")
# ])

# print("\n----------\n")

# print("What is my favorite color?")

# print("\n----------\n")
# print(response.content)

# print("\n----------\n")

# from langchain import LLMChain
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.prompts import HumanMessagePromptTemplate
# from langchain_core.prompts import MessagesPlaceholder
# from langchain.memory import ConversationBufferMemory
# from langchain.memory import FileChatMessageHistory

# memory = ConversationBufferMemory(
#     chat_memory=FileChatMessageHistory("messages.json"),
#     memory_key="messages",
#     return_messages=True
# )

# prompt = ChatPromptTemplate(
#     input_variables=["content", "messages"],
#     messages=[
#         MessagesPlaceholder(variable_name="messages"),
#         HumanMessagePromptTemplate.from_template("{content}")
#     ]
# )

# chain = LLMChain(
#     llm=chatbot,
#     prompt=prompt,
#     memory=memory,
#     verbose=True
# )

# response = chain.invoke("hello!")

# print("\n----------\n")

# print("hello!")

# print("\n----------\n")
# print(response)

# print("\n----------\n")

# response = chain.invoke("my name is Julio")

# print("\n----------\n")

# print("my name is Julio")

# print("\n----------\n")
# print(response)

# print("\n----------\n")

# response = chain.invoke("what is my name?")

# print("\n----------\n")

# print("what is my name?")

# print("\n----------\n")
# print(response["text"])

# print("\n----------\n")


############################### NEW WAY TO WRITE LANGCHAIN WITH RUNNABLES ###############


# import os
# from dotenv import load_dotenv, find_dotenv

# # Load environment variables
# _ = load_dotenv(find_dotenv())
# # Ensure you have GROQ_API_KEY in your .env file
# groq_api_key = os.environ["GROQ_API_KEY"]
# # openai_api_key = os.environ.get("OPENAI_API_KEY") # Keep if needed elsewhere, but not used here

# # --- Model Initialization ---
# from langchain_groq import ChatGroq
# chatbot = ChatGroq(model_name="llama-3.1-8b-instant", groq_api_key=groq_api_key)

# # --- Prompt Template Definition ---
# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain_core.messages import HumanMessage, AIMessage # Import AIMessage too

# prompt = ChatPromptTemplate.from_messages([
#     # "system", "You are a helpful assistant."), # Optional: Add a system message if desired
#     MessagesPlaceholder(variable_name="history"), # Placeholder for chat history
#     ("human", "{content}"), # Placeholder for the user's current input
# ])

# # --- Memory Setup ---
# from langchain.memory import FileChatMessageHistory

# # Define a function to get the chat history object.
# # This function takes a session_id, allowing you to manage multiple independent conversations.
# # For this example, we'll use a single file, so the session_id isn't strictly used
# # to change the file, but the structure requires it.
# def get_session_history(session_id: str) -> FileChatMessageHistory:
#     return FileChatMessageHistory(f"messages_{session_id}.json")

# # --- Chain Construction using LCEL and Memory Wrapper ---
# from langchain_core.runnables.history import RunnableWithMessageHistory

# # 1. Define the core chain (prompt | model) using LCEL
# core_chain = prompt | chatbot

# # 2. Wrap the core chain with RunnableWithMessageHistory
# #    This automatically handles loading and saving messages.
# chain_with_history = RunnableWithMessageHistory(
#     core_chain,
#     get_session_history, # Function to retrieve the history object for a given session
#     input_messages_key="content", # The key in the input dict for the user's message
#     history_messages_key="history", # The key in the prompt for the MessagesPlaceholder
# )

# # --- Invocation ---
# # Each conversation needs a unique session_id. All invokes with the same
# # session_id will share the same history file ("messages_user123.json" in this case).
# session_id = "user123"

# print("\n---------- Invoke 1 ----------\n")
# user_input_1 = "hello!"
# print(f"Human: {user_input_1}")
# # Invoke requires a dictionary matching the `input_messages_key`
# # and a config dict with the session_id
# response_1 = chain_with_history.invoke(
#     {"content": user_input_1},
#     config={"configurable": {"session_id": session_id}}
# )
# print(f"\nAI: {response_1.content}")
# print("\n----------------------------\n")


# print("\n---------- Invoke 2 ----------\n")
# user_input_2 = "my name is Julio"
# print(f"Human: {user_input_2}")
# response_2 = chain_with_history.invoke(
#     {"content": user_input_2},
#     config={"configurable": {"session_id": session_id}}
# )
# print(f"\nAI: {response_2.content}")
# print("\n----------------------------\n")


# print("\n---------- Invoke 3 ----------\n")
# user_input_3 = "what is my name?"
# print(f"Human: {user_input_3}")
# response_3 = chain_with_history.invoke(
#     {"content": user_input_3},
#     config={"configurable": {"session_id": session_id}}
# )
# print(f"\nAI: {response_3.content}")
# print("\n----------------------------\n")

# You can inspect the history file "messages_user123.json" to see the saved conversation.

# --- Optional: LangGraph Approach (Newer Recommendation for Complex State) ---
# For more complex scenarios involving multiple steps, conditional logic, or tool use
# with memory, LangGraph is the latest recommendation. It involves defining a state
# graph and using checkpointers for persistence. While powerful, it's more verbose
# for this simple chat example. RunnableWithMessageHistory remains suitable here.


####################### PRACTICE ############################

import os 
from dotenv import load_dotenv, find_dotenv

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
_ = load_dotenv(find_dotenv())

groq_api_key = os.environ["GROQ_API_KEY"]

chatbot = ChatGroq(model="llama-3.1-8b-instant", groq_api_key=groq_api_key)

message_To_Chatbot = [HumanMessage(content="My favourite colour is blue")]

response = chatbot.invoke(message_To_Chatbot)

print(response.content)

second_message = [HumanMessage(content="What is my favourite colour")]
response2 = chatbot.invoke(second_message)
print(response2.content)

from langchain.prompts import HumanMessagePromptTemplate
from langchain_core.prompts import MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from langchain.memory import FileChatMessageHistory
from langchain import LLMChain
from langchain_core.prompts import ChatPromptTemplate


memory = ConversationBufferMemory(
    chat_memory=FileChatMessageHistory("message.json"),
    memory_key="messages",
    return_messages=True
)

prompt = ChatPromptTemplate(
    input_variables=["content","messages"],
    messages=[
        MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

chain = LLMChain(
    llm = chatbot,
    memory = memory,
    prompt = prompt
)

response = chain.invoke("hello")

print(response["text"])

response = chain.invoke("My name is Mihir")

print(response["text"])

response = chain.invoke("What is My name?")

print(response["text"])


