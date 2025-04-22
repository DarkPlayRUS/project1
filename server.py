from flask import Flask, Response, json
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app, resources={r"/api/news*": {"origins":"*"}})

@app.get("/")
def get_news():
    news = [
        {
        "id": "1",
        "name": "Поздравления",
        "description": "Всех с добрым утром!",
        "date": "2025-04-1"
        },

        {
        "id": "2",
        "name": "Сегодня интересный день",
        "description": "Сегодня, 1 апреля, учёные нашли новую солнечную систему, где есть жизнь",
        "date": "2025-04-1"
        }
    ]
    return Response(json.dumps(news), content_type="application/json")
def main():
    app.run("localhost", 8000, True)

if __name__ == "__main__":
    main()
