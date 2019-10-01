from django.shortcuts import render,redirect
from django.http import HttpResponse

from .forms import *
#from .models import *

# Create your views here.

#calculation
def calu(request):

    return render(request, 'myapp/cal.html',{'name1':'manoj'} )



def add(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    if 'add' in request.GET:

        res = val1+val2

    elif 'sub' in request.GET:
        res = val1 - val2

    elif 'mul' in request.GET:
        res = val1 * val2

    elif 'div' in request.GET:
        res = val1 / val2
    return render(request, 'myapp/index.html', {'result': res})





def mycontact(request):
    form1 = contctform(request.POST)
    if request.method == 'POST':

            if form1.is_valid():
                form1.save(commit=True)
    return render(request,'myapp/home.html',({'form': form1 }))

'''
def myview(request):
    queryset = ImageModel.objects.all()
    context = {'queryset ': queryset}
    return render(request, 'myapp/index.html' , context)
'''

def hotel_image_view(request):
    if request.method == 'POST':
        formi = HotelForm(request.POST, request.FILES)

        if formi.is_valid():
            formi.save()
            return redirect('success')
    else:
        formi = HotelForm()
    return render(request, 'myapp/index.html', {'formi': formi})


def success(request):
    return HttpResponse('successfuly uploaded')