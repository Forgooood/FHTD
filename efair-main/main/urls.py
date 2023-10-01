from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', homeView, name='home_url'),
    path('signup', signupView, name='signup_url'),
    path('cabinet', cabinetView, name='cabinet_url'),
    path('login', loginView, name='login_url'),
    path('logout', logoutView, name='logout_url'),
    path('edit_profile', editProfileView, name='edit_profile_url'),
    path('offers/', offersView, name='offers_url'),
    path('offers/<int:category_id>', offersView, name='offers_url'),
    path('offer/<int:offer_id>', offerDetailView, name='offer_url'),
    path('create_offer', createOfferView, name='offer_create_url'),
    path('edit_offer/<int:offer_id>', editOfferView, name='offer_edit_url'),
    path('delete_offer/<int:offer_id>', deleteOfferView, name='offer_delete_url'),
    path('create_offer_buy/<int:offer_id>', createOfferBuyView, name='create_offer_buy_url'),
    path('offers_buy/<int:offer_id>', offerBuyView, name='offers_buy_url'),
    path('offer_decline', offerDecline, name='offers_decline_url'),
    path('offer_accept', offerAccept, name='offers_accept_url'),
    path('news/<int:news_id>', newsDetailView, name='news_url'),
    path('delete_user/<int:user_id>', deleteCustomUserView, name='user_delete_url'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)