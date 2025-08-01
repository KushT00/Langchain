import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env
load_dotenv()

# Set the API key as an environment variable
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
# Initialize the LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-001")
## template where we fit language and text in template

from langchain_core.prompts import ChatPromptTemplate


from langchain_core.output_parsers import StrOutputParser


movie_title_template = ChatPromptTemplate.from_messages( [("user","Suggest me one single name of title of a movie to watch in language {language} and of genre {genre}  ")])

movie_title_chain = movie_title_template | llm | StrOutputParser() ## this is chain with pipe operators

response=movie_title_chain.invoke({"language": "english", "genre":"horror"})

print(response)

