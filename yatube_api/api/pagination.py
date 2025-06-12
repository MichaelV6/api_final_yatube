from rest_framework.pagination import LimitOffsetPagination

class OptionalLimitOffsetPagination(LimitOffsetPagination):

    default_limit = None


    def get_default_limit(self, request):
        return None