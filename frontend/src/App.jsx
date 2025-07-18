// frontend/src/App.jsx
import { useState } from 'react';
import axios from 'axios';

function App() {
  const [pnr, setPnr] = useState('');
  const [result, setResult] = useState(null);

  const checkPnr = async () => {
    try {
      const res = await axios.get(`http://localhost:5000/api/pnr/${pnr}`);
      setResult(res.data);
    } catch (err) {
      alert('Error fetching PNR data');
    }
  };

  return (
    <div className="p-6 max-w-md mx-auto">
      <h1 className="text-2xl font-bold mb-4">PNR Status Checker</h1>
      <input
        type="text"
        className="border p-2 w-full"
        placeholder="Enter 10-digit PNR"
        value={pnr}
        onChange={(e) => setPnr(e.target.value)}
      />
      <button onClick={checkPnr} className="bg-blue-600 text-white px-4 py-2 mt-2">
        Check Status
      </button>

      {result && (
        <div className="mt-4 border p-4">
          <p><strong>Train:</strong> {result.train.name} ({result.train.number})</p>
          <p><strong>From:</strong> {result.from_station.name}</p>
          <p><strong>To:</strong> {result.to_station.name}</p>
          <p><strong>Boarding:</strong> {result.boarding_point.name}</p>
          <p><strong>Date:</strong> {result.doj}</p>
          <ul>
            {result.passengers.map((p, i) => (
              <li key={i}>{p.no}: {p.current_status}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
