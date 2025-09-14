from langchain_ollama import ChatOllama
import os

def generate_summary(file_path: str, output_file: str = "OutputFiles/summary.txt") -> None:
    """
    Generate a summary of the content in the specified file using an LLM and save it.
    """
    try:
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
        print(f"Summary saved to {output_file}")
    except Exception as e:
        print(f"An error occurred while generating the summary: {e}")