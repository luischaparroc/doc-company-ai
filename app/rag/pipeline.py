import os

import openai
from langchain.chat_models import ChatOpenAI
from llama_index import LLMPredictor, ServiceContext, StorageContext, load_index_from_storage


def execute_pipeline(question: str) -> str:
    openai_api_key = os.environ.get('OPENAI_API_KEY')
    if not openai_api_key:
        raise ValueError('"OPENAI_API_KEY" environment variable not set. Please, set this env variable')

    openai.api_key = openai_api_key

    llm_predictor = LLMPredictor(
        llm=ChatOpenAI(
            temperature=0.3,
            model_name='gpt-3.5-turbo',
            openai_api_key=os.environ.get('OPENAI_API_KEY')
        )
    )

    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

    storage_context = StorageContext.from_defaults(persist_dir='storage')

    index = load_index_from_storage(storage_context)

    query_engine = index.as_query_engine(service_context=service_context)
    response = query_engine.query(question)

    return response.response
