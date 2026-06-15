import streamlit as st
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper,WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun,WikipediaQueryRun,DuckDuckGoSearchRun
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
import os
from dotenv import load_dotenv
import uuid
load_dotenv()
os.environ['GROQ_API_KEY']=os.getenv('GROQ_API_KEY')


#used inbuilt tool of wikipedia
api_wrapper_wiki=WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=250)
wiki=WikipediaQueryRun(api_wrapper=api_wrapper_wiki)
api_wrapper_arxiv=ArxivAPIWrapper(top_k_results=1,doc_content_chars_max=250)
arxiv=ArxivQueryRun(api_wrapper=api_wrapper_arxiv)
search=DuckDuckGoSearchRun()

tools=[arxiv,search,wiki]



from langgraph.checkpoint.memory import InMemorySaver



if 'messages' not in st.session_state:
    st.session_state['messages']=[
        {'role':'assistant','content':'hi i am chatbot who can search the web , wikipedia and research papers.how can i help you?'}
    ]

if 'thread_id' not in st.session_state:
    st.session_state['thread_id']=uuid.uuid4()

if "memory" not in st.session_state:
    st.session_state.memory = InMemorySaver()

for msg in st.session_state.messages:
    st.chat_message(msg['role']).write(msg['content'])

llm=ChatGroq(model='qwen/qwen3-32b',streaming=True)

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="You are a helpful assistant.respond to questions with provided context",
    checkpointer=st.session_state.memory,

)

if prompt:=st.chat_input(placeholder='what is machine learning'):
    st.session_state.messages.append({'role':'user','content':prompt})
    st.chat_message('user').write(prompt)

    
    with st.chat_message('assistant'):
        st_cb=StreamlitCallbackHandler(st.container(),expand_new_thoughts=True)
        response = agent.invoke(
    {
        "messages": [
            ("user", f"{prompt}")
        ]
    },
    config={"configurable": {"thread_id": st.session_state.thread_id},'callbacks':[st_cb]}
)

    st.chat_message('ai').write(response['messages'][-1].content)
    st.session_state.messages.append({'role':'ai','content':response['messages'][-1].content})
    
    


