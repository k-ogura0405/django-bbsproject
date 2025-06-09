"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
# カスタム403エラー処理を行う関数をインポート
from bbs.views import custom_permission_denied_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bbs/', include('bbs.urls')),
    path('', RedirectView.as_view(url='/bbs/')),
    path('accounts/', include('django.contrib.auth.urls')),
]

# カスタム403エラーハンドラの設定
handler403 = 'bbs.views.custom_permission_denied_view'