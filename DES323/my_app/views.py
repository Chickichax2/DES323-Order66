from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from my_app.models import dairy_dataset
import pandas as pd
import requests
import json
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
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def contact(request):
    return render(request, "contact.html")

def result(request):
    return render(request, "result.html")

def pincode(request):
    return render(request, "pincode.html")

def dairy(request):
    csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRsQsF25947ZGBAMUS_ljKLeV4bFzPSOf_wShl8_mqXOwvohpmxXq0bu-zFfGn2ppf4TmS1lNIl7aLU/pub?output=csv"
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
    return JsonResponse({"success_indexes":success, "error_indexes":errors})

def create(request):
    pass

def view(request):
    dairy_objects = dairy_dataset.objects.all()
    list_dairy_dataset = {
        "filter_type":"All",
        "datasets": dairy_objects
    }
    return render(request, 'crud_result.html', context = list_dairy_dataset)

def update(request):
    pass

def delete(request):
    pass
    
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
        
