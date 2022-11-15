#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, session
from flask_migrate import Migrate

from models import db, Article, User

app = Flask(__name__)
app.secret_key = b'Y\xf1Xz\x00\xad|eQ\x80t \xca\x1a\x10K'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/clear')
def clear_session():
    session['page_views'] = 0

    return make_response(
        jsonify({
            'message': '200: Successfully cleared session data.'
        }),
        200
    )

@app.route('/articles')
def index_articles():
    articles = [article.to_dict() for article in Article.query.all()]
    return make_response(jsonify(articles), 200)

@app.route('/articles/<int:id>')
def show_article(id):

    session['page_views'] = 0 if not session.get('page_views') else session.get('page_views')
    session['page_views'] += 1

    if session['page_views'] <= 3:

        article = Article.query.filter(Article.id == id).first()
        article_json = jsonify(article.to_dict())

        return make_response(article_json, 200)

    else:
        return make_response(
            jsonify({
                'message': 'Maximum pageview limit reached'
            }),
            401
        )

if __name__ == '__main__':
    app.run(port=5555)
