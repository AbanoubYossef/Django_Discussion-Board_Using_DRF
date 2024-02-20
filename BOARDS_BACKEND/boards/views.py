from django.shortcuts import render, get_object_or_404
# from django.http import JsonResponse
from . models import *
from django.db.models import Count
from rest_framework.views import APIView  
from rest_framework.response import Response  
from .serializers import *
from rest_framework import status, generics

# Create your views here.


# def boards_list(request):
#     boards = Board.objects.all()
#     data ={'results': list(boards.values("pk", "name", "description"))}
#     return JsonResponse(data)


# class BoardsList(APIView):
    
#     def get(self, request):
#         boards = Board.objects.all()
#         data =BoardSerializer(boards,  many=True).data
#         return Response(data)
    
#     def post(self,request):
#         serializer = BoardSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data ,status= status.HTTP_201_CREATED)
        
#         return Response(serializer.errors ,status= status.HTTP_400_BAD_REQUEST)

class BoardsList(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    
# def board_topics(request,board_id):
#     board = get_object_or_404(Board, pk=board_id)
#     topics= board.topics.order_by('created_at').annotate(comments=Count('posts'))
#     data={
#         "results":{"name":board.name, "description" :board.description},
#         "topics": list(topics.values("pk", "subject", "board", "created_by", "created_at", "updated_at"))
#     }
#     return JsonResponse(data)

# class BoardTopics(APIView):
    
#     def get(self,request,board_id):
#         board = get_object_or_404(Board, pk=board_id)
#         topics= board.topics.order_by('created_at').annotate(comments=Count('posts'))
#         data = TopicSerializer(topics, many=True).data
#         return Response(data)
    
#     def post(self, request,board_id):
#         serializer = TopicSerializer(data= request.data )
#         topic_details= request.data
#         if serializer.is_valid():
#             topic  = serializer.save()
#             post_serilizar = PostSerializer( data ={
#                 "message":topic_details['message'],
#                 "topic":topic.pk, 
#                 "created_by":topic.created_by, 
#                 "created_at":topic.created_at, 
#                 "updated_at":topic.updated_at, 
#                 })
#             if post_serilizar.is_valid():
#                 post_serilizar.save()
#             return Response(serializer.data ,status= status.HTTP_201_CREATED)
        
#         return Response(serializer.errors ,status= status.HTTP_400_BAD_REQUEST)

class BoardTopics(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

# class BoardDetails(APIView):
#     def get(self, request, board_id):
#         board = get_object_or_404(Board, pk = board_id)
#         data = BoardSerializer(board).data
#         return Response(data)


class BoardDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset =Board.objects.all()
    serializer_class = BoardSerializer
    lookup_field = 'id'