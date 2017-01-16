from django.conf.urls import url, include
from django.contrib import admin
from .api import views

urlpatterns = [
    # url(r'^locations$', views.UserListView.as_view(), name='user_list_view'),
    url(r'^rating/user/(?P<pk>[0-9]+)/$', views.UserRatingeDetail.as_view(), name='user_rating'),
    url(r'^view/user/(?P<pk>[0-9]+)/$', views.UserProfileView.as_view(), name='user_profile_view'),
    url(r'^match/$', views.UserMatchView.as_view(), name='user_match'),
    url(r'^currency/$', views.VirtualCurrencyView.as_view(), name='virtual_currency'),
    url(r'^gifts/$', views.UserGiftView.as_view(), name='user_gifts'),
    url(r'^gifts/send/$', views.GiftSendView.as_view(), name='gift_send'),

    url(r'^cards/$', views.CardView.as_view(), name='cards'),
]