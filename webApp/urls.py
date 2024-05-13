from . import views
from django.urls import re_path
urlpatterns = [
    re_path(r'^submit/expense/$',views.submit_expense,name='submit-expense'),
    re_path(r'^submit/income/$',views.submit_income,name='submit-income'),
    
]
