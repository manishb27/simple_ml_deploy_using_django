from django.shortcuts import render
from django.http import HttpResponse
import joblib



# our home page view
def home(request):    
    return render(request, 'home.html')


# custom method for generating predictions
def getPredictions(sepal_length,sepal_width, petal_length, petal_width):
    model = joblib.load('playground/iris_log_model.sav')
    prediction = model.predict(([[sepal_length,sepal_width, petal_length, petal_width]]))
    
    if prediction == 0:
        return "Setosa"
    elif prediction == 1:
        return 'Versicolor'
    else:
        return 'Virginica'
        

# our result page view
def result(request):
    sepal_length = float(request.GET['sepal_length'])
    sepal_width = float(request.GET['sepal_width'])
    petal_length = float(request.GET['petal_length'])
    petal_width = float(request.GET['petal_width'])
    
    print(sepal_length, sepal_width, petal_length, petal_width)

    ans = getPredictions(sepal_length,sepal_width, petal_length, petal_width)

    return render(request, 'result.html', {'ans': ans})
# Create your views here.

# , {'result':result}
# def indexed(request):
#     return render(request, 'index.html' )