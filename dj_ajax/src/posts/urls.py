from django.urls import path
from .views import (
    post_line_and_create,
    load_post_data_view,
    
    hello_world_view
)

app_name = 'posts'
urlpatterns = [
    path('', post_line_and_create, name='main-board'),
    path('data/<int:num_posts>/', load_post_data_view, name='posts-data'),
    
    path('hello-world/', hello_world_view, name='hello-world'),
]