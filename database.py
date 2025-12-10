import aiosqlite
import asyncio


class Database:
    def __init__(self, path="db.sqlite"):
        self.path = path
        self.db = None

    async def connect(self):
        self.db = await aiosqlite.connect(self.path)
        await self.db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                role TEXT,
                phone TEXT,
                car_model TEXT,
                active_order INTEGER
            );
        """)
        await self.db.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER,
                cargo TEXT,
                from_addr TEXT,
                to_addr TEXT,
                phone TEXT,
                driver_id INTEGER,
                status TEXT,
                tg_chat_id TEXT,
                tg_message_id INTEGER,
                reserved_until INTEGER,
                created_at INTEGER DEFAULT (strftime('%s','now'))
            );
        """)
        await self.db.execute("""
            CREATE TABLE IF NOT EXISTS sessions (
                chat_id INTEGER PRIMARY KEY,
                step TEXT,
                temp JSON
            );
        """)
        await self.db.commit()

    async def set_role(self, user_id, role):
        await self.db.execute("INSERT OR REPLACE INTO users (user_id, role) VALUES (?, ?)", (user_id, role))
        await self.db.commit()


db = Database()
# Optionally connect immediately when imported in main