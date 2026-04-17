# SmartCart AI – Predictive Retail Assistant

## Problem
Retail systems are reactive and inefficient.

## Solution
AI-powered predictive shopping + inventory optimization. This system simulates autonomous retail decision-making using lightweight AI logic, optimized for scalability on cloud platforms like Google Cloud Run.

## Features
- Smart recommendations
- Auto cart generation
- Inventory optimization
- Explainable AI

## Tech Stack
- FastAPI
- Python
- Google Cloud Run

## Architecture & Google Cloud Integration
This lightweight API is designed to be fully containerized via Docker and deployed continuously using **Google Cloud Run**. The containerized deployment model is perfect for handling elastic retail traffic bursts while scaling to zero during off-peak hours.
While the current version utilizes simulated, fast in-memory inference, a future scale out would leverage **Google BigQuery** for managing historical purchase sequences, feeding into advanced Matrix Factorization or LLM based vector engines, all without rewriting the API layer.

## Security
- Input validation via Pydantic
- No sensitive data stored
- Safe API design

## How to Run
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Testing
```bash
pytest
```

## Future Scope
- ML models
- Real-time analytics
- Full frontend

## Deployment (Cloud Run)
1. Build the container: `docker build -t smartcart-ai .`
2. Push to Artifact Registry (or Google Container Registry).
3. Deploy to Cloud Run using `gcloud run deploy`.
