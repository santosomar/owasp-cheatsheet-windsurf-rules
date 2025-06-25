import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

MAX_CONTENT_LENGTH = 8000

def summarize_cheatsheet(content, api_key):
    """Summarizes the cheatsheet content if it's too long."""
    client = OpenAI(api_key=api_key)
    prompt = f"Summarize the key takeaways and actionable security advice from the following OWASP cheatsheet. The summary should be concise and capture the most critical points for a developer to follow. Cheatsheet content:\n\n{content}"
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are an expert in summarizing technical security documents."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error summarizing content: {e}"

def generate_rule(cheatsheet_content, api_key):
    """
    Generates a Windsurf IDE rule using OpenAI's GPT-4.1-mini model.

    Args:
        cheatsheet_content (str): The content of the OWASP cheatsheet.
        api_key (str): Your OpenAI API key.

    Returns:
        str: The generated Windsurf rule in Markdown format.
    """
    client = OpenAI(api_key=api_key)

    prompt = f"""\
Create a Windsurf IDE rule based on the following OWASP cheatsheet material.

The rule must start with a YAML frontmatter for configuration:
```
---
trigger: glob
globs: [a comma-separated list of relevant file extensions]
---

Then the rest of the rule here based on the cheatsheet material...
```

The rule must provide actionable advice and best practices based on the topic of the cheatsheet to the coding agent/software developer.
THe rule should be concise and capture the most critical points for a developer to follow. 

Determine the most appropriate file extensions for the 'globs' field based on the cheatsheet's content.

{cheatsheet_content}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are an expert in software security and Windsurf IDE rule creation."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating rule: {e}"

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not set.")
        return

    cheatsheet_dir = os.path.join(os.path.dirname(__file__), '..', 'cheatsheets')
    rules_dir = os.path.join(os.path.dirname(__file__), '..', 'rules')

    if not os.path.exists(rules_dir):
        os.makedirs(rules_dir)

    for filename in os.listdir(cheatsheet_dir):
        if filename.endswith(".md"):
            cheatsheet_path = os.path.join(cheatsheet_dir, filename)
            rule_filename = f"sdlc-{os.path.splitext(filename)[0]}.md"
            rule_path = os.path.join(rules_dir, rule_filename)

            print(f"Processing {filename}...")

            with open(cheatsheet_path, 'r', encoding='utf-8') as f:
                cheatsheet_content = f.read()

            if len(cheatsheet_content) > MAX_CONTENT_LENGTH:
                print(f"  Content is too long, summarizing {filename}...")
                cheatsheet_content = summarize_cheatsheet(cheatsheet_content, api_key)

            rule_content = generate_rule(cheatsheet_content, api_key)

            with open(rule_path, 'w', encoding='utf-8') as f:
                f.write(rule_content)

            print(f"  Successfully created {rule_filename}")

if __name__ == "__main__":
    main()


