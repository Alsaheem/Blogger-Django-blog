from django.urls import path
from blog import views
from django.conf.urls import url
app_name ='blog'

urlpatterns = [
    path('', views.PostListView.as_view() , name='home'),
    path('user/<str:username>', views.UserPostListView.as_view(), name='user_posts'), 
    path('post/<int:pk>/', views.PostDetailView.as_view() , name='post_detail'),
    path('post/<int:pk>/update', views.UpdatePostView.as_view() , name='post_update'),
    path('post/<int:pk>/delete', views.DeletePostView.as_view() , name='post_delete'),
    path('post/new/', views.CreatePostView.as_view() , name='post_new'),
    path('about/', views.AboutView.as_view() , name='about')

]
