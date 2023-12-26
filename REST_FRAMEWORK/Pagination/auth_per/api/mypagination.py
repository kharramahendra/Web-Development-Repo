from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination


class MyPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'p' # ?page=4 --> ?p=4
    page_size_query_param = 'records' # user can set any number of records per page
    max_page_size = 7 # now user can not misuse of dynamic pagination
    last_page_strings = 'end'

class MyCursorPagination(CursorPagination):
    page_size = 5
    ordering = 'name'

class MyLimitPagination(LimitOffsetPagination):
    pass