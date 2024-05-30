from msilib.schema import MoveFile
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import ReviewListSerializer, ReviewSerializer, MovieListSerializer, CommentSerializer, UserSerializer
from .models import Review, Movie, Comment
from django.contrib.auth import get_user_model



@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_like(request, movie_pk) :
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.user in movie.like_users.all():
        movie.like_users.remove(request.user)
        return Response('좋아요를 취소했습니다.', status=status.HTTP_200_OK)
    else :
        movie.like_users.add(request.user)
        return Response('좋아요 했습니다.', status=status.HTTP_200_OK)
    
    





@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def review_list(request):
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        # movie = Movie.objects.get(pk=movie_pk)
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        print(serializer.data)
        return Response(serializer.data)
    
    elif request.method == 'DELETE' :
        if review.user == request.user :
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        

@api_view(['GET'])
def find_review_user(request, review_pk) :
    review = get_object_or_404(Review, pk=review_pk)
    user_pk = review.user_id
    User = get_user_model()
    user = get_object_or_404(User, pk=user_pk)

    if request.method == 'GET' :
        serialize = UserSerializer(user)
        return Response(serialize.data)


    

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def comment_list(request):
    if request.method == 'GET':
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'DELETE'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        print(serializer.data)
        return Response(serializer.data)
    
    elif request.method == 'DELETE' :
        if comment.user == request.user :
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        

@api_view(['GET'])
def find_comment_user(request, comment_pk) :
    comment = get_object_or_404(Comment, pk=comment_pk)
    user_pk = comment.user_id
    User = get_user_model()
    user = get_object_or_404(User, pk=user_pk)

    if request.method == 'GET' :
        serialize = UserSerializer(user)
        return Response(serialize.data)
        

    


# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def article_list(request):
#     if request.method == 'GET':
#         articles = get_list_or_404(Article)
#         serializer = ArticleListSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             # serializer.save()
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET'])
# def article_detail(request, article_pk):
#     article = get_object_or_404(Article, pk=article_pk)

#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         print(serializer.data)
#         return Response(serializer.data)
    



