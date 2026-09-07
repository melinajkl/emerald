import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI(
    title="Emerald API",
    description="Backend API for Emerald Knowledge Base",
    version="0.1.0"
)

# Allow requests from your Next.js frontend container / host
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    """Health check endpoint."""
    return {"status": "ok", "service": "Emerald Backend"}

@app.get("/api/health")
def health_check():
    """Detailed health check for database connection testing."""
    db_user = os.getenv("POSTGRES_USER", "not_set")
    return {
        "status": "healthy",
        "database_user": db_user
    }

# Entrypoint for running directly with python backend/app.py
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True)