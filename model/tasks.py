# from celery import shared_task
# from celery.loaders import app
#
#
# @shared_task
# def add(x, y):
#     return x + y
#
#
# # pv uv 统计案例
# from django.db.models import F  # 获取源数据
#
# from .models import Post
#
#
# @app.task
# def increase_pv(post_id):
#     return Post.objects.filter(id=post_id).update(pv=F('pv') + 1)