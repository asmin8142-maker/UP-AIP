from django.contrib.auth.models import User
from django.db.models import Avg, Count

from rest_framework import generics, status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiExample,
    OpenApiParameter,
)
from drf_spectacular.types import OpenApiTypes

from .models import Book
from .serializers import (
    BookListSerializer,
    BookDetailSerializer,
    RegisterSerializer,
)
from .permissions import IsOwner


class RegisterView(generics.CreateAPIView):
    """
    Регистрация пользователя.
    Возвращает токен.
    """

    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        token, _ = Token.objects.get_or_create(user=user)

        return Response(
            {
                "message": f"Пользователь {user.username} успешно создан",
                "token": token.key,
                "user_id": user.id,
                "username": user.username,
            },
            status=status.HTTP_201_CREATED,
        )


@extend_schema_view(
    list=extend_schema(
        summary="Список книг",
        description="Возвращает книги текущего пользователя",
        parameters=[
            OpenApiParameter(
                name="status",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description="Фильтр по статусу",
                required=False,
            )
        ],
    ),
    create=extend_schema(
        summary="Создать книгу",
        description="Добавление новой книги",
        examples=[
            OpenApiExample(
                "Пример книги",
                value={
                    "title": "Гарри Поттер",
                    "author": "Дж. К. Роулинг",
                    "status": "reading",
                    "rating": 8,
                },
                request_only=True,
            )
        ],
    ),
    retrieve=extend_schema(summary="Получить книгу"),
    update=extend_schema(summary="Обновить книгу"),
    partial_update=extend_schema(summary="Частично обновить книгу"),
    destroy=extend_schema(summary="Удалить книгу"),
)
class BookViewSet(viewsets.ModelViewSet):
    """
    CRUD для книг.
    Пользователь видит только свои книги.
    """

    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        queryset = Book.objects.filter(
            owner=self.request.user
        )

        status_filter = self.request.query_params.get("status")

        if status_filter:
            queryset = queryset.filter(status=status_filter)

        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return BookListSerializer

        return BookDetailSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @extend_schema(
        summary="Статистика чтения",
        description="Средний рейтинг и количество книг по статусам",
    )
    @action(
        detail=False,
        methods=["get"],
        url_path="reading_stats"
    )
    def reading_stats(self, request):
        books = self.get_queryset()

        status_stats = books.values(
            "status"
        ).annotate(
            count=Count("id")
        )

        avg_rating = books.aggregate(
            avg_rating=Avg("rating")
        )

        done_books = books.filter(
            status="done"
        ).count()

        return Response(
            {
                "total_books": books.count(),
                "average_rating": avg_rating["avg_rating"],
                "completed_books": done_books,
                "books_by_status": list(status_stats),
            }
        )