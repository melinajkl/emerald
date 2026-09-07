# Emerald Monorepo

Full-stack application powered by a **FastAPI** backend, a **Next.js** (App Router) frontend, and a **PostgreSQL** database, fully orchestrated with **Docker Compose**.

---

## Architecture Overview

* **Frontend**: Next.js 14+ (TypeScript, Tailwind CSS, App Router) → `http://localhost:3000`
* **Backend**: FastAPI (Python) → `http://localhost:8080`
* **Database**: PostgreSQL 16 → `localhost:5433` (internal port `5432`)

---

## Prerequisites

Ensure you have the following installed on your machine:

* [Docker Desktop](https://www.docker.com/products/docker-desktop/) (or Docker Engine + Docker Compose plugin)
* [Node.js](https://nodejs.org/) (v20+ recommended, for local IDE tooling/autocompletion)
* [Git](https://git-scm.com/)

---

## Project Structure

```text
emerald/
├── backend/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── src/
│   ├── Dockerfile
│   ├── package.json
│   └── next.config.mjs
├── docker-compose.yaml
└── README.md

```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone git@github.com:melinajkl/emerald.git # via SSH
git clone https://github.com/melinajkl/emerald.git # via HTTPS
cd emerald

```

### 2. Run the Full Stack with Docker

Start all services (Frontend, Backend, Database) in detached mode:

```bash
docker compose up -d --build

```

To view logs across all services:

```bash
docker compose logs -f

```

To view logs for a specific service:

```bash
docker compose logs -f frontend
docker compose logs -f backend

```

---

## Environment & Service Endpoints

| Service | Host URL | Container Name | Notes |
| --- | --- | --- | --- |
| **Frontend** | `http://localhost:3000` | `emerald_frontend` | Next.js Dev Server |
| **Backend** | `http://localhost:8080` | `emerald_backend` | FastAPI Server |
| **FastAPI Docs** | `http://localhost:8080/docs` | `emerald_backend` | Swagger UI |
| **PostgreSQL** | `localhost:5433` | `postgres-emerald` | DB: `emerald_db`, User: `postgres` |

---

## Database Credentials

When connecting from your host machine (e.g., via DBeaver or TablePlus):

* **Host**: `localhost`
* **Port**: `5433`
* **Database**: `emerald_db`
* **Username**: `postgres`
* **Password**: `postgrespassword`

When connecting from the **FastAPI container**, use the internal service name:

```text
postgresql://postgres:postgrespassword@web-services-db:5432/emerald_db

```

---

## Development Workflow

### Hot Reloading

Both the frontend and backend volumes are mapped to your local host files:

* Edits in `./frontend/src` immediately trigger Next.js Fast Refresh.
* Edits in `./backend` reflect in the FastAPI application.

### Rebuilding a Single Service

If you modify dependencies (`package.json` or `requirements.txt`), rebuild only that container:

```bash
# Rebuild Frontend
docker compose build --no-cache frontend
docker compose up -d frontend

# Rebuild Backend
docker compose build --no-cache backend
docker compose up -d backend

```

### Resetting the Environment

To shut down containers and clear the database volume:

```bash
docker compose down -v

```