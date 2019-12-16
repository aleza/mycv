from django.urls import path

from . import views


app_name = 'cv'

urlpatterns = [
	# ex: /cv/
    path('', views.index, name='index'),
        
    path('resume/', views.detail_r, name='detail_r'),

    path('education/<int:person_id>/', views.detail_e, name='detail_e'),

    path('data/<int:person_id>/', views.detail_d, name='detail_d'),

    path('hobbies/<int:person_id>/', views.detail_h, name='detail_h'),

    path('courses/<int:person_id>/', views.detail_c, name='detail_c'),

]