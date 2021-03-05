from django.shortcuts import render

#test view

def test(request):
    return render(request, 'index.html')
