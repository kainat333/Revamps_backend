# cars/views.py
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from . import models
import json


@method_decorator(csrf_exempt, name='dispatch')
class Purchase(View):
    def post(self, request):
        try:
            data = json.loads(request.body)  #
            print("Received data:", data)
            Purchase = models.Purchase.objects.create(
                name=data.get['name'],
                email=data.get['email'],
                address=data.get['address'],
                # Use empty string if location not provided
                phone=data.get('phone'),
                payment_method=data.get('payment_method'),  # Can be None if not provided
                price=data.get['price'],
                car_type=data.get['car_type'],
                car_id=data.get['car_id'],
            )
            print(
                'purchase',Purchase
            )

            return JsonResponse({'id': Purchase.id, 'message': 'Service request created successfully!'}, status=201)
        except KeyError as e:
            return JsonResponse({'error': f'Missing field: {str(e)}'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
