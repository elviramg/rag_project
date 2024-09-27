import os
import gradio as gr
from langchain_bot import LangChainBot, LangChainBotException, QueryProcessingError


def get_faiss_index_path():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    return os.path.join(project_root, 'persistence', 'langchain', 'faiss_index')

langchain_bot = LangChainBot(get_faiss_index_path())

def chat(message, history):
    try:
        langchain_history = [(h[0], h[1]) for h in history]
        response = langchain_bot.query(message, langchain_history)
        history.append((message, response))
        
        return history, history
    except QueryProcessingError as e:
        error_message = f"Error processing query: {str(e)}"
        history.append((message, error_message))
        return history, history
    except LangChainBotException as e:
        error_message = f"Bot error: {str(e)}"
        history.append((message, error_message))
        return history, history
    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        history.append((message, error_message))
        return history, history

def create_chat_interface():
    with gr.Blocks() as interface:
        gr.Markdown("# Jane Austen Style Love Advisor")
        
        chatbot = gr.Chatbot(
            value=[
                (None, "Welcome, dear friend, to our quaint parlor of romantic counsel. Pray, what matters of the heart shall we discuss today?")
            ]
        )
        msg = gr.Textbox(label="Your question")
        clear = gr.Button("Clear")

        msg.submit(chat, [msg, chatbot], [chatbot, chatbot])
        clear.click(lambda: None, None, chatbot, queue=False)

    return interface
