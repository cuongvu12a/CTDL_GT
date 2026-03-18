import os
from contextlib import asynccontextmanager
import psycopg2
from psycopg2.extras import RealDictCursor
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

DATABASE_URL = os.getenv("DATABASE_URL", "postgres://admin:secret@localhost:5432/myapp")


def get_conn():
    return psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)


def init_db():
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS items (
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL,
                    done BOOLEAN DEFAULT FALSE,
                    created_at TIMESTAMP DEFAULT NOW()
                )
            """)
        conn.commit()


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(title="Docker Learning API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class ItemCreate(BaseModel):
    name: str


class ItemUpdate(BaseModel):
    done: bool


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/items")
def list_items():
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM items ORDER BY created_at DESC")
            return cur.fetchall()


@app.post("/items", status_code=201)
def create_item(body: ItemCreate):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO items (name) VALUES (%s) RETURNING *",
                (body.name,),
            )
            item = cur.fetchone()
        conn.commit()
    return item


@app.patch("/items/{item_id}")
def update_item(item_id: int, body: ItemUpdate):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE items SET done=%s WHERE id=%s RETURNING *",
                (body.done, item_id),
            )
            item = cur.fetchone()
        conn.commit()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM items WHERE id=%s", (item_id,))
        conn.commit()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=3000, reload=True)
