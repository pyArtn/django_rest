import requests

from conf_file import *


class Telegram:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        if request.user.is_authenticated:
            try:
                username = request.user.username
                method = request.method
                response = requests.post(url=url,
                                         data={'chat_id': chat_id, 'text': text.format(username, method)})
                print(response.status_code)
                # print(response.url)
                # print(response.request)
            except Exception as ex:
                print(f"error in send_message: {ex}")
