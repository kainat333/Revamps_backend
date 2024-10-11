from django.http import JsonResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from . import models
from .models import Submission
import json


@method_decorator(csrf_exempt, name='dispatch')
class Services(View):
    # def post(self, request, *args, **kwargs):
    #     try:
    #         # Parse JSON data from request body
    #         data = json.loads(request.body)

    #         # Create a new Service object and assign the parsed data to its fields
    #         service = models.Service()

    #         # Expecting 'title' from JSON body
    #         service.title = data.get('title')
    #         # Expecting 'description' from JSON body
    #         service.description = data.get('description')

    #         # Save the object to the database
    #         service.save()

    #         # Return a success response
    #         return JsonResponse({'message': 'Service created successfully'}, status=201)

    #     except json.JSONDecodeError:
    #         # Handle JSON decoding error
    #         return JsonResponse({'error': 'Invalid JSON data'}, status=400)

    #     except Exception as e:
    #         # Handle other exceptions
    #         return JsonResponse({'error': str(e)}, status=500)

    def get(self, request, *args, **kwargs):
        service_id = kwargs.get('id')
        print(service_id)
        if service_id is not None:
            try:
                service = models.Service.objects.get(id=service_id)
                print(service)
                service_data = {
                    'id': service.id,
                    'title': service.title,
                    'description': service.description,
                }
                return JsonResponse(service_data, status=200)

            except models.Service.DoesNotExist:
                return JsonResponse({'error': 'Service not found'}, status=404)

            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)

    # def put(self, request, *args, **kwargs):
    #     try:
    #         # Parse JSON data from request body
    #         data = json.loads(request.body)

    #         # Get the service ID from the request data (assuming it's provided in the JSON)
    #         service_id = data.get('id')

    #         if not service_id:
    #             return JsonResponse({'error': 'Service ID is required for updating'}, status=400)

    #         # Fetch the existing service object from the database by ID
    #         service = models.Service.objects.get(id=service_id)

    #         # Update the service object with new data
    #         # Use existing value if not provided
    #         service.image = data.get('image', service.image)
    #         # Use existing value if not provided
    #         service.title = data.get('title', service.title)
    #         # Use existing value if not provided
    #         service.description = data.get('description', service.description)

    #         # Save the updated service to the database
    #         service.save()

    #         # Return a success response
    #         return JsonResponse({'message': 'Service updated successfully'}, status=200)

    #     except models.Service.DoesNotExist:
    #         # Handle case where the service does not exist
    #         return JsonResponse({'error': 'Service not found'}, status=404)

    #     except json.JSONDecodeError:
    #         # Handle JSON decoding error
    #         return JsonResponse({'error': 'Invalid JSON data'}, status=400)

    #     except Exception as e:
    #         # Handle other exceptions
    #         return JsonResponse({'error': str(e)}, status=500)

    # def delete(self, request, *args, **kwargs):
    #     try:
    #         # Parse JSON data from request body
    #         data = json.loads(request.body)

    #         # Get the service ID from the request data
    #         service_id = data.get('id')

    #         if not service_id:
    #             return JsonResponse({'error': 'Service ID is required for deletion'}, status=400)

    #         # Fetch the service object by ID and delete it
    #         service = models.Service.objects.get(id=service_id)
    #         service.delete()

    #         # Return a success response
    #         return JsonResponse({'message': 'Service deleted successfully'}, status=200)

    #     except models.Service.DoesNotExist:
    #         # Handle case where the service does not exist
    #         return JsonResponse({'error': 'Service not found'}, status=404)

    #     except json.JSONDecodeError:
    #         # Handle JSON decoding error
    #         return JsonResponse({'error': 'Invalid JSON data'}, status=400)

    #     except Exception as e:
    #         # Handle other exceptions
    #         return JsonResponse({'error': str(e)}, status=500)


@method_decorator(csrf_exempt, name='dispatch')
class SubmissionForm(View):
    def post(self, request):
        try:
            data = json.loads(request.body)  #
            print("Received data:", data)
           
            service_request= Submission()
            service_request.name= data['name']
            service_request.email= data['email']
            service_request.address= data['address']
            service_request.tel= data['tel']
            service_request.postcode= data['postcode']
            service_request.ServeYouWant= data['ServeYouWant']
            service_request.save()
            return JsonResponse({'id': service_request.id, 'message': 'Service request created successfully!'}, status=201)
        except KeyError as e:
            return JsonResponse({'error': f'Missing field: {str(e)}'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
