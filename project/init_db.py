from models import get_db, init_db

init_db()

conn = get_db()
cur = conn.cursor()

# Добавляем тестовые статьи
cur.execute("INSERT INTO articles (title, content) VALUES (?, ?)",
            ("Первая статья", "Это содержимое первой статьи."))
cur.execute("INSERT INTO articles (title, content) VALUES (?, ?)",
            ("Вторая статья", "А это текст второй статьи."))

conn.commit()
conn.close()

print("База инициализирована!")
