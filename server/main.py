from server.app.controllers.file import upload, generate_record
from server.app.init import app
from server.app.controllers.user import \
        register, login, email_captcha, get_record_list, \
        get_query_list, get_algorithm_list, get_user_info

app.add_url_rule(
        '/register', view_func=register, methods=['POST'])
app.add_url_rule(
        '/login', view_func=login, methods=['POST'])
app.add_url_rule(
        '/email_captcha', view_func=email_captcha, methods=['POST'])
app.add_url_rule(
        '/main/upload', view_func=upload, methods=['POST'])
app.add_url_rule(
        '/main/getRecordList', view_func=get_record_list, methods=['GET'])
app.add_url_rule(
        '/main/record/getQueryList', view_func=get_query_list, methods=['POST'])
app.add_url_rule(
        '/main/upload/genrec', view_func=generate_record, methods=['POST'])
app.add_url_rule(
        '/main/getAlgorithmList', view_func=get_algorithm_list, methods=['GET'])
app.add_url_rule(
        '/main/getUserInfo', view_func=get_user_info, methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True)
