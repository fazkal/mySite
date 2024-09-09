from django.contrib.sitemaps import Sitemap
from blog.models import Post1

class blogSitemap(Sitemap):
    changeferq="weekly"
    priority=0.5

    def items(self):
        return Post1.objects.filter(status=True)

    def lastmod(self,obj):
        return obj.published_date