import gradio as gr
from langchain_bot import LangChainBot, LangChainBotException, QueryProcessingError

langchain_bot = LangChainBot("../persistence/langchain/faiss_index")

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
        
        chatbot = gr.Chatbot()
        msg = gr.Textbox(label="Your question")
        clear = gr.Button("Clear")

        msg.submit(chat, [msg, chatbot], [chatbot, chatbot])
        clear.click(lambda: None, None, chatbot, queue=False)

    return interface
