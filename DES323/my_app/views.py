from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from my_app.models import dairy_dataset
import pandas as pd
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

def dairy(request):
    csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRsQsF25947ZGBAMUS_ljKLeV4bFzPSOf_wShl8_mqXOwvohpmxXq0bu-zFfGn2ppf4TmS1lNIl7aLU/pub?output=csv"
    df = pd.read_csv(csv_url)
    dairy_dataset = df[["Location", "Total Land Area (acres)", "Number of Cows", "Price per Unit", "Date", "Farm Size", "Product Name", "Quantity (liters/kg)"]]
    success = []
    errors = []
    for index, row in dairy_dataset.iterrows():
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
    """
        try:
            instance.save()
            success.append(index)
        except:
            errors.append(index)
    return JsonResponse({"success_indexes":success, "error_indexes":errors})
    """
