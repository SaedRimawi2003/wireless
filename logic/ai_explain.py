from openai import AzureOpenAI
import re

client = AzureOpenAI(
    api_key="1cOuw0n9gKhQxzhyg6ElpSP83qOdhWyoEKn7oKM8RIwRvyL7qDbtJQQJ99BFACHYHv6XJ3w3AAAAACOGCXa0",
    api_version="2023-05-15",
    azure_endpoint="https://12117-mcai2brr-eastus2.openai.azure.com/"
)

DEPLOYMENT_NAME = "gpt-35-turbo"

def generate_explanation(scenario, data):
    prompt = f"You are an AI tutor helping a student understand results from the {scenario} calculation. Explain the following technical result clearly, and why it's important:\n{data}"

    response = client.chat.completions.create(
        model=DEPLOYMENT_NAME,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.6,
        max_tokens=300
    )

    raw_text = response.choices[0].message.content
    clean_text = re.sub(r'\s*\n\s*', ' ', raw_text).strip()
    return clean_text
