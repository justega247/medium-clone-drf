from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import Article, Author
from .serializers import ArticleSerializer


# Create your views here.
# Using APIView
# class ArticleView(APIView):
#     def get(self, request):
#         articles = Article.objects.all()
#         # the many param informs the serializer that it will be serializing more than a single article.
#         serializer = ArticleSerializer(articles, many=True)
#         return Response({
#             "articles": serializer.data
#         })
#
#     def post(self, request):
#         article = request.data.get('article')
#         # Create an article from the above data
#         serializer = ArticleSerializer(data=article)
#         if serializer.is_valid(raise_exception=True):
#             article_saved = serializer.save()
#         return Response({
#             "success": f"Article {article_saved.title} created successfully"
#         })
#
#     def put(self, request, pk):
#         saved_article = get_object_or_404(Article.objects.all(), pk=pk)
#         data = request.data.get('article')
#         serializer = ArticleSerializer(instance=saved_article, data=data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             article_saved = serializer.save()
#         return Response({
#             "success": f"Article {article_saved.title} updated successfully"
#         })
#
#     def delete(self, request, pk):
#         # Get object with this pk
#         article = get_object_or_404(Article.objects.all(), pk=pk)
#         article.delete()
#         return Response({
#             "message": f"Article with id {pk} has been deleted."
#         }, status=204)


# Using GenericAPIView
# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import (
#     ListModelMixin,
#     CreateModelMixin,)
#
#
# class ArticleView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
#     def perform_create(self, serializer):
#         author = get_object_or_404(Author, id=self.request.data.get('author_id'))
#         return serializer.save(author=author)
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# CreateAPIView extends from the CreateModelMixin that we were extending above and
# defines a post method for us. We can, therefore, extend CreateAPIView and forget
# about writing the post method ourselves. The same applies to the get method.
# We can just extend ListAPIView and forget about writing the get method.

# from rest_framework.generics import CreateAPIView, ListAPIView


# class ArticleView(CreateAPIView, ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
#     def perform_create(self, serializer):
#         author = get_object_or_404(Author, id=self.request.data.get('author_id'))
#         return serializer.save(author=author)


# Even further, we can use a special GenericView and combine both creating an article and
# listing an article. We will use ListCreateAPIView . For this, we will need to update our code to the following.

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class ArticleView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        author = get_object_or_404(Author, id=self.request.data.get('author_id'))
        return serializer.save(author=author)


class SingleArticleView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
