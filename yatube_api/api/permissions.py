from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Разрешение, которое позволяет только авторам объектов редактировать их.
    Анонимные пользователи могут только просматривать.
    """
    
    message = 'У вас недостаточно прав для выполнения данного действия.'

    def has_permission(self, request, view):
        # Чтение доступно всем
        if request.method in permissions.SAFE_METHODS:
            return True
        # Создание - только аутентифицированным
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Чтение доступно всем
        if request.method in permissions.SAFE_METHODS:
            return True
        # Изменение и удаление - только автору
        return obj.author == request.user