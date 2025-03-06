from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello_nfactorial(request):
    return HttpResponse("Hello, nfactorial school!")

def add(request, first, second):
    result = first + second
    return HttpResponse(f"Summ: {result}")

def upper(request, text):
    result = text.upper()
    return HttpResponse(f"Upper: {result}")

def palindrome(request, word):
    if word == word[::-1]:
        return HttpResponse("True")
    else:
        return HttpResponse("False")

def calculator(request, first, operation, second):
    if operation == 'add':
        result = first + second
    elif operation == 'sub':
        result = first - second
    elif operation == 'mult':
        result = first * second
    elif operation == 'div':
        if second != 0:
            result = first / second
        else:
            return HttpResponse("Div by zero")
    else:
        return HttpResponse("Unknown operation")
    return HttpResponse(f"Result: {result}")