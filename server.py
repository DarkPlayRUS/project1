from flask import Flask, Response, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.get("/api/news")
def get_news():
    news = [
        {
        "name": "Поздравления",
        "description": "Всех с добрым утром!",
        "date": "2025-04-1"
        },

        {
        "name": "Сегодня интересный день",
        "description": "Сегодня, 1 апреля, учёные нашли новую солнечную систему, где есть жизнь",
        "date": "2025-04-1"
        }
    ]