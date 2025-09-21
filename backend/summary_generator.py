from langchain_ollama import ChatOllama
import os
from logger import setup_logger

logger = setup_logger(__name__)

def generate_summary(file_path: str, output_file: str = "OutputFiles/summary.txt") -> None:
    """
    Generate a summary of the content in the specified file using an LLM and save it.
    """
    try:
        logger.info(f"Generating summary for {file_path}")
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        llm = ChatOllama(
            model="llama3.1:8b",
            base_url="http://localhost:11434",
            temperature=0,
        )
        prompt = f'''
        You are a helpful assistant that explains content.
        Write it in bullet points. Your points should cover the main ideas and key details of the content.
        {content}
        ''' 
        response = llm.invoke(prompt)
        with open(output_file, "w", encoding="utf-8") as summary_file:
            summary_file.write(response.content)
        logger.info(f"Summary saved successfully: {output_file}")
    except Exception as e:
        logger.error(f"Summary generation failed: {e}")