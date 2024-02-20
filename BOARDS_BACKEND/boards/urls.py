from django.urls import path
from . views import * 
urlpatterns = [
    # path('',boards_list,name='home'),
    # path('<int:board_id>/', board_topics, name='topics'),
    path('', BoardsList.as_view(), name='home'),
    path('<int:board_id>/', BoardTopics.as_view(), name='topics'),
    path('board_details/<int:id>/', BoardDetails.as_view(), name='board_details'),
    # path('about/',views.about,name='about'),
    # path('boards/<int:board_id>/new/', views.new_topic, name='new_topic'),
    # path('boards/<int:board_id>/topics/<int:topic_id>/', views.topic_posts, name='topic_posts'),
    # path('boards/<int:board_id>/topics/<int:topic_id>/reply/', views.reply_for_topic, name='reply_for_topic'),
    # path('boards/<int:board_id>/topics/<int:topic_id>/post/<int:post_id>/edit/', views.PostUpdateView.as_view(), name='edit_post'),
]