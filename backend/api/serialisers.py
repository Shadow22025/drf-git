from rest_framework import serializers
from blog.models import Article
from django.contrib.auth.models import User

class ArticleSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = ("title","slug","author","content","publish","status")       #نام فیلد هایی که مورد استفاده هستند  
        # exclude = ("created","updated") # نام فیلد هایی که استفاده نمیکنیم
        fields = "__all__" # همه فیلد ها رو میگیرد

        

class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__" 