import google.generativeai as genai
import textwrap
import markdown
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def to_markdown(text):
    # Convert text to markdown format
    return textwrap.dedent(f"""
    {text}
    """)

# Set your Google API key
GOOGLE_API_KEY = "GOOGLE_API_KEY "
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def get_completion(prompt):
    if not prompt:
        return "Empty Error Prompt."
    
    formatted_prompt = (
        f"Give me the Code Review of the diff in \"{prompt}\". "
        "Check for any potential bugs or flaws that might occur "
        "and give me a scale from 1 to 10 as to how severe this could be."
    )
    
    try:
        response = model.generate_content(formatted_prompt)
        logger.debug(f"API response: {response}")
        return markdown.markdown(to_markdown(response.text))
    except Exception as e:
        logger.error(f"API Retrieval Error: {e}")
        return f"API Retrieval Error, Your Error Prompt was: {prompt}."

def solve_error_prompts(error_prompts):
    return [get_completion(prompt) for prompt in error_prompts]

def main():
    error_prompts = ["My pipeline is not working"]
    completions = solve_error_prompts(error_prompts)
    for completion in completions:
        print(completion)

if __name__ == "__main__":
    main()
