import json
import logging
import random

from django.http import JsonResponse
from django.shortcuts import render
# from wxcloudrun.models import Counters
from wxcloudrun.models import Rolls

logger = logging.getLogger('log')


def index(request, _):
    """
    获取主页

     `` request `` 请求对象
    """

    return render(request, 'index.html')


# def counter(request, _):
#     """
#     获取当前计数
#
#      `` request `` 请求对象
#     """
#
#     rsp = JsonResponse({'code': 0, 'errorMsg': ''}, json_dumps_params={'ensure_ascii': False})
#     if request.method == 'GET' or request.method == 'get':
#         rsp = get_count()
#     elif request.method == 'POST' or request.method == 'post':
#         rsp = update_count(request)
#     else:
#         rsp = JsonResponse({'code': -1, 'errorMsg': '请求方式错误'},
#                            json_dumps_params={'ensure_ascii': False})
#     logger.info('response result: {}'.format(rsp.content.decode('utf-8')))
#     return rsp
#
#
# def get_count():
#     """
#     获取当前计数
#     """
#
#     try:
#         data = Counters.objects.get(id=1)
#     except Counters.DoesNotExist:
#         return JsonResponse({'code': 0, 'data': 0},
#                             json_dumps_params={'ensure_ascii': False})
#     return JsonResponse({'code': 0, 'data': data.count},
#                         json_dumps_params={'ensure_ascii': False})
#
#
# def update_count(request):
#     """
#     更新计数，自增或者清零
#
#     `` request `` 请求对象
#     """
#
#     logger.info('update_count req: {}'.format(request.body))
#
#     body_unicode = request.body.decode('utf-8')
#     body = json.loads(body_unicode)
#
#     if 'action' not in body:
#         return JsonResponse({'code': -1, 'errorMsg': '缺少action参数'},
#                             json_dumps_params={'ensure_ascii': False})
#
#     if body['action'] == 'inc':
#         try:
#             data = Counters.objects.get(id=1)
#         except Counters.DoesNotExist:
#             data = Counters()
#         data.id = 1
#         data.count += 1
#         data.save()
#         return JsonResponse({'code': 0, "data": data.count},
#                             json_dumps_params={'ensure_ascii': False})
#     elif body['action'] == 'clear':
#         try:
#             data = Counters.objects.get(id=1)
#             data.delete()
#         except Counters.DoesNotExist:
#             logger.info('record not exist')
#         return JsonResponse({'code': 0, 'data': 0},
#                             json_dumps_params={'ensure_ascii': False})
#     else:
#         return JsonResponse({'code': -1, 'errorMsg': 'action参数错误'},
#                             json_dumps_params={'ensure_ascii': False})


def roll(request, _):
    """
    获取随机折扣

     `` request `` 请求对象
    """

    rsp = JsonResponse({'code': 0, 'errorMsg': ''}, json_dumps_params={'ensure_ascii': False})
    if request.method == 'GET' or request.method == 'get':
        rsp = get_roll()
    else:
        rsp = JsonResponse({'code': -1, 'errorMsg': '请求方式错误'},
                           json_dumps_params={'ensure_ascii': False})
    logger.info('response result: {}'.format(rsp.content.decode('utf-8')))
    return rsp


def get_roll():
    """
    生成随机折扣并保存到数据库
    """

    # Generate a random discount between 0 and 10
    random_discount = random.randint(0, 10)

    # Create a new Rolls record with the random discount
    roll = Rolls(discount=random_discount)
    roll.save()

    return JsonResponse({'code': 0, 'data': roll.discount},
                        json_dumps_params={'ensure_ascii': False})
