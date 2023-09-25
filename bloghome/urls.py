from django.urls import path
from bloghome import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.landing_page, name='home'),
    path("viewpost_1", views.page_1, name='blogpage1'),
    path("viewpost_2", views.page_2, name='blogpage2'),
    path("viewpost_3", views.page_3, name='blogpage3'),
    path("viewpost_4", views.page_4, name='blogpage4'),
    path("viewpost_5", views.page_5, name='blogpage5'),
    path("viewpost_6", views.page_6, name='blogpage6'),
    path("viewpost_7", views.page_7, name='blogpage7'),
    path("viewpost_8", views.page_8, name="blogpage8"),
    path("viewpost_9", views.page_9, name="blogpage9"),
    path('update', views.blogPostUpdate, name='update'),
    path('success_upld', views.success_upld, name='success_upld'),
    path('delete/<id>', views.delete_view, name='delete_view'),
    path('success_dlt', views.success_dlt, name='success_dlt')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATICFILES_DIRS)
