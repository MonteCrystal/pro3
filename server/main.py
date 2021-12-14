from server.app.controllers.file import upload
from server.app.init import app
from server.app.controllers.user import register, login, email_captcha

app.add_url_rule(
        '/register', view_func=register, methods=['POST'])
app.add_url_rule(
        '/login', view_func=login, methods=['POST'])
app.add_url_rule(
        '/email_captcha', view_func=email_captcha, methods=['POST'])
app.add_url_rule(
        '/upload', view_func=upload, methods=['POST'])


if __name__ == '__main__':
    app.run(debug=True)
