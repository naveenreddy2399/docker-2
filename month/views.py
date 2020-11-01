from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.dates import MonthArchiveView
from month.models import Article

def home(*args, **kwargs):
    return HttpResponse("<h1>Month View</h1><h3>In admin page you can add article name and choose a day from calendar..... </h3>")

class ArticleMonthArchiveView(MonthArchiveView):
    template_name="month.html"
    queryset = Article.objects.all()
    date_field = "pub_date"
    allow_future = True

