from django.shortcuts import render
from restuarent.models import Menu
result=Menu.objects.all()
# Create your views here.
def fun1(request):
    result=Menu.objects.all()
    
    context={"result":result}
    return render(request,"Home.html",context)

def fun2(request):
    Result=Menu.objects.all()
    
    if request.method == "POST":
        Item=str(request.POST.get("item"))
        if Menu.objects.filter(name=Item).exists():
            abc=Menu.objects.get(name=Item) 
        else:
            abc=None
        return render(request,"item.html",{"res":Result,"res2":abc})
            

    
    return render(request,"item.html")



def fun3(request):
    result=Menu.objects.all()
    if request.method=="POST":
        dish=request.POST.get("food")
        cost=request.POST.get("price")
        obj=Menu(name=dish,price=cost)
        obj.save()
        result=Menu.objects.all()
        return render(request,"pr.html",{"res":result , "obj":obj})
    return render(request,"pr.html")