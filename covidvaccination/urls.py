from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

# imports for swagger API documentation
from vaccination_registry import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
   openapi.Info(
      title="COVID-19 Vaccination",
      default_version='v1',
      description="COVID-19 Vaccinatio",
      terms_of_service="https://myapp/policies/terms/",
      contact=openapi.Contact(email="vaccination@vaccine.local"),
      license=openapi.License(name="Test License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vaccination/', include('vaccination_registry.urls')),
    path('', include('vaccination_registry.urls')),
    path('api/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
