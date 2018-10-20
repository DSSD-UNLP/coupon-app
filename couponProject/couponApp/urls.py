from django.conf.urls        import url, include
from .                       import views
from django.conf             import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^coupons/$',              views.CouponCreate.as_view()),
    url(r'^coupons/(?P<name>.*)/$', views.CouponDetail.as_view()),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)