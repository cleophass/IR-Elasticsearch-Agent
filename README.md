# IR-Elasticsearch-Agent

Quick project using LangChain `create_agent` method to build an agent with memory for Information Retrieval. The agent can answer questions using a retrieval tool and can also index documents on demand.

## Purpose

Elasticsearch + LangChain agent with conversational memory for Information Retrieval tasks.

## Setup

### Install dependencies

```bash
uv sync
```

### Start Elasticsearch and Kibana

```bash
docker-compose up -d
```

Elasticsearch will be available at http://localhost:9200  
Kibana will be available at http://localhost:5601

### Configure environment

Create a `.env` file:

```
ANTHROPIC_API_KEY=your_anthropic_api_key
EMBEDDINGS_MODEL_NAME =your_embedding_model_name
LLM_MODEL_NAME =your_llm_model_name
ES_HOST=your_elasticsearch_host
```

## Usage

```bash
uv run main.py
```

Ask questions like:
- "Find articles about machine learning"
- "Search for technology articles"
- "What is deep learning?"

Type `exit` or `quit` to quit.
