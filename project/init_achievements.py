from models import get_db, init_db

if __name__ == "__main__":
    init_db()
    conn = get_db()
    cur = conn.cursor()

    achievements = [
        ("Первый шаг", "Открыть первую статью", None),
        ("Читатель", "Прочитать 5 статей", None),
        ("Коллекционер", "Собрать все ачивки", None)
    ]

    cur.executemany("INSERT INTO achievements (name, description, icon) VALUES (?, ?, ?)", achievements)
    conn.commit()
    conn.close()
    print("Ачивки добавлены!")
