from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langchain.agents  import create_agent
from dotenv import load_dotenv


load_dotenv()

email_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert email writer. Write clear, professional, and well-structured emails."
        ),
        (
            "human",
            """
Generate an email with the following details:

Purpose: {purpose}

Tone: {tone}

Receiver: {receiver}

Additional Details:
{details}

The email should include:
- Subject
- Greeting
- Email Body
- Closing
- Signature
"""
        )
    ]
)

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

chain = email_prompt | llm

response = chain.invoke({
    "purpose": "Applying for an internship",
    "tone": "Professional",
    "receiver": "HR Manager",
    "details": "I am a third-year Computer Engineering student with knowledge of Python and Machine Learning."
})

print(response.content)