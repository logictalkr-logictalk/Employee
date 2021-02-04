from django.shortcuts import render, redirect
from .models import Asset
from .forms import AssetForm

# Create your views here.
def assetList(request):  
    assets = Asset.objects.all()  
    return render(request,"asset-list.html",{'assets':assets})  

def assetCreate(request):  
    if request.method == "POST":  
        form = AssetForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('asset-list')  
            except:  
                pass  
    else:  
        form = AssetForm()  
    return render(request,'asset-create.html',{'form':form})  

def assetUpdate(request, id):  
    asset = Asset.objects.get(id=id)
    form = AssetForm(initial={'empid': asset.empid, 'empname': asset.empname, 'asset': asset.asset})
    if request.method == "POST":  
        form = AssetForm(request.POST, instance=asset)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/asset-list')  
            except Exception as e: 
                pass    
    return render(request,'asset-update.html',{'form':form})  

def assetDelete(request, id):
    asset = Asset.objects.get(id=id)
    try:
        asset.delete()
    except:
        pass
    return redirect('asset-list')