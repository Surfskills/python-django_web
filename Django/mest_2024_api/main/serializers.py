#create serializers for all models in main
from rest_framework import serializers

class CourseSerializer(serializers.Serializer):
    name = serializers.CharField()

class ClassSerializers(serializers.Serializer):   
    tittle = serializers.CharField()
    description = serializers.CharField()
    start_date_and_time = serializers.CharField()
    end_date_and_time = serializers.CharField()
    organizer = serializers.CharField()
    venue = serializers.CharField()

class ClassAttendanceSerializers(serializers.Serializer ):
    attendee = serializers.CharField()
    start_date_and_time = serializers.CharField()
    end_date_and_time = serializers.CharField()

class QuerySerializer(serializers.Serializer):
    tittle = serializers.CharField()
    description = serializers.CharField()
    submitted_by = serializers.CharField()
    status = serializers.CharField()
    date_created = serializers.CharField()

class QueryCommentserializer(serializers.Serializer):
    comment = serializers.CharField()
    date_created = serializers.CharField()
   

