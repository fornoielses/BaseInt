from models import get_db, init_db

if __name__ == "__main__":
    init_db()
    conn = get_db()
    cur = conn.cursor()

    tasks = [
        (1, "Как посмотреть статистику пользователей на коммутаторе?", "show users"),
        (1, "Как посмотреть таблицу MAC-адресов?", "show mac address-table"),
        (2, "Напишите простую команду вывода текста в Python", "print('Hello')")
    ]

    cur.executemany("INSERT INTO tasks (article_id, question, answer) VALUES (?, ?, ?)", tasks)
    conn.commit()
    conn.close()
    print("Задачи добавлены!")
