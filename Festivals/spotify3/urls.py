from django.urls import path
from spotify3 import views
urlpatterns=[
    path('fest1',views.wish),
    path('fest2',views.wish2),
    path('fest3',views.wish3),
    path('fest4',views.wish4)
]