from django.shortcuts import redirect, render

# Create your views here.
def login_redirect(request):
    return redirect('/account/login')

def web_home(request):
    return render(request,"home/web_home.html")