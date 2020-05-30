from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.home,name='home'),
    url(r'^search/',views.search_results,name="search_results"),
    url(r'^new/post$',views.new_post,name="new_post"),
    url(r'^new/comment$',views.new_comment,name="new_comment"),
    url(r'^profile/(\d+)',views.profile,name = 'profile'),
    url(r'^accounts/profile',views.profile,name='profile'),
    url(r'^createprofile',views.create_profile,name="create_profile")
    url(r'^logout/$', views.logout, {"next_page": '/'}), 
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)