from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Post

class LatestEntriesFeed(Feed):
    title = "my first blog"
    link = "/rss/feed"
    description = "the best blog ever"

    def items(self):
        return Post.objects.filter(status=True)

    def item_title(self, item):
        return item.title

    def item_content(self, item):
        return item.content
