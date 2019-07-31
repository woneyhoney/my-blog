from django.contrib import admin
from django.urls import path, include
import blog.views
import portfolio.views

# Media 파일 다룰려면 2줄 추가해야됨
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"),
    path('blog/', include('blog.urls')),
    path('portfolio/', portfolio.views.portfolio, name="portfolio"),
    path('account/', include('account.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

