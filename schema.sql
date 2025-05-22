CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    type TEXT CHECK(type IN ('收入', '支出')) NOT NULL,
    category TEXT NOT NULL,
    amount REAL NOT NULL,
    description TEXT
);