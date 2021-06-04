from django.urls import path
from . import views


urlpatterns = [
    path('', views.index.as_view(), name='main'),

    path('api/redirect/order', views.redirectOrder.as_view(), name='redirect-order'),
    path('api/make/order', views.order.as_view(), name='make-order'),
    path('api/question', views.question.as_view(), name='question'),

    path('order/<int:id>', views.order.as_view(), name='order'),
    path('catalog', views.catalog.as_view(), name='catalog'),
    path('about-us', views.about.as_view(), name='about-us'),
    path('question', views.question.as_view(), name='question')
]