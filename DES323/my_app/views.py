from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from my_app.models import *
import pandas as pd
import requests
from django.contrib.auth import authenticate , login
from django.shortcuts import render, redirect


from django.contrib.auth.models import User
from .serailizers import *
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def user(request):
    return render(request, "user.html")

def search(request):
    return render(request, "search.html")

def login(request):
    # if request.method == 'POST':
    #     email = request.POST['email']
    #     pass1 = request.POST['pass']
        
    #     user_ac = authenticate(email=email, password=pass1)
        
    #     if user_ac is not None:
    #         login(request, user_ac)
    #         username = user.username
    #         # messages.success(request, "Logged In Sucessfully!!")
    #         return render(request, "search",{"username":username})
        
            
    
    return render(request, "login.html")

    

def register(request):
    if request.method == "POST":
        form_data = request.POST
        new_item = user_ac(
            email = form_data['regis_email'],
            username = form_data['regis_username'],
            password =  form_data['regis_password']
        )
        
        new_item.save()
        return redirect('/login')



    return render(request, "register.html")

def contact(request):
    return render(request, "contact.html")

def result(request):
    return render(request, "result.html")

def pincode(request):
    return render(request, "pincode.html")

def dairy(request):
    csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT8cyD5DN8VtbyY1WVKiWXTvb1njwjK-8PupnJR1Otb3rX8QPsu-u8Vs9miQzDs-vCEWvJVZCuA_2xA/pub?output=csv"
    df = pd.read_csv(csv_url)
    dataset = df[["Location", "Total Land Area (acres)", "Number of Cows", "Price per Unit", "Date", "Farm Size", "Product Name", "Quantity (liters/kg)"]]
    success = []
    errors = []
    for index, row in dataset.iterrows():
        instance = dairy_dataset(
            location = row['Location'],
            tot_land_area = row['Total Land Area (acres)'],
            num_cows = int(row['Number of Cows']),
            price = row['Price per Unit'],
            recording_date = row['Date'],
            farm_size = row['Farm Size'],
            product_type = row['Product Name'],
            quantity = int(row['Quantity (liters/kg)'])
        )
        try:
            instance.save()
            success.append(index)
        except:
            errors.append(index)
    return JsonResponse({"success_indexes":success,"error_index":errors})
########################################################################
def create(request):
    if request.method == "POST":
        form_data = request.POST
        new_item = dairy_dataset(
            location = form_data['location'],
            tot_land_area = form_data['tot_land_area'],
            num_cows = int(form_data['num_cows']),
            price = form_data['price'],
            recording_date = form_data['recording_date'],
            farm_size = form_data['farm_size'],
            product_type = form_data['product_type'],
            quantity = int(form_data['quantity'])
        )
        try:
            new_item.save()
        except:
            return HttpResponse("An error has occured.")
        return redirect('read')
    context_data = {
        'item_id': "New",
        'form_data': {
            'location':"",
            'tot_land_area':0,
            'num_cows':0,
            'price':0,
            'recording_date':"",
            'farm_size':"",
            'product_type':"",
            'quantity':0
        }
    }
    return render(request, 'create_data.html', context = context_data)

def read(request):
    dairy_objects = dairy_dataset.objects.all()
    context_data = {
        "filter_type":"All",
        "datasets": dairy_objects
    }
    return render(request, 'crud_result.html', context = context_data)

def update(request, id):
    try:
        item = dairy_dataset.objects.get(id = id)
    except:
        return HttpResponse("ID not found")
    if request.method == "POST":
        form_data = request.POST
        item.location = form_data['location'],
        item.tot_land_area = form_data['tot_land_area'],
        item.num_cows = int(form_data['num_cows']),
        item.price = form_data['price'],
        item.recording_date = form_data['recording_date'],
        item.farm_size = form_data['farm_size'],
        item.product_type = form_data['product_type'],
        item.quantity = int(form_data['quantity'])
        try:
            item.save()
        except:
            return HttpResponse("An error has occured.")
        return redirect('read')
    context_data = {
        'item_id': id,
        'form_data': {
            'location':item.location,
            'tot_land_area':item.tot_land_area,
            'num_cows':item.num_cows,
            'price':item.price,
            'recording_date':item.recording_date,
            'farm_size':item.farm_size,
            'product_type':item.product_type,
            'quantity':item.quantity
        }
    }
    return render(request, 'create_data.html', context = context_data)
    
def delete(request, id):
    dairy_objects = dairy_dataset.objects.filter(id = id)
    if len(dairy_objects) <= 0:
        return HttpResponse("ID not found")
    dairy_objects.delete()
    return redirect('read')    
#############################################################################
#### crud user ##########################################################

    
        






#### crud user ##########################################################
def external_api(request):
    api_url = "https://api.postalpincode.in/pincode/110001"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()

    # Assuming the response structure is a list with one object
    if len(data) > 0:
        # Access the first (and only) object in the list
        specific_object = data[0]

        # Access and print specific elements within the object
        print("Status:", specific_object.get("Status"))
        print("Message:", specific_object.get("Message"))

        # Accessing PostOffice details (assuming it's also a list)
        post_offices = specific_object.get("PostOffice", [])
        for office in post_offices:
            print("Post Office Name:", office.get("Name"))
            print("Delivery Status:", office.get("DeliveryStatus"))
            print("District:", office.get("District"))
            print("State:", office.get("State"))
            print("-------------------")
        else:
            print("No data available.")
    else:
        print("Failed to fetch data. Status code:", response.status_code)
    

    return JsonResponse(response.json(), safe=False)
###############################################################################
def data_sci_item_list_all(request):
    dataset_objs = user_ac.objects.all()
    context_data = {
        "filter_type": "All",
        "datasets": dataset_objs
    }
    return render(request, 'list_view.html', context=context_data)

def data_sci_item_edit(request, id):
    try:
        item = user_ac.objects.get(id=id)
    except:
        return HttpResponse("ID Not found")
    if request.method == "POST":
        form_data = request.POST
        item.email = form_data['Email']
        item.username = form_data['Username']
        try:
            item.save()
        except:
            return HttpResponse("ERROR!")
        return redirect('/manage_user')
    context_data = {
        'item_id': id,
        'form_data': {
            'Email': item.email,
            'Username': item.username
        }
    }
    return render(request, 'form.html', context=context_data)

def data_sci_item_delete(request, id):
    dataset_objs = user_ac.objects.filter(id = id)
    if len(dataset_objs) <= 0:
        return HttpResponse("ID Not found")
    dataset_objs.delete()
    return redirect('/manage_user')
###########################################################################

@csrf_exempt
def api_register(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = AuthenticationAPISerializer(data=data)
        if serializer.is_valid():
            user = User.objects.create_user(
            username = serializer.data['username'],
            password = serializer.data['password']
            )
            token = Token.objects.create(user=user)
            return JsonResponse({"status":"success","token":token.key}, status=200)
        #else:
        return JsonResponse({"status":"failed","message":"Input not valid."})
    return JsonResponse({"status":"failed", "message":"Method not allowed."},status=400)