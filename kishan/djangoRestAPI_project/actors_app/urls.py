from .                          import views
from django.urls                import path
from django.conf                import settings
from django.conf.urls.static    import static

urlpatterns = [
    path( ''                , views.ActorsList.as_view() ),
    path( 'actor/<int:pk>'  , views.ActorByID .as_view() ),
]

if settings.DEBUG:
    urlpatterns += static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )