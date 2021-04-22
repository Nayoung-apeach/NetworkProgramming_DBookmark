from django.urls import path

from bookmark.views import BookmarkListView, BookmarkCreateView

app_name = 'bookmark'


urlpatterns = {
    path('', BookmarkListView.as_view(), name='list'),  # {% url 'bookmark:list' %}
    path('add/', BookmarkCreateView.as_view(), name='add'), #{% url 'bookmark:add' %}
}
