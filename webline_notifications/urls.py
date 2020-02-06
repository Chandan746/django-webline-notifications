from django.conf.urls import url
from . import views
app_name = 'webline_notifications'
urlpatterns = [
    url(r'^see-all/$',
        views.see_all_notification, name='see_all_notification'),
]
