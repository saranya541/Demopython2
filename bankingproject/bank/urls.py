
from django.urls import path
from .import views
app_name='bank'
urlpatterns = [
    path('',views.alldiscat,name='alldiscat'),
    path('<slug:c_slug>/', views.alldiscat,name='district_by_branch'),
    path('<slug:c_slug>/<slug:district_slug>/', views.pdtdetail,name='disbradetail')

]
