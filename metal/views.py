import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Metal
def home(request):
    return JsonResponse("this is metal homepage",safe=False)
@method_decorator(csrf_exempt,name='dispatch')
class Crud(View):
    #post request
    def post(self,request):
        try:
            data=json.loads(request.body)

            save_data=Metal()

            save_data.name=data.get('name')
            save_data.email=data.get('email')
            save_data.save()
            return JsonResponse("Sucessfully data save",safe=False)
        except json.JSONDecodeError:
            return JsonResponse("Invalid json data",safe=False)
        except Exception as e:
            return JsonResponse(str(e),safe=False)
        
        #Get request
    def get(self,request):
        try:
            metals=Metal.objects.all()
            metal_list = list(metals.values())
            return JsonResponse(metal_list,safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class Del_Patch(View):
    def delete(self, request, *args, **kwargs):
        metal_id = kwargs.get('id')  
        if metal_id is not None:
            try:
                deleted_count,_ = Metal.objects.get(id=metal_id).delete()
                if deleted_count > 0:
                    return JsonResponse("ID successfully deleted", safe=False)
                else:
                    return JsonResponse(f"No record found with ID {metal_id}", safe=False, status=404)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse("ID not provided", safe=False, status=400)
    def patch(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            metal_id = kwargs.get('id')
            if metal_id is not None:
                metal = Metal.objects.get(id=metal_id)
                if 'name' in data:
                    metal.name = data['name']
                if 'email' in data:
                    metal.email = data['email']
                metal.save()
                return JsonResponse("Metal object updated successfully", safe=False)
            else:
                return JsonResponse("ID not provided", safe=False, status=400)
        except Metal.DoesNotExist:
            return JsonResponse(f"No record found with ID {metal_id}", safe=False, status=404)
        except json.JSONDecodeError:
            return JsonResponse("Invalid JSON data", safe=False, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    # def delete(self, request, *args, **kwargs):
    #     metal_id = kwargs.get('id')  
    #     if metal_id is not None:
    #         try:
    #             metal = Metal.objects.get(id=metal_id)
    #             metal.delete()
                
    #             return JsonResponse(f"ID {metal_id} successfully deleted", safe=False)
    #         except Metal.DoesNotExist:
    #             return JsonResponse(f"No record found with ID {metal_id}", safe=False, status=404)
    #         except Exception as e:
    #             return JsonResponse({'error': str(e)}, status=500)
    #     else:
    #         return JsonResponse("ID not provided", safe=False, status=400)
