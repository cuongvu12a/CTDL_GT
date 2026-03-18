const express = require('express');
const http = require('http');
const { Server } = require('socket.io');
const { Pool } = require('pg');
const path = require('path');

const app = express();
const server = http.createServer(app);
const io = new Server(server);

const pool = new Pool({
  host: process.env.POSTGRES_HOST || 'db',
  user: process.env.POSTGRES_USER || 'postgres',
  password: process.env.POSTGRES_PASSWORD || 'postgres',
  database: process.env.POSTGRES_DB || 'votes',
});

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.get('/', (req, res) => {
  res.render('index');
});

async function getResults() {
  try {
    const res = await pool.query('SELECT vote, COUNT(*) as count FROM votes GROUP BY vote');
    const results = { a: 0, b: 0 };
    res.rows.forEach(row => {
      results[row.vote] = parseInt(row.count);
    });
    return results;
  } catch {
    return { a: 0, b: 0 };
  }
}

io.on('connection', (socket) => {
  const interval = setInterval(async () => {
    const results = await getResults();
    socket.emit('results', results);
  }, 1000);

  socket.on('disconnect', () => clearInterval(interval));
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => console.log(`Result service on port ${PORT}`));
