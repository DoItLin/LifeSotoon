from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.utils import timezone
from models import User, out_comes ,in_comes# Ensure these models are imported correctly

@csrf_exempt 
def submit_expense(request):
    """User submits an expense."""
    if request.method == 'POST':
        try:
            this_token = request.POST['token']
            this_user = User.objects.filter(token__token=this_token).get()
            now = timezone.now()  #TODO Use timezone.now() for better time handling
            out_comes.objects.create(user=this_user, amount=request.POST['amount'], text=request.POST['text'], date=now)
            return JsonResponse({
                'status': 'ok',
                'message': 'Data registered successfully.'
            }, encoder=JSONEncoder)
        except User.DoesNotExist:
            return JsonResponse({
                'status': 'error',
                'message': 'User not found.'
            }, encoder=JSONEncoder)
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, encoder=JSONEncoder)
    else:
        # If the request method is not POST, you might want to return an error or a different response
        return HttpResponse("Invalid request method.", status=400)



"""TODO it's for income fucntion """
@csrf_exempt 
def submit_income(request):
    """User submits an income."""
    if request.method == 'POST':
        try:
            this_token = request.POST['token']
            this_user = User.objects.filter(token__token=this_token).get()
            now = timezone.now()
            in_comes.objects.create(user=this_user, amount=request.POST['amount'], text=request.POST['text'], date=now)
            return JsonResponse({
                'status': 'ok',
                'message': 'Income registered successfully.'
            })
        except User.DoesNotExist:
            return JsonResponse({
                'status': 'error',
                'message': 'User not found.'
            })
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            })
    else:
        # If the request method is not POST, you might want to return an error or a different response
        return HttpResponse("Invalid request method.", status=400)
