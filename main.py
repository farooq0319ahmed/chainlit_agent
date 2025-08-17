# code name: -> Chainlit Introduction | OpenAI Agent-SDK
#from chainlit import on_chat_start, Message
# --------------------------------------------------
#@on_chat_start # start hone ke foran bad
#async def my_start():
#    await Message(content="hello, i am Farooq").send()
# ---------------------------------------------------
# command uv run chainlit run main.py -w
# ---------------------------------------------------


import chainlit as cl
# --------------------------------------------------
@cl.on_chat_start # start hone ke foran bad
async def my_start():
    await cl.Message(content="hello, i am Farooq").send()
# ---------------------------------------------------
@cl.on_message # jab user koi message bheje
async def my_message(msg: cl.Message):
    user_input = msg.content
    await cl.Message(content=user_input).send()  # user ka message wapis bhej do