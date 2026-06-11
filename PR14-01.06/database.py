import sqlite3
from config import DB_PATH


def get_connection():
    """Создать соединение с SQLite"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Создать таблицу расходов"""

    conn = get_connection()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        category TEXT NOT NULL,
        amount REAL NOT NULL,
        description TEXT,
        created_at TEXT DEFAULT (datetime('now', 'localtime'))
    )
    """)

    conn.commit()
    conn.close()


def get_all_items():
    """Получить все расходы"""

    conn = get_connection()

    items = conn.execute("""
        SELECT *
        FROM expenses
        ORDER BY created_at DESC
    """).fetchall()

    conn.close()

    return items


def add_item(date, category, amount, description):
    """Добавить расход"""

    conn = get_connection()

    conn.execute(
        """
        INSERT INTO expenses
        (date, category, amount, description)
        VALUES (?, ?, ?, ?)
        """,
        (date, category, amount, description)
    )

    conn.commit()
    conn.close()


def delete_item(item_id):
    """Удалить расход"""

    conn = get_connection()

    conn.execute(
        "DELETE FROM expenses WHERE id = ?",
        (item_id,)
    )

    conn.commit()
    conn.close()


def get_stats():
    """Статистика расходов"""

    conn = get_connection()

    total_records = conn.execute(
        "SELECT COUNT(*) FROM expenses"
    ).fetchone()[0]

    total_amount = conn.execute(
        "SELECT COALESCE(SUM(amount),0) FROM expenses"
    ).fetchone()[0]

    avg_amount = conn.execute(
        "SELECT COALESCE(AVG(amount),0) FROM expenses"
    ).fetchone()[0]

    by_category = conn.execute("""
        SELECT
            category,
            COUNT(*) AS cnt,
            SUM(amount) AS total
        FROM expenses
        GROUP BY category
        ORDER BY total DESC
    """).fetchall()

    conn.close()

    return {
        "total_records": total_records,
        "total_amount": round(total_amount, 2),
        "avg_amount": round(avg_amount, 2),
        "by_category": by_category
    }