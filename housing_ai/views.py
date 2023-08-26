from django.shortcuts import render
# , HttpResponse


#for model
from joblib import dump, load
import numpy as np
import pandas as pd



# Create your views here.
def index(request):
    global longitude
    global latitude
    global housing_median_age
    global total_rooms
    global total_bedrooms
    global population
    global households
    global median_income
    global ocean_proximity
    
    # global label
    # global a
    # a=50
    if request.method == "POST":
        longitude = request.POST.get('longitude')
        # label = request.POST.get('label')
        latitude = request.POST.get('latitude')
        housing_median_age = request.POST.get('housing_median_age')
        total_rooms = request.POST.get('total_rooms')
        total_bedrooms = request.POST.get('total_bedrooms')
        population = request.POST.get('population')
        households = request.POST.get('households')
        median_income = request.POST.get('median_income') 
        ocean_proximity = request.POST.get('ocean_proximity')
    # print(longitude)
        

    return render(request, 'index.html')
# np_array = [[longitude, latitude, housing_median_age, total_rooms, total_bedrooms, population, households, median_income, ocean_proximity]]
''', ocean_proximity_1H_OCEAN, ocean_proximity_INLAND, ocean_proximity_ISLAND, ocean_proximity_NEAR_BAY, ocean_proximity_NEAR_OCEAN'''


def solution(request):
    # import pdb
    # pdb.set_trace()
    longitude= abs(float(request.POST.get('longitude')))
    latitude = float(request.POST.get('latitude'))
    housing_median_age = float(request.POST.get('housing_median_age'))
    total_rooms = float(request.POST.get('total_rooms'))
    total_bedrooms = float(request.POST.get('total_bedrooms'))
    population = float(request.POST.get('population'))
    households = float(request.POST.get('households'))
    median_income = float(request.POST.get('median_income'))
    ocean_proximity = float(request.POST.get('ocean_proximity'))
    # print(abs(longitude))
    # print(type(longitude))
    # print(type(latitude))
    # print(type(housing_median_age))
    # print(type(total_rooms))
    # print(type(total_bedrooms))
    # print(type(population))
    # print(type(households))
    # print(type(median_income))
    # print(type(ocean_proximity))

    

    array = [[longitude, latitude, housing_median_age, total_rooms, total_bedrooms, population, households, median_income, ocean_proximity]]
    p_pred=price_predictor(array)
    return render(request, 'solution.html', {'longitude': round(p_pred, 2)})



#model

def price_predictor(np_array):
    list = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income', 'ocean_proximity']
    regressor = load('housing.joblib')
    df = pd.DataFrame(np_array, columns = list[:]) 
    # df = pd.read_csv('read.csv')
    # df.iloc[:,0:7] = abs(df.iloc[:,0:7])
    pred_data = regressor.predict(np_array)
    return (float(pred_data[0]))