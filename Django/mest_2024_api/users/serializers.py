from rest_framework import serializers

class UserSerilizer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone_number = serializers.CharField()
    username = serializers.CharField()
    email = serializers.CharField()

class CohortSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    year = serializers.CharField()
    start_date = serializers.CharField()
    end_date = serializers.CharField()

class CohortMemberSerializer(serializers.Serializer):
    member = serializers.CharField()
    cohort = serializers.CharField()
    year = serializers.CharField()
    start_date = serializers.CharField()
    end_date = serializers.CharField()


