from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model = ChatAnthropic()