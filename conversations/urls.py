from django.urls import path

from . import views

app_name = "conversation"

urlpatterns = [
    path("",views.inbox_messages,name="inbox"),
    path("messages/<int:pk>/",views.message_detail,name="message_detail"),
    path('new_message/<int:item_pk>/', views.new_conversation, name="new_messages"),
]
