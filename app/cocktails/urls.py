from django.urls import path
from cocktails import views as cocktails_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', cocktails_views.index.as_view(), name='home'),
    path('api/cocktails/', cocktails_views.cocktails_list),
    path('api/cocktails/<int:pk>/', cocktails_views.cocktails_detail),
    path('api/cocktails/published/', cocktails_views.cocktails_list_published)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
