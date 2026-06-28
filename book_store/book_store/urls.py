from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    # Without this, /admin (no trailing slash) is caught by book_outlet's
    # <slug:slug> pattern and Django tries to find a Book with slug "admin".
    path("admin", RedirectView.as_view(url="/admin/", permanent=False)),
    path("", include("book_outlet.urls")),
]
