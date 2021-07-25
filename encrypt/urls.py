from django.urls import path
from .views import(
    home,
    encrypt,
    decrypt,
    encrypted,
    decrypted
)
app_name='encrypt'
urlpatterns = [
    path('', home, name='home'),
    path('encrypt/', encrypt, name='encrypt'),
    path('decrypt/', decrypt, name='decrypt'),
    path('encrypt/done/', encrypted, name='encrypt_done'),
    path('decrypt/done/', decrypted, name='decrypt_done'),
]