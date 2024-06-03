# urls.py
from django.urls import path, include
from rest import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import BannerViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="aifans",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

router = DefaultRouter()
router.register(r'banners', BannerViewSet)

urlpatterns = [
    path("", views.home),
    path('banners/', views.banners_list, name='banners'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Include the router URLs here
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
