from django.contrib import admin
from .models import   out_comes
from .models import in_comes
from .models import Token 

# Register your models here.

admin.site.register(out_comes)
admin.site.register(in_comes)
admin.site.register(Token)

