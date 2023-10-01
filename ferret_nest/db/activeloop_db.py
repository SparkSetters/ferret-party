from langchain.vectorstores import DeepLake
from langchain.embeddings.openai import OpenAIEmbeddings


def create_db_connection(model, dataSet):
    embeddings = OpenAIEmbeddings(model=model)
    my_activeloop_org_id = "giantpineapplestatue"
    my_activeloop_dataset_name = dataSet
    dataset_path = f"hub://{my_activeloop_org_id}/{my_activeloop_dataset_name}"
    db = DeepLake(dataset_path=dataset_path, embedding_function=embeddings)
    return db
