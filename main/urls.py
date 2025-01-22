from django.urls import path
from . import views
from .views import download_resume
from .views import footer_view

app_name='main'

urlpatterns = [
    path('',views.IndexView.as_view(),name='home'),
    path('contact/',views.ContactView.as_view(), name='contact'),
    path('portfolio/',views.PortfolioView.as_view(), name='portfolios'),
    path('portfolio/<slug:slug>',views.PortfolioDetailView.as_view(),name='portfolio'),
    path('blog/',views.BlogView.as_view(),name='blogs'),
    path('blog/<slug:slug>',views.BlogDetailView.as_view(),name='blog'),
    path('download/<int:user_id>/', views.download_resume, name='download_resume'),
    path('footer/', footer_view, name='footer'),

]

