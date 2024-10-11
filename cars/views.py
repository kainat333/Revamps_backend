from django.http import JsonResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from . import models
import json

@method_decorator(csrf_exempt, name='dispatch')
class fetch_specific_cars(View):
    def get(self, request, *args, **kwargs):
        car_id = kwargs.get('id')
        if car_id is not None:
            try:
                newcar = models.NewCar.objects.get(id=car_id)
                newcar_data = {
                    'id': newcar.id,
                    'make': newcar.make,
                    'model': newcar.model,
                    'year': newcar.year,
                    'price': newcar.price,
                    'location': newcar.location,
                    'image': newcar.image,
                    'kilometers': newcar.kilometers,
                    'fuelType': newcar.fuelType,
                    'transmission': newcar.transmission,
                    'bodyType': newcar.bodyType,
                    'color': newcar.color,
                    'engineCapacity': newcar.engineCapacity,
                    'registeredIn': newcar.registeredIn
                }
                return JsonResponse(newcar_data, status=200)

            except models.NewCar.DoesNotExist:
                return JsonResponse({'error': 'Car not found'}, status=404)

            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({'error': 'No car ID provided'}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class Cars(View):
    def post(self, request, *args, **kwargs):
        try: 
            # Parse JSON data from request body
            data = json.loads(request.body)

            # Create a new NewCar object and assign the parsed data to its fields
            myObject = models.NewCar()
            myObject.make = data.get('make')
            myObject.model = data.get('model')
            myObject.year = data.get('year')
            myObject.price = data.get('price')
            myObject.location = data.get('location')
            myObject.image = data.get('image')
            myObject.kilometers = data.get('kilometers')
            myObject.fuelType = data.get('fuelType')
            myObject.transmission = data.get('transmission')
            myObject.bodyType = data.get('bodyType')
            myObject.color = data.get('color')
            myObject.engineCapacity = data.get('engineCapacity')
            myObject.registeredIn = data.get('registeredIn')

            # Save the object to the database
            myObject.save()

            # Return a success response
            return JsonResponse({'message': 'success'}, safe=False)

        except json.JSONDecodeError:
            # Handle JSON decoding error
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        except Exception as e:
            # Handle other exceptions
            return JsonResponse({'error': str(e)}, status=500)

    def get(self, request, *args, **kwargs):
        try:
        # Fetch all car records from the NewCar model
            cars = models.NewCar.objects.filter(is_active=True)

        # Serialize the data into a list of dictionaries
            car_list = list(cars.values())

        # Return the serialized data as a JSON response
            return JsonResponse( car_list, safe=False)

        except Exception as e:
        # Handle any exceptions and return an error response
            return JsonResponse({'error': str(e)}, status=500)
    def put(self, request, *args, **kwargs):
        try:
            # Parse JSON data from request body
            data = json.loads(request.body)

            # Get the car ID from the data (you can also get it from the URL kwargs if preferred)
            car_id = data.get('id')

            if not car_id:
                return JsonResponse({'error': 'Car ID is required for updating'}, status=400)

            # Fetch the existing car object from the database by ID
            myObject = models.NewCar.objects.get(id=car_id)

            # Update the fields with the provided data
            myObject.make = data.get('make', myObject.make)
            myObject.model = data.get('model', myObject.model)
            myObject.year = data.get('year', myObject.year)
            myObject.price = data.get('price', myObject.price)
            myObject.location = data.get('location', myObject.location)
            myObject.image = data.get('image', myObject.image)
            myObject.kilometers = data.get('kilometers', myObject.kilometers)
            myObject.fuelType = data.get('fuelType', myObject.fuelType)
            myObject.transmission = data.get('transmission', myObject.transmission)
            myObject.bodyType = data.get('bodyType', myObject.bodyType)
            myObject.color = data.get('color', myObject.color)
            myObject.engineCapacity = data.get('engineCapacity', myObject.engineCapacity)
            myObject.registeredIn = data.get('registeredIn', myObject.registeredIn)

            # Save the updated object to the database
            myObject.save()

            # Return a success response
            return JsonResponse({'message': 'Car updated successfully'}, safe=False)

        except models.NewCar.DoesNotExist:
            # Handle case where the car does not exist
            return JsonResponse({'error': 'Car not found'}, status=404)

        except json.JSONDecodeError:
            # Handle JSON decoding error
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        except Exception as e:
            # Handle other exceptions
            return JsonResponse({'error': str(e)}, status=500)
# Used car function
@method_decorator(csrf_exempt, name='dispatch')
class Usedcars(View):
    def post(self, request, *args, **kwargs):
        try:
            # Parse JSON data from request body
            data = json.loads(request.body)

            # Create a new NewCar object and assign the parsed data to its fields
            myObject = models.UsedCar()
            myObject.make = data.get('make')
            myObject.model = data.get('model')
            myObject.year = data.get('year')
            myObject.price = data.get('price')
            myObject.location = data.get('location')
            myObject.image = data.get('image')
            myObject.kilometers = data.get('kilometers')
            myObject.fuelType = data.get('fuelType')
            myObject.transmission = data.get('transmission')
            myObject.bodyType = data.get('bodyType')
            myObject.color = data.get('color')
            myObject.engineCapacity = data.get('engineCapacity')
            myObject.registeredIn = data.get('registeredIn')

            # Save the object to the database
            myObject.save()

            # Return a success response
            return JsonResponse({'message': 'success'}, safe=False)

        except json.JSONDecodeError:
            # Handle JSON decoding error
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        except Exception as e:
            # Handle other exceptions
            return JsonResponse({'error': str(e)}, status=500)

    def get(self, request, *args, **kwargs):
        try:
        # Fetch all car records from the NewCar model
            cars = models.UsedCar.objects.filter(is_active=True)

        # Serialize the data into a list of dictionaries
            car_list = list(cars.values())

        # Return the serialized data as a JSON response
            return JsonResponse( car_list, safe=False)

        except Exception as e:
        # Handle any exceptions and return an error response
            return JsonResponse({'error': str(e)}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class fetch_specific_used_cars(View):
    def get(self, request, *args, **kwargs):
        car_id = kwargs.get('id')
        if car_id is not None:
            try:
                usedcar = models.UsedCar.objects.get(id=car_id)
                usedcar_data = {
                    'id': usedcar.id,
                    'make': usedcar.make,
                    'model': usedcar.model,
                    'year': usedcar.year,
                    'price': usedcar.price,
                    'location': usedcar.location,
                    'image': usedcar.image,
                    'kilometers': usedcar.kilometers,
                    'fuelType': usedcar.fuelType,
                    'transmission': usedcar.transmission,
                    'bodyType': usedcar.bodyType,
                    'color': usedcar.color,
                    'engineCapacity': usedcar.engineCapacity,
                    'registeredIn': usedcar.registeredIn
                }
                return JsonResponse(usedcar_data, status=200)

            except models.NewCar.DoesNotExist:
                return JsonResponse({'error': 'Car not found'}, status=404)

            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({'error': 'No car ID provided'}, status=400)
