import gradio as gr
from chat_interface import create_chat_interface

if __name__ == "__main__":
    interface = create_chat_interface()
    # This helps us create a temporary public URL
    interface.launch(share=True)