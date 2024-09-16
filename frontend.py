import gradio as gr
from RAG import get_answer

def process_text(text):
    prompt, output = get_answer(text) 
    return prompt, output


interface = gr.Interface(
    fn=process_text, 
    inputs=gr.Textbox(label="Enter your text"),  
    outputs=[
        gr.Textbox(label="Prompt When Chunk added"),  
        gr.Textbox(label="Output")  
    ],
    title="Text Processor",
    description="Enter text to get the prompt and output."
)


interface.launch()
