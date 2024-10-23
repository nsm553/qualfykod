import os
from dotenv import load_dotenv
from openai import OpenAI
from together import Together

load_dotenv()

client = OpenAI (api_key=os.getenv("TOGETHER_API_KEY"))

def query(category: str, input: str):

    if category == "bug_detection":

        prompt = f"""Analyzing this bug detection result: '{input}', formulate 3 targeted questions for developers. Each question should:
        1. Point to a specific bug or potential issue.
        2. What is the root cause and potential impact.
        3. Suggest an approach to debug or possible fix.
        Consider bug types such as logical errors, runtime exceptions, and edge cases."""

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an expert software engineer specializing in code analysis. Provide actionable advice."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=
        )

    except Exception as e:
        err = f"Error getting response from OpenAI: {str(e)}"
        print(err)
        return err