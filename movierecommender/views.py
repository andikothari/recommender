from . import views
from .models import Movie
from django.shortcuts import render
from django.http import HttpResponseServerError

# HINT: Create a view to provide movie recommendations list for the HTML template

# def movie_recommendation_view(request): 
#     if request.method == "GET":
#         # The context/data to be presented in the HTML template
#         context = {}
#         # Render a HTML page with specified template and context
#         return render(request, 'movierecommender/movie_list.html', context)


def movie_recommendation_view(request):
    try:
        if request.method == "GET":
            # The context/data to be presented in the HTML template
            context = {}
            # Render a HTML page with specified template and context
            return render(request, 'movierecommender/movie_list.html', context)
        else:
            # Handle other HTTP methods if necessary
            return HttpResponseServerError("Unsupported HTTP method.")
    except Exception as e:
        # Log the exception (you can use logging instead of print in a real application)
        print(f"An error occurred: {e}")
        # Return a generic error response
        return HttpResponseServerError("An internal server error occurred.")