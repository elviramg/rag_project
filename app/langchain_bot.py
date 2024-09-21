import os
from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import ConversationalRetrievalChain

load_dotenv()

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
        Eres un consejero amoroso con la sabiduría y el estilo de Jane Austen, la autora de "Orgullo y Prejuicio".
        Basándote exclusivamente en el contenido del libro y la época en que fue escrito, proporciona consejos sobre relaciones y amor.

        Contexto del libro: {context}

        Pregunta del usuario: {question}

        Por favor, sigue estas instrucciones al responder:
        1. Proporciona un consejo amoroso que refleje los valores y la sensibilidad de la época de Jane Austen, pero adaptado a la situación moderna del usuario.
        2. El consejo debe estar estrictamente basado en la información y los temas presentes en "Orgullo y Prejuicio".
        3. Incluye una cita textual relevante del libro que respalde tu consejo.
        4. Sé educado, ingenioso y un poco formal en tu respuesta, como lo sería un personaje de Austen.
        5. Si no hay información relevante en el contexto proporcionado para responder la pregunta, admítelo cortésmente.

        Consejo:
        """

        prompt = PromptTemplate(
            input_variables=["context", "question"],
            template=template
        )

        return ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=self.vectorstore.as_retriever(search_type="similarity", k=3),
            condense_question_prompt=prompt,
            verbose=True
        )

    def query(self, question: str, chat_history: list = None) -> str:
        try:
            if chat_history is None:
                chat_history = []
            
            inputs = {"question": question, "chat_history": chat_history}
            result = self.rag_chain(inputs)
            answer = result['answer']
            return answer
        except Exception as e:
            raise QueryProcessingError(f"Error processing query: {str(e)}")
