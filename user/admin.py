from django.contrib import admin
from .forms import UserCrationForm

from .models import user_profile
# Register your models here.
admin.site.register(user_profile)
