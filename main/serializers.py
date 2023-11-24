from rest_framework import serializers
from main.models import Book_Entry, Book, Custom_Entry, Catalog_Entry
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)


class BookSerializer(TaggitSerializer, serializers.ModelSerializer):
    taggits = TagListSerializerField()

    class Meta:
        model = Book
        fields = "__all__"

class CustomSerializer(TaggitSerializer, serializers.ModelSerializer):
    taggits = TagListSerializerField()
    class Meta:
        model = Custom_Entry
        fields = "__all__"

class Catalog_EntrySerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Catalog_Entry
        fields = ['book', ]

class Book_EntrySerializer(serializers.ModelSerializer):
    catalog_entry = Catalog_EntrySerializer(read_only=True)
    custom_entry = CustomSerializer(read_only=True)
        
    class Meta:
        model = Book_Entry
        fields = ['status', 'last_chapter_read', 'catalog_entry', 'last_read_date', 'custom_entry', 'review', 'rating', 'pk', 'notes']
        
class BookPostSerializer(TaggitSerializer, serializers.ModelSerializer):
    taggits = TagListSerializerField()

    class Meta:
        model = Book
        fields = "__all__"

