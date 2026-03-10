from dotenv import load_dotenv
from PyPDF2 import PdfReader
import streamlit as st
from langchain_community.embeddings import OpenAIEmbeddings, SentenceTransformerEmbeddings
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.memory import ConversationBufferWindowMemory
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv()

def get_pdf_text(pdf_docs):
    """ PDF 문서에서 텍스트를 추출 """
    text = ''
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    """ 지정된 조건에 따라 주어진 텍스트를 더 작은 덩어리로 분할 """
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", " ", ""],
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    """ 주어진 텍스트 청크에 대한 임베딩을 생성하고 FAISS를 사용하여 벡터 저장소를 생성 """
    embeddings = SentenceTransformerEmbeddings(model_name='all-MiniLM-L6-v2')
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    """ 주어진 벡터 저장소로 대화 체인을 초기화 """
    # ConversationBufferWindowMemory에 이전 대화 저장
    memory = ConversationBufferWindowMemory(memory_key='chat_history',
                                            return_messages=True)

    # ConversationalRetrievalChain을 통해 langchain 챗봇에 쿼리 전송
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(temperature=0, model_name='gpt-4o-mini'),
        retriever=vectorstore.as_retriever(),
        get_chat_history=lambda h: h,
        memory=memory
    )
    return conversation_chain

user_uploads = st.file_uploader('파일을 업로드해주세요.', accept_multiple_files=True)
if user_uploads:
    # PDF 문서에서 텍스트 추출
    raw_text = get_pdf_text(user_uploads)
    st.write('업로드된 PDF 파일의 내용:', raw_text)

    # 텍스트에서 청크로 분할
    text_chunks = get_text_chunks(raw_text)
    st.write('텍스트 청크:', text_chunks)

    # 벡터 저장소 생성
    vectorstore = get_vectorstore(text_chunks)
    st.write('벡터 저장소 생성 완료!')

    # 대화 체인 생성
    st.session_state.conversation = get_conversation_chain(vectorstore)
    st.write('대화 체인 생성 완료!')

if user_query := st.chat_input('질문을 입력해주세요.'):
    # 대화 체인을 사용하여 사용자의 메시지를 처리
    if 'conversation' in st.session_state:
        result = st.session_state.conversation({
            'question': user_query,
            'chat_history': st.session_state.get('chat_history', [])
        })
        response = result['answer']
    else:
        response = '먼저 문서를 업로드해주세요.'
    with st.chat_message('assistant'):
        st.write(response)

