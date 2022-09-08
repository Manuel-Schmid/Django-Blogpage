from django.contrib import admin
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from . import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from blog.schema import schema
from graphql_jwt.decorators import jwt_cookie


urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path("graphql/",
         jwt_cookie(
             csrf_exempt(
                 GraphQLView.as_view(graphiql=True, schema=schema)
             )
         )
    ),  # todo: anschauen mit Stefan
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
