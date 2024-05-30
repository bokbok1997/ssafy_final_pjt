from django.urls import path
from . import views


urlpatterns = [
    path('reviews/', views.review_list),
    # path('<int:movie_pk>/reviews/', views.review_list),
    path('reviews/<int:review_pk>/', views.review_detail),
    path('reviews/<int:review_pk>/find_user/', views.find_review_user),
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/likes/', views.movie_like),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('comments/<int:comment_pk>/find_user/', views.find_comment_user),
    # +) comments를 왜 review pk로 안나눴는가? << 이건 vue에서 filter를 사용하여 나눠주면 될 것 같아서

]
