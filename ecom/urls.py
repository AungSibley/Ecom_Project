from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('Ecom_Login.urls')),
    path('', include('Ecom_Shop.urls')),
    path('shop/', include('Ecom_Order.urls')),
    path('payment/', include('Ecom_Payment.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


