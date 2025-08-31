from flask import Flask, render_template, g
from models import get_db

app = Flask(__name__)

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'db'):
        g.db.close()

@app.route("/")
def index():
    db = get_db()
    articles = db.execute("SELECT * FROM articles").fetchall()
    return render_template("index.html", articles=articles)

@app.route("/article/<int:article_id>")
def article(article_id):
    db = get_db()
    article = db.execute("SELECT * FROM articles WHERE id=?", (article_id,)).fetchone()
    if article is None:
        return "Статья не найдена", 404
    return render_template("article.html", article=article)

if __name__ == "__main__":
    app.run(debug=True)
