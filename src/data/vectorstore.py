from langchain import FAISS
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings


class VectorStoreManager:
    def __init__(self):
        pass

    def get_vectorstore(self, chunks: list[str]) -> FAISS:
        embeddings = OpenAIEmbeddings()
        # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
        vectorstore = FAISS.from_texts(chunks, embeddings)
        return vectorstore
