from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    username    =   serializers.EmailField()
    password    =   serializers.CharField(style={'input_type': 'password'})
    nickname    =   serializers.CharField()
    name        =   serializers.CharField()
    profile     =   serializers.ImageField(allow_empty_file=True)
    birth       =   serializers.DateField()
    generation  =   serializers.ChoiceField(choices=((1, "1기"), (2, "2기")))
    interesting =   serializers.MultipleChoiceField(choices=[
        ('BACKEND', 'Backend-end'),
        ('FRONTEND', 'Front-end'),
        ('MLOPS', 'MLOps'),
        ('DS', 'Data Scientists'),
    ])
    github      =   serializers.URLField()
    blog        =   serializers.URLField()
    bio         =   serializers.CharField()

    class Meta:
        model = models.User
        fields = (
            'username',
            'password',
            'nickname',
            'name',
            'profile',
            'generation',
            'birth',
            'interesting',
            'github',
            'blog',
            'bio',
        )
    
    def create(self, validated_data):
        raise NotImplementedError('`create()` must be implemented.')