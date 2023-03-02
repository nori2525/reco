from django.contrib import admin
from .models import m_user
from .models import w_user
from .models import user_img

# Register your models here.
admin.site.register(m_user)
admin.site.register(w_user)
admin.site.register(user_img)