from calendar import c
from django.shortcuts import render

# restAPI for Django 
from rest_framework.response import Response
from rest_framework.views import APIView
# Models, Serializer for Dajngo orm 
from .models import Content
from users.models import User
from .serializers import contentSerializer
## for create user uuid to test insert DB
import uuid

class boardsAPI(APIView):
    get_cnt = 0

    def get(self, request):
        ## request가 많이 왔을 때, 한번에 처리 하는 방법?? 
        ## 동민이 형은 어떻게 처리 하는 지?
        # insert content for Test
        # user = User()
        # user.save()

        new_content = Content()
        new_content.title = f"Content {self.get_cnt}"
        new_content.content = " "

        # new_content.user_name = user
        new_content.save()

        ## read contests List 
        contents = Content.objects.all()
        print(contents)

        serializer = contentSerializer(contents, many=True)
        print(serializer)
        return Response(serializer.data)

    def post(self, request):
        pass