from django.http import JsonResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from . import models
import json
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password


@method_decorator(csrf_exempt, name='dispatch')
class Users(View):
    def post(self, request, *args, **kwargs):
        try:
            # Parse JSON data from request body
            data = json.loads(request.body)

            # Create a new User object and assign the parsed data to its fields
            user = models.User()
            user.username = data.get('username')
            user.email = data.get('email')
            # Assuming password is hashed before storing
            user.password = make_password(data.get('password'))

            # Save the user object to the database
            user.save()

            # Return a success response
            return JsonResponse({'message': 'User created successfully'}, safe=False)

        except json.JSONDecodeError:
            # Handle JSON decoding error
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        except Exception as e:
            # Handle other exceptions
            return JsonResponse({'error': str(e)}, status=500)

    def put(self, request, *args, **kwargs):
        try:
            # Parse JSON data from request body
            data = json.loads(request.body)

            # Get the user ID from the data (you can also get it from the URL kwargs if preferred)
            user_id = data.get('id')

            if not user_id:
                return JsonResponse({'error': 'User ID is required for updating'}, status=400)

            # Fetch the existing user object from the database by ID
            user = models.User.objects.get(id=user_id)

            # Update the fields with the provided data
            user.username = data.get('username', user.username)
            user.email = data.get('email', user.email)
          # Check if a new password is provided
            new_password = data.get('password')
            if new_password:
                # Hash the new password before saving
                user.password = make_password(new_password)

            # Save the updated user object to the database
            user.save()

            # Return a success response
            return JsonResponse({'message': 'User updated successfully'}, safe=False)

        except models.User.DoesNotExist:
            # Handle case where the user does not exist
            return JsonResponse({'error': 'User not found'}, status=404)

        except json.JSONDecodeError:
            # Handle JSON decoding error
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        except Exception as e:
            # Handle other exceptions
            return JsonResponse({'error': str(e)}, status=500)


@method_decorator(csrf_exempt, name='dispatch')
class Login(View):
    def post(self, request, *args, **kwargs):
        try:
            # Parse JSON data from request body
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')

            if not email or not password:
                return JsonResponse({'error': 'email and password are required'}, status=400)

            # Fetch the user object from the database by email
            try:
                user = models.User.objects.get(email=email)
            except models.User.DoesNotExist:
                return JsonResponse({'error': 'Invalid email or password'}, status=400)

            # Check if the provided password matches the stored (hashed) password
            if check_password(password, user.password):
                # Authentication successful
                return JsonResponse({'message': 'Login successful'}, safe=False)
            else:
                return JsonResponse({'error': 'Invalid email or password'}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
