from django.shortcuts import render, redirect

def index(request):
    return render(request, "index.html")

def result(request):
    print("Survey Results.................")
    name_from_form = request.POST['name']
    location_from_form = request.POST['location']
    language_from_form = request.POST['favoritelanguage']
    comment_from_form = request.POST['comment']
    context =  {
        "name_on_survey" : name_from_form,
        "location_on_survey": location_from_form, 
        "language_on_survey": language_from_form, 
        "comment_on_survey": comment_from_form, 
    }
    return render(request,"show.html",context)

