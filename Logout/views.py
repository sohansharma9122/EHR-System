from django.shortcuts import render

# Create your views here.

def logout(request):
    #Clear all session data
    request.session.flush()
    return render(request, 'logout.html', {'MSG': 'You have been logged out successfully!'})
