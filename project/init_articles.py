from models import get_db, init_db

if __name__ == "__main__":
    init_db()
    conn = get_db()
    cur = conn.cursor()

    articles = [
        ("Основы работы с коммутатором", 
         "В этой статье мы рассмотрим базовые команды для работы с сетевыми коммутаторами."),
        ("Введение в Python", 
         "Python — это универсальный язык программирования. В этой статье мы напишем первую программу.")
    ]

    cur.executemany("INSERT INTO articles (title, content) VALUES (?, ?)", articles)
    conn.commit()
    conn.close()
    print("Статьи добавлены!")
