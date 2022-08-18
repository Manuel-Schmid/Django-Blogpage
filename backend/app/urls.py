from django.contrib import admin
from django.urls import include, path
from . import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from graphene_file_upload.django import FileUploadGraphQLView
from blog.schema import schema


urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    # path("graphql/", GraphQLView.as_view(graphiql=True, schema=schema)),
    path("graphql/", FileUploadGraphQLView.as_view(graphiql=True, schema=schema)),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
