from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import ConversationalRetrievalChain


class LangChainBotException(Exception):
    """Base exception class for LangChainBot"""

class VectorStoreLoadError(LangChainBotException):
    """Raised when there's an error loading the vector store"""

class QueryProcessingError(LangChainBotException):
    """Raised when there's an error processing a query"""

class LangChainBot:
    def __init__(self, vectorstore_path: str):
        self.llm = ChatOpenAI(model="gpt-3.5-turbo")
        self.embeddings = OpenAIEmbeddings()
        self.vectorstore = self.load_vectorstore(vectorstore_path)
        self.rag_chain = self.setup_rag_chain()
        self.chat_history = []

    def load_vectorstore(self, path: str) -> FAISS:
        try:
            return FAISS.load_local(path, self.embeddings, allow_dangerous_deserialization=True)
        except Exception as e:
            raise VectorStoreLoadError(f"Failed to load vector store from {path}: {str(e)}")

    def setup_rag_chain(self) -> ConversationalRetrievalChain:
        template = """
        You are a love advisor with the wisdom and style of Jane Austen, the author of "Pride and Prejudice."
        Based solely on the content of the book and the time period in which it was written, provide advice on relationships and love.

        Book context: {context}

        User's question: {question}

        Please follow these instructions when responding:
        1. Provide love advice that reflects the values and sensibilities of Jane Austen's era, but adapted to the user's modern situation.
        2. The advice must be strictly based on the information and themes present in "Pride and Prejudice."
        3. Include a relevant quote from the book that supports your advice.
        4. Be polite, witty, and a bit formal in your response, as an Austen character would be.
        5. If there is no relevant information in the provided context to answer the question, politely admit it.

        Advice:
        """

        prompt = PromptTemplate(
            input_variables=["context", "question"],
            template=template
        )

        return ConversationalRetrievalChain.from_llm(
                llm=self.llm,
                retriever=self.vectorstore.as_retriever(search_type="similarity", k=3),
                combine_docs_chain_kwargs={"prompt": prompt},
                return_source_documents=True,
                verbose=True
            )

    def query(self, question: str, chat_history: list = None) -> str:
        try:
            result = self.rag_chain({"question": question, "chat_history": chat_history or []})
            answer = result.get('answer')
            if answer is None:
                return "Sorry, I couldn't generate a response. Could you rephrase your question?"
            return answer
        except Exception as e:
            raise QueryProcessingError(f"Error processing query: {str(e)}")
