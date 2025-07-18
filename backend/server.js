const express = require('express');
const axios = require('axios');
const cors = require('cors');
const app = express();
const PORT = 5000;

app.use(cors());

app.get('/api/pnr/:pnr', async (req, res) => {
  const { pnr } = req.params;
  try {
    const response = await axios.get(`https://api.railwayapi.site/api/v1/pnr/check/${pnr}`);
    res.json(response.data);
  } catch (err) {
    res.status(500).json({ error: 'PNR not found or API error' });
  }
});

app.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));
