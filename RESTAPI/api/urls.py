from django.urls import path
from . import views

urlpatterns = [
    path('blogposts', views.BlogPostListCreate.as_view(), name='blogpost-view-create'),
    path(
        'blogposts/<int:pk>/', views.BlogPostRetrieveUpdateDestroy.as_view(),
         name='update',
    ),
    path('blogposts/all/', views.BlogPostList.as_view(), name="blogpost-view-all"),
    path('blogposts/all/<int:pk>/', views.BlogPostListOne.as_view(), name="blogpost-view-one"),
]