# Panaversity Hackathon II: Phase 2 - Full-Stack Todo Web App

A full-stack Todo application built with Next.js, FastAPI, SQLModel, and Neon PostgreSQL.

## Features
- Full CRUD operations (Create, Read, Update, Delete)
- Permanent storage with Neon PostgreSQL
- Responsive web UI with Tailwind CSS
- RESTful API architecture

## Tech Stack
- **Frontend:** Next.js (App Router), TypeScript, Tailwind CSS
- **Backend:** FastAPI, SQLModel
- **Database:** Neon PostgreSQL

## Prerequisites
- Python 3.13+
- Node.js 18+ and npm
- Neon PostgreSQL Account

## Setup Instructions

### 1. Backend Setup
1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file and add your Neon connection string:
   ```env
   DATABASE_URL=your_neon_postgresql_url
   ```
5. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

### 2. Frontend Setup
1. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Create a `.env.local` file:
   ```env
   NEXT_PUBLIC_API_URL=http://localhost:8000
   ```
4. Run the development server:
   ```bash
   npm run dev
   ```

## API Endpoints
- `GET /todos`: List all tasks
- `POST /todos`: Create a new task
- `PATCH /todos/{id}`: Update task title or status
- `DELETE /todos/{id}`: Delete a task

## Project Structure
```text
/hackathon2
├── backend/
│   ├── main.py         # FastAPI routes
│   ├── models.py       # SQLModel definitions
│   ├── database.py     # Connection logic
│   └── .env            # Database secrets
├── frontend/
│   ├── src/app/        # Next.js pages
│   ├── src/components/ # UI Components
│   └── .env.local      # API configuration
└── README.md
```
