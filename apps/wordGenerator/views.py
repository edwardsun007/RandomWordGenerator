from django.shortcuts import render, redirect  # for redirect
from django.contrib import messages   # for display flash message on page
from django.utils.crypto import get_random_string
def index(request):
    # home page
    # attempt by 1
    # generate word
    try:
        request.session['attempts']
    except KeyError: # if the key not exist means this is 1st time we visit, start to 0
        request.session['attempts'] = 0

    return render(request, "wordGenerator/index.html")


# once click button, we need to generate the string and pass it throught session
def generate(request):
    request.session['attempts']+=1
    randWord = get_random_string(length=12)
    request.session['word']=randWord
    return redirect('/')

# reset attempt back to 0
def reset(request):
    # reset attempt to 0
    #request.session['attempts'] = 0
    del request.session['attempts']   # you can either reset it or delete the entire dict to get the same goal
    #tryGet = request.session['attempts'] # after del , you will hit reference error if you still want to access it
    del request.session['word']
    return redirect('/')
