from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book


class BookListSerializer(serializers.ModelSerializer):
    """
    Краткий сериализатор для списка книг.
    """

    owner_username = serializers.CharField(
        source='owner.username',
        read_only=True
    )

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'author',
            'status',
            'rating',
            'owner_username'
        ]

        read_only_fields = [
            'id',
            'owner_username'
        ]


class BookDetailSerializer(serializers.ModelSerializer):
    """
    Полный сериализатор книги.
    """

    owner_username = serializers.CharField(
        source='owner.username',
        read_only=True
    )

    class Meta:
        model = Book
        fields = '__all__'

        read_only_fields = [
            'id',
            'owner',
            'created_at',
            'owner_username'
        ]

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                'Название книги не может быть пустым.'
            )
        return value.strip()

    def validate_rating(self, value):
        if value < 0 or value > 10:
            raise serializers.ValidationError(
                'Оценка должна быть от 0 до 10.'
            )
        return value


class RegisterSerializer(serializers.ModelSerializer):
    """
    Регистрация нового пользователя.
    """

    password = serializers.CharField(
        write_only=True,
        min_length=8
    )

    password2 = serializers.CharField(
        write_only=True
    )

    class Meta:
        model = User

        fields = [
            'username',
            'email',
            'password',
            'password2'
        ]

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({
                'password': 'Пароли не совпадают.'
            })

        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )

        return user