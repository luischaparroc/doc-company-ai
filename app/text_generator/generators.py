from llama_index import VectorStoreIndex, SimpleDirectoryReader

from app.llm_systems.supported_llm_systems import SupportedLLMSystems
from app.llm_systems.messages_config import ChatGPTMessage
from app.text_generator import prompts


def generate_information(prompt: str, output_file: str) -> None:
    chatgpt = SupportedLLMSystems.CHATGPT.get_llm_system()
    messages = [
        ChatGPTMessage(content=prompt, role='user')
    ]

    company_context = chatgpt.request(messages, temperature=1)

    with open(output_file, 'w') as f:
        f.write(company_context)


def persist_embeddings() -> None:
    reader = SimpleDirectoryReader(input_dir='app/text_generator/documentation')
    documents = reader.load_data()
    index = VectorStoreIndex.from_documents(documents, show_progress=True)
    index.storage_context.persist()


def start_documentation() -> str:
    generate_information(
        prompt=prompts.COMPANY_PROMPT,
        output_file='app/text_generator/documentation/company_context.txt'
    )
    generate_information(
        prompt=prompts.TECHNOLOGY_PROMPT,
        output_file='app/text_generator/documentation/technology_context.txt'
    )
    generate_information(
        prompt=prompts.CUSTOMER_SUCCESS_PROMPT,
        output_file='app/text_generator/documentation/customer_success_context.txt'
    )
    generate_information(
        prompt=prompts.PEOPLE_PROMPT,
        output_file='app/text_generator/documentation/people_context.txt'
    )
    generate_information(
        prompt=prompts.FINANCE_PROMPT,
        output_file='app/text_generator/documentation/finance_context.txt'
    )
    generate_information(
        prompt=prompts.LEGAL_PROMPT,
        output_file='app/text_generator/documentation/legal_context.txt'
    )
    generate_information(
        prompt=prompts.MARKETING_PROMPT,
        output_file='app/text_generator/documentation/marketing_context.txt'
    )
    generate_information(
        prompt=prompts.PRODUCT_PROMPT,
        output_file='app/text_generator/documentation/product_context.txt'
    )
    persist_embeddings()

    return 'Information generated successfully'
