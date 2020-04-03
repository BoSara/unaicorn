from django.shortcuts import render
from . import ml_heart

def home(request):
	return render(request, 'index.html')

def result(request):
    age = int(request.GET['age'])
    sex = int(request.GET['sex'])
    cp = int(request.GET['cp'])
    trestbps = int(request.GET['trestbps'])
    chol = int(request.GET['chol'])
    fbs = int(request.GET['fbs'])
    restecg = int(request.GET['restecg'])
    thalach = int(request.GET['thalach'])
    exang = int(request.GET['exang'])
    oldpeak = float(request.GET['oldpeak'])
    slope = int(request.GET['slope'])
    ca = int(request.GET['ca'])
    thal = int(request.GET['thal'])
    prediction= ml_heart.rfc_heart_model(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
    return render(request, 'result.html', {'prediction':prediction})