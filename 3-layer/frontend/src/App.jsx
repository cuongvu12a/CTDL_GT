import { useEffect, useState } from "react";

const API = "";

export default function App() {
  const [items, setItems] = useState([]);
  const [input, setInput] = useState("");
  const [error, setError] = useState(null);

  async function fetchItems() {
    try {
      const res = await fetch(`${API}/items`);
      setItems(await res.json());
    } catch {
      setError("Cannot connect to API");
    }
  }

  useEffect(() => {
    fetchItems();
  }, []);

  async function addItem(e) {
    e.preventDefault();
    if (!input.trim()) return;
    await fetch(`${API}/items`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name: input }),
    });
    setInput("");
    fetchItems();
  }

  async function toggleItem(item) {
    await fetch(`${API}/items/${item.id}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ done: !item.done }),
    });
    fetchItems();
  }

  async function deleteItem(id) {
    await fetch(`${API}/items/${id}`, { method: "DELETE" });
    fetchItems();
  }

  return (
    <div className="container">
      <h1>Todo List</h1>
      <p className="subtitle">Docker: React + FastAPI + PostgreSQL</p>

      {error && <div className="error">{error}</div>}

      <form onSubmit={addItem} className="form">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Add new item..."
          className="input"
        />
        <button type="submit" className="btn-add">Add</button>
      </form>

      <ul className="list">
        {items.map((item) => (
          <li key={item.id} className={`item ${item.done ? "done" : ""}`}>
            <span onClick={() => toggleItem(item)} className="item-name">
              {item.done ? "✓ " : "○ "}
              {item.name}
            </span>
            <button onClick={() => deleteItem(item.id)} className="btn-del">✕</button>
          </li>
        ))}
        {items.length === 0 && <li className="empty">No items yet.</li>}
      </ul>
    </div>
  );
}
