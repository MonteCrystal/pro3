#
# # from server.app.app import Ping, CreateAccount, Login, UserInfo, Logout
# # from server.app.app import CreateSpiderTask, SearchSpiderTask, GetTopicDetail
# # from server.app.app import OperateLog
# # from server.app.app import RegisterServiceNode, GetAllService, DestroyService
# from server.app.views.user import CreateAccount
# from server.app.init import app
#
#
# def bind_urls(app):
#     ##########
#     # user
#     ##########
#     app.add_url_rule(
#         '/register', view_func=CreateAccount.as_view('create_account'), methods=['POST'])
#     # app.add_url_rule(
#     #     '/user/login', view_func=Login.as_view('login'), methods=['POST'])
#     # app.add_url_rule(
#     #     '/user/logout', view_func=Logout.as_view('logout'), methods=['POST'])
#     # app.add_url_rule(
#     #     '/user/info', view_func=UserInfo.as_view('get_user_info'), methods=['GET'])
#     # app.add_url_rule(
#     #     '/user/logout', view_func=UserInfo.as_view('log_out'), methods=['POST'])
#
#
