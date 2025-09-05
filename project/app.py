from flask import Flask, render_template, request, abort
from models import get_db, init_db

app = Flask(__name__)

with app.app_context():
    init_db()

@app.route("/")
def index():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, title FROM articles ORDER BY id DESC")
    articles = cur.fetchall()
    conn.close()
    return render_template("index.html", articles=articles, title="Статьи")

@app.route("/article/<int:article_id>", methods=["GET", "POST"])
def article(article_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM articles WHERE id=?", (article_id,))
    article = cur.fetchone()
    if not article:
        abort(404)

    cur.execute("SELECT * FROM tasks WHERE article_id=?", (article_id,))
    tasks = cur.fetchall()

    feedback = {}
    if request.method == "POST":
        for t in tasks:
            user_answer = request.form.get(f"task_{t['id']}", "").strip()
            if user_answer.casefold() == t["answer"].strip().casefold():
                feedback[t["id"]] = "✅ Верно!"
            else:
                feedback[t["id"]] = f"❌ Неверно. Правильный ответ: {t['answer']}"

    conn.close()
    return render_template("article.html", article=article, tasks=tasks, feedback=feedback, title=article['title'])

@app.route("/search")
def search():
    query = request.args.get("q", "").strip()
    results = []
    if query:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM articles")
        articles = cur.fetchall()
        for a in articles:
            if query.casefold() in a["title"].casefold() or query.casefold() in a["content"].casefold():
                results.append(a)
        conn.close()
    return render_template("search.html", results=results, query=query, title="Поиск")

@app.route("/achievements")
def achievements():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM achievements ORDER BY id ASC")
    items = cur.fetchall()
    conn.close()
    return render_template("achievements.html", achievements=items, title="Ачивки")

@app.route("/achievement/<int:ach_id>")
def achievement_detail(ach_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM achievements WHERE id=?", (ach_id,))
    ach = cur.fetchone()
    conn.close()
    if not ach:
        abort(404)
    return render_template("achievement.html", achievement=ach, title=ach["name"])

if __name__ == "__main__":
    app.run(debug=True)
