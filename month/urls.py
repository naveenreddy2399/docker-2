from django.urls import path
from month.views import ArticleMonthArchiveView

urlpatterns = [
    # Example: /2012/08/
    path('<int:year>/<int:month>/',
         ArticleMonthArchiveView.as_view(month_format='%m'),
         name="archive_month_numeric"),
    # Example: /2012/aug/
    path('<int:year>/<str:month>/',
         ArticleMonthArchiveView.as_view(),
         name="archive_month"),
]