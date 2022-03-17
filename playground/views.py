from django.shortcuts import render
from django.http import HttpResponse



# our home page view
def home(request):    
    return render(request, 'home.html')


# custom method for generating predictions
def getPredictions(sepal_length,sepal_width, petal_length, petal_width):
    import pickle
    model = pickle.load(open('iris_log_mode', "rb"))
    prediction = model.predict(([[sepal_length,sepal_width, petal_length, petal_width]]))
    
    if prediction == 0:
        return "not survived"
    elif prediction == 1:
        return "survived"
    else:
        return "error"
        

# our result page view
def result(request):
    sepal_length = float(request.GET['sepal_length'])
    sepal_width = float(request.GET['sepal_width'])
    petal_length = float(request.GET['petal_length'])
    petal_width = float(request.GET['petal_width'])
    

    result = getPredictions(sepal_length,sepal_width, petal_length, petal_width)

    return render(request, 'result.html', {'result':result})
# Create your views here.
