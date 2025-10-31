from langchain.agents import create_agent
from langchain.tools import ToolRuntime
from app.config import LLM_MODEL_NAME, SYSTEM_PROMPT
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import InMemorySaver
from typing import Dict, Any
from langchain_core.messages import AIMessage
from app.agent_tools import retrieve_documents, index_documents

class RAGChain:
    def __init__(
        self, 
        model_name: str = LLM_MODEL_NAME,
        system_prompt: str = SYSTEM_PROMPT,
        temperature: float = 0.3,
        max_tokens: int = 1000, 
        checkpointer: ToolRuntime = InMemorySaver(),
    ):
        self.model_name = model_name
        self.system_prompt = system_prompt
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.checkpointer = checkpointer
        self.config = {"configurable": {"thread_id": "1"}}
        self.agent = self._initialize_agent()

    def _initialize_agent(self):
        model = init_chat_model(
            model=self.model_name,
            temperature=self.temperature,
            timeout=10,
            max_tokens=self.max_tokens
        )
        return create_agent(
        model=model,
        tools=[retrieve_documents, index_documents],
        system_prompt=self.system_prompt,
        checkpointer=self.checkpointer,
        )

    def _create_prompt(self, question: str):
        return {
            "messages": [
                ("user", f"Answer the following question {question}"),
            ]
        }

    def query(self, question: str) -> Dict[str, Any]:
        response = self.agent.invoke(self._create_prompt(question), config=self.config)
        messages = response.get('messages', [])
        final_message = None
        for message in messages:
            if isinstance(message, AIMessage) and not message.tool_calls:
                final_message = message.content
        return {
            'response': final_message,
        }
