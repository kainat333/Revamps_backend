from django.shortcuts import render
import json
from django.http import JsonResponse
from .models import Contact
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')
class Save_data(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            contact = Contact()
            contact.name = data.get('name')
            contact.email = data.get('email')
            contact.message = data.get('message')
            contact.save()
            return JsonResponse('success', safe=False)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400, safe=False)
        except Exception as e:
            print(e)
            return JsonResponse({'error': str(e)}, status=500, safe=False)
