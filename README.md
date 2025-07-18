// README.md
# PNR Status Checker

## How to Run Locally

### 1. Clone the Repo
```bash
git clone <your-repo-url>
cd pnr-status-checker
```

### 2. Setup Backend
```bash
cd backend
npm install
npm start
```

This will start backend at: `http://localhost:5000`

### 3. Setup Frontend
```bash
cd ../frontend
npm install
npm run dev
```

This will start frontend at: `http://localhost:5173`

Ensure CORS is enabled in backend.

---

You can now enter a PNR on the frontend and fetch results from the backend via the Railway API.