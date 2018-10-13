from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^coupons/$', views.CouponList.as_view()),
    url(r'^coupons/(?P<name>.*)/$', views.CouponDetail.as_view()),
]