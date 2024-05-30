from django.db import models
from django.conf import settings
# from django.contrib.postgres.fields import ArrayField


# 영화 정보를 넣은 모델
# 유저와 N:M 관계를 가지고 있음 (0명 이상의 유저는 0개 이상의 영화에 좋아요를 누를 수 있다.)
class Movie(models.Model) :
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    movie_id = models.IntegerField()
    genre_ids = models.IntegerField(null=True)
    adult = models.BooleanField(default=False)
    backdrop_path = models.TextField(null=True)
    original_language = models.TextField()
    original_title = models.TextField()
    overview = models.TextField()
    popularity = models.FloatField()
    poster_path = models.TextField(null=True)
    release_date = models.TextField()
    title = models.TextField()
    video = models.BooleanField(default=False)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()


# 리뷰를 넣은 모델 (유저와 영화와 1:N 관계)
class Review(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# 리뷰에 달릴 댓글을 넣을 모델 (유저 및 리뷰와 1:N 관계)
# 영화를 뺀 이유 : 이미 리뷰가 영화랑 1:N 관계이기 때문에 리뷰와 연결되어있으니 굳이 필요없음
class Comment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

