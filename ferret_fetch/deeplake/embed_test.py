from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import DeepLake
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
load_dotenv()


def embed_test(texts):
    llm = OpenAI(model="text-davinci-003", temperature=0)
    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

    my_activeloop_org_id = "giantpineapplestatue"
    my_activeloop_dataset_name = "langchain_course_from_zero_to_hero"
    dataset_path = f"hub://{my_activeloop_org_id}/{my_activeloop_dataset_name}"
    db = DeepLake(dataset_path=dataset_path, embedding_function=embeddings)

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.create_documents(texts)

    db.add_documents(docs)
