from django.shortcuts import render

# Create your views here.
def home(request):
    name = 'Rajkumar'
    args = {'myName': name}
    return render(request, 'accounts/login.html', args)