import gradio as gr

from app.text_generator.generators import start_documentation
from app.rag.pipeline import execute_pipeline


def answer_question(question: str, history: str) -> str:
    response = execute_pipeline(question)
    return response


def generate_documentation() -> str:
    try:
        return start_documentation()
    except Exception as e:
        return f'Error found: {str(e)}'


def run():
    with gr.Blocks() as demo:
        gr.ChatInterface(
            fn=answer_question,
            examples=[
                "What is the mission of the company?",
                "Who is the CEO?",
                "How many employees have the company?"
            ],
            title="PayApp Bot"
        )
        generator_button = gr.Button('Generate Documentation')
        output = gr.Textbox('Output box')
        generator_button.click(fn=generate_documentation, inputs=None, outputs=output)

    demo.launch(server_name="0.0.0.0", server_port=7860)


if __name__ == "__main__":
    run()
