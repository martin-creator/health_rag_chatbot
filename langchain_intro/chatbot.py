import dotenv
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

# Chat model provides a simple interface to interact with OpenAI's GPT-3.5 model
chat_model = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)