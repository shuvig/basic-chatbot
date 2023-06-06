from langchain.chains.conversational_retrieval.base import BaseConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI


class ConversationManager:
    def __init__(self):
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    def get_conversation(self, vectorstore) -> BaseConversationalRetrievalChain:
        llm = ChatOpenAI()
        return ConversationalRetrievalChain.from_llm(llm=llm,
                                                     retriever=vectorstore.as_retriever(),
                                                     memory=self.memory)

    @staticmethod
    def handle_user_question(question, conversation):
        response = conversation({"question": question})
        return response
