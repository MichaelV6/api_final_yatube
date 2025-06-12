# api/exceptions.py
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

def custom_exception_handler(exc, context):
    # 1. Ловим InvalidToken / TokenError и формируем «правильный» ответ
    if isinstance(exc, (InvalidToken, TokenError)):
        return Response(
            {
                "detail": "Token is invalid or expired",
                "code": "token_not_valid",
            },
            status=status.HTTP_401_UNAUTHORIZED,
        )

    # 2. Всё остальное отдаём стандартному DRF-обработчику
    return exception_handler(exc, context)
