from django.shortcuts import render

# Create your views here.
def nearbydetails(request):
    return render(request ,"nearbydetails/location.html")
def Myflat(request):
    return render(request ,"nearbydetails/Myhome.htm")
def Milkfarm(request):
    return render(request ,"nearbydetails/Milkfarm.htm")
def Tutioncentre(request):
    return render(request ,"nearbydetails/Tutioncentre.html")
def Rationshop(request):
    return render(request ,"nearbydetails/Rationshop.html")
def Generalstores(request):
    return render(request ,"nearbydetails/Generalstores.html")