# FastAPI + React LLM Chat Interface

A full-stack application that enables users to chat with an LLM model.

## Tech Stack

- **Backend**: Python 3.11 + FastAPI + LangChain
- **Frontend**: React 18 + TypeScript + Vite + Tailwind CSS
- **Testing**: pytest (backend), vitest (frontend)

## Project Structure

```
/backend
  ├── app/
  │   ├── main.py              # FastAPI app + router include
  │   ├── routers/llm.py       # /ask endpoint → LangChain call
  │   └── services/llm_client.py
  ├── tests/
  │   └── test_llm.py
  ├── requirements.txt
  └── .env.example
/frontend
  ├── src/
  │   ├── App.tsx
  │   ├── components/
  │   └── hooks/
  └── ...
```

## Setup Instructions

### Prerequisites

- Python 3.11+
- Node.js 16+
- npm or yarn

### Backend Setup

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file based on `.env.example` and add your API key:
   ```
   cp .env.example .env
   # Now edit .env to add your API key
   ```

5. Run the backend server:
   ```
   uvicorn app.main:app --reload
   ```
   
   **Troubleshooting**: If you encounter a `UnicodeDecodeError` on startup, ensure your `.env` file is saved with UTF-8 encoding (not UTF-8 with BOM).

### Frontend Setup

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Run the frontend development server:
   ```
   npm run dev
   ```
    
    The frontend will be available at `http://localhost:5173` (or the next available port).

## Development

It is recommended to run the backend and frontend servers in separate terminals to manage them independently.

1. **Terminal 1 (Backend):**
   ```
   cd backend
   source venv/bin/activate  # Or venv\Scripts\activate on Windows
   uvicorn app.main:app --reload
   ```

2. **Terminal 2 (Frontend):**
   ```
   cd frontend
   npm run dev
   ```

## Testing

### Backend Tests

```
cd backend
source venv/bin/activate  # Or venv\Scripts\activate on Windows
pytest
```

### Frontend Tests

```
cd frontend
npm test
```

## API Endpoints

- `GET /`
  - Response: `{ "message": "Welcome to the LLM API!" }`
- `POST /api/ask`
  - Request: `{ "question": string }`
  - Response: `{ "answer": string }` 