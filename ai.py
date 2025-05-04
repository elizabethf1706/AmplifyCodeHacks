# this file is ment to essentially set up the ai.
# this is mean to allow for web scraping. ai will call  this multiple times with different prompts 
# Mixtral-8x7b-32768 
# 
# groq_client.py

import groq  # Ensure groq SDK is installed

# Initialize the Groq client with your API key
client = groq.Client(api_key="")
prompt_template = """
You are an expert at generating keyword variations specifically for use in web scraping. 
Given a user's request, generate a list of precise and useful scraping prompts that can be used to search for relevant data online.
Focus only on phrases or keywords, not full sentences. Avoid commentary, explanation, or formatting.

User request: "{}"

Scraper prompts:
"""
prompt_template = """
You are an expert at generating keyword variations specifically for use in web scraping. 
Given a user's request, generate a list of precise and useful scraping prompts that can be used to search for relevant data online.
Focus only on phrases or keywords, not full sentences. Avoid commentary, explanation, or formatting.

User request: "{}"

Scraper prompts:
"""

def generate_prompt(user_query):
    """Generate expanded scraping prompts using the LLaMA 3.3 70B model."""
    formatted_prompt = prompt_template.format(user_query)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": formatted_prompt}
        ],
        temperature=0.7,
        max_tokens=512,
    )

    content = response.choices[0].message.content
    return [line.strip('- ').strip() for line in content.split("\n") if line.strip()]