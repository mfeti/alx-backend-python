INSTALLED_APPS += ['rest_framework', 'rest_framework_simplejwt']

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES'] = [
    'rest_framework.permissions.IsAuthenticated',
]

REST_FRAMEWORK['DEFAULT_PAGINATION_CLASS'] = 'chats.pagination.MessagePagination'

REST_FRAMEWORK['DEFAULT_FILTER_BACKENDS'] = ['django_filters.rest_framework.DjangoFilterBackend']
