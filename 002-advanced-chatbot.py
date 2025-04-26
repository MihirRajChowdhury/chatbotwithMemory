# import warnings

# from langchain._api import LangChainDeprecationWarning

# warnings.simplefilter("ignore", category=LangChainDeprecationWarning)

# import os
# from dotenv import load_dotenv, find_dotenv
# _ = load_dotenv(find_dotenv())
# # openai_api_key = os.environ["OPENAI_API_KEY"]

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

# from langchain_community.chat_message_histories import ChatMessageHistory
# from langchain_core.chat_history import BaseChatMessageHistory
# from langchain_core.runnables.history import RunnableWithMessageHistory

# chatbotMemory = {}

# # input: session_id, output: chatbotMemory[session_id]
# def get_session_history(session_id: str) -> BaseChatMessageHistory:
#     if session_id not in chatbotMemory:
#         chatbotMemory[session_id] = ChatMessageHistory()
#     return chatbotMemory[session_id]


# chatbot_with_message_history = RunnableWithMessageHistory(
#     chatbot, 
#     get_session_history
# )

# session1 = {"configurable": {"session_id": "001"}}

# responseFromChatbot = chatbot_with_message_history.invoke(
#     [HumanMessage(content="My favorite color is red.")],
#     config=session1,
# )

# print("\n----------\n")

# print("My favorite color is red.")

# print("\n----------\n")
# print(responseFromChatbot.content)

# print("\n----------\n")

# responseFromChatbot = chatbot_with_message_history.invoke(
#     [HumanMessage(content="What's my favorite color?")],
#     config=session1,
# )

# print("\n----------\n")

# print("What's my favorite color? (in session1)")

# print("\n----------\n")
# print(responseFromChatbot.content)

# print("\n----------\n")

# session2 = {"configurable": {"session_id": "002"}}

# responseFromChatbot = chatbot_with_message_history.invoke(
#     [HumanMessage(content="What's my favorite color?")],
#     config=session2,
# )

# print("\n----------\n")

# print("What's my favorite color? (in session2)")

# print("\n----------\n")
# print(responseFromChatbot.content)

# print("\n----------\n")

# session1 = {"configurable": {"session_id": "001"}}

# responseFromChatbot = chatbot_with_message_history.invoke(
#     [HumanMessage(content="What's my favorite color?")],
#     config=session1,
# )

# print("\n----------\n")

# print("What's my favorite color? (in session1 again)")

# print("\n----------\n")
# print(responseFromChatbot.content)

# print("\n----------\n")

# session2 = {"configurable": {"session_id": "002"}}

# responseFromChatbot = chatbot_with_message_history.invoke(
#     [HumanMessage(content="Mi name is Julio.")],
#     config=session2,
# )

# print("\n----------\n")

# print("Mi name is Julio. (in session2)")

# print("\n----------\n")
# print(responseFromChatbot.content)

# print("\n----------\n")

# responseFromChatbot = chatbot_with_message_history.invoke(
#     [HumanMessage(content="What is my name?")],
#     config=session2,
# )

# print("\n----------\n")

# print("What is my name? (in session2)")

# print("\n----------\n")
# print(responseFromChatbot.content)

# print("\n----------\n")

# responseFromChatbot = chatbot_with_message_history.invoke(
#     [HumanMessage(content="What is my favorite color?")],
#     config=session1,
# )

# print("\n----------\n")

# print("What is my favorite color? (in session2)")

# print("\n----------\n")
# print(responseFromChatbot.content)

# print("\n----------\n")

# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain_core.runnables import RunnablePassthrough


# def limited_memory_of_messages(messages, number_of_messages_to_keep=2):
#     return messages[-number_of_messages_to_keep:]

# prompt = ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             "You are a helpful assistant. Answer all questions to the best of your ability.",
#         ),
#         MessagesPlaceholder(variable_name="messages"),
#     ]
# )

# limitedMemoryChain = (
#     RunnablePassthrough.assign(messages=lambda x: limited_memory_of_messages(x["messages"]))
#     | prompt 
#     | chatbot
# )

# chatbot_with_limited_message_history = RunnableWithMessageHistory(
#     limitedMemoryChain,
#     get_session_history,
#     input_messages_key="messages",
# )

# responseFromChatbot = chatbot_with_message_history.invoke(
#     [HumanMessage(content="My favorite vehicles are Vespa scooters.")],
#     config=session1,
# )

# print("\n----------\n")

# print("My favorite vehicles are Vespa scooters. (in session1)")

# print("\n----------\n")
# print(responseFromChatbot.content)

# print("\n----------\n")

# responseFromChatbot = chatbot_with_message_history.invoke(
#     [HumanMessage(content="My favorite city is San Francisco.")],
#     config=session1,
# )

# print("\n----------\n")

# print("My favorite city is San Francisco. (in session1)")

# print("\n----------\n")
# print(responseFromChatbot.content)

# print("\n----------\n")

# responseFromChatbot = chatbot_with_limited_message_history.invoke(
#     {
#         "messages": [HumanMessage(content="what is my favorite color?")],
#     },
#     config=session1,
# )

# print("\n----------\n")

# print("what is my favorite color? (chatbot with memory limited to the last 3 messages)")

# print("\n----------\n")
# print(responseFromChatbot.content)

# print("\n----------\n")

# responseFromChatbot = chatbot_with_message_history.invoke(
#     [HumanMessage(content="what is my favorite color?")],
#     config=session1,
# )

# print("\n----------\n")

# print("what is my favorite color? (chatbot with unlimited memory)")

# print("\n----------\n")
# print(responseFromChatbot.content)

# print("\n----------\n")



import warnings

from langchain._api import LangChainDeprecationWarning

warnings.simplefilter("ignore", category=LangChainDeprecationWarning)


# from langchain._api import LangChainDeprecationWarning

# warnings.simplefilter("ignore", category=LangChainDeprecationWarning)

from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv,find_dotenv

from langchain_core.messages import HumanMessage

_ = load_dotenv(find_dotenv())

groq_api_key = os.environ["GROQ_API_KEY"] 

chatbot = ChatGroq(model_name="llama-3.1-8b-instant", groq_api_key=groq_api_key)

response = chatbot.invoke(
    [HumanMessage("My favourite color is black")]
)


print(response.content)

response = chatbot.invoke(
    [HumanMessage("What is my favourite colour")]
)


print(response.content)

from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

chatbotMemory = {}

def get_session_history(session_id:str)-> BaseChatMessageHistory:
    if session_id not in chatbotMemory:
        chatbotMemory[session_id]= ChatMessageHistory()
    return chatbotMemory[session_id]

chatbot_with_message_history = RunnableWithMessageHistory(
    chatbot,
    get_session_history
)




session1 = {"configurable": {"session_id": "001"}}

response = chatbot_with_message_history.invoke([
    HumanMessage("My favourite Color is yellow")
],
config=session1)

# print(response.content)



response = chatbot_with_message_history.invoke([
    HumanMessage("What is my favourite color")
],config=session1)

# print(response.content)

response = chatbot_with_message_history.invoke([
    HumanMessage("hello my name is mihir")
],config=session1)

# print(response.content)

response = chatbot_with_message_history.invoke([
    HumanMessage("What is my name")
],config=session1)

# print(response.content)




session2 = {"configurable":{"session_id":"002"}}


response = chatbot_with_message_history.invoke([
    HumanMessage("My favourite color is red")
],config=session2)

# print(response.content)

response = chatbot_with_message_history.invoke([
    HumanMessage("What is my favourite color")
],config=session2)

# print(response.content)

response = chatbot_with_message_history.invoke([
    HumanMessage("hello my name is raj")
],config=session2)

# print(response.content)

response = chatbot_with_message_history.invoke([
    HumanMessage("What is my name")
],config=session2)

# print(response.content)

# print(chatbotMemory)
# ///////////////// rate limiting ////////////////////////////

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough

def limited_memory_of_messages(messages,number_of_messages=2):
    return messages[-number_of_messages:]

prompt = ChatPromptTemplate.from_messages(
    [
        ("system",
        "hello how are you doing tonight"),
    MessagesPlaceholder(variable_name="messages")

    ])

limitedMemoryChain = (
    RunnablePassthrough.assign(messages=lambda x:limited_memory_of_messages(x["messages"]))
    | prompt
    | chatbot
)

chatbot_with_limited_memory = RunnableWithMessageHistory(
    limitedMemoryChain,
    get_session_history,
    input_messages_key="messages"
)

# First invoke
response = chatbot_with_limited_memory.invoke(
    {"messages": [HumanMessage(content="hello my favourite sport is cricket")]}, # Pass as dict
    config=session1
)
# print(response.content)

# Second invoke
response = chatbot_with_limited_memory.invoke(
    {"messages": [HumanMessage(content="What is my name")]}, # Pass as dict
    config=session1
)

print(response.content)

print(chatbotMemory)

