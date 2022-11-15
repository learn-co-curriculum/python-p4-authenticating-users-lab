import flask

from app import app
app.secret_key = b'a\xdb\xd2\x13\x93\xc1\xe9\x97\xef2\xe3\x004U\xd1Z'

class TestApp:
    '''Flask API in app.py'''

    def test_show_articles_route(self):
        '''shows an article "/article/<id>".'''
        with app.app_context():
            response = app.test_client().get('/articles/1')
            response_json = response.get_json()

            assert(response_json.get('author'))
            assert(response_json.get('title'))
            assert(response_json.get('content'))
            assert(response_json.get('preview'))
            assert(response_json.get('minutes_to_read'))
            assert(response_json.get('date'))

    def test_increments_session_page_views(self):
        '''increases session['page_views'] by 1 after every viewed article.'''
        with app.test_client() as client:

            client.get('/articles/1')
            assert(flask.session.get('page_views') == 1)

            client.get('/articles/2')
            assert(flask.session.get('page_views') == 2)

            client.get('/articles/3')
            assert(flask.session.get('page_views') == 3)

            client.get('/articles/3')
            assert(flask.session.get('page_views') == 4)

    def test_limits_three_articles(self):
        '''returns a 401 with an error message after 3 viewed articles.'''
        with app.app_context():

            client = app.test_client()

            response = client.get('/articles/1')
            assert(response.status_code == 200)
            
            response = client.get('/articles/2')
            assert(response.status_code == 200)

            response = client.get('/articles/3')
            assert(response.status_code == 200)

            response = client.get('/articles/4')
            assert(response.status_code == 401)
            assert(response.get_json().get('message') == 
                'Maximum pageview limit reached')

