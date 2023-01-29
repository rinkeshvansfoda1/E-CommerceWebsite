from django.db.models.lookups import YearLookup
from django.http import HttpResponse, request
from django.http.response import Http404
from django.shortcuts import render, get_object_or_404
from django.urls.resolvers import LocalePrefixPattern
from django.utils.functional import partition
from .models import Product, Product_jeans, Product_laptop, Product_phone, Product_smarttv, Product_washing_machine


def index(request):
    # below line also create back button with href, and here we are creating the button and all other stuff which is not good so we will try to use the templates
    # return HttpResponse("Home <a href='https://www.youtube.com/watch?v=ES-bdt0KUZg&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=8'>Back</a>")
    # return HttpResponse("Home <a href='/'>Back</a>")
    # creating the variables
    # params={'Name':'Rinkesh','Place':'New York'}
    # using templates/render

    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def computer(request):
    # return HttpResponse("Search Product")
    # prodss=Product()
    # prodss.Product_Name='ASUS'
    # prodss.Description='Hello Testing work under it'
    # prodss.Image='pc.jpg'
    # prodss.Price=1000
    # prodss.Offer=True
    # prodsss=[prodss]
    product=Product.objects.all()
    for i in product:
        print(i.Image)
    return render(request,'computer.html',{'product':product})

def laptop(request):
    product_laptop=Product_laptop.objects.all()
    return render(request,'laptop.html',{'product_laptop':product_laptop})

def washing_machine(request):
    product_washing_machine=Product_washing_machine.objects.all()
    return render(request,'washing_machine.html',{'product_washing_machine':product_washing_machine})

def phone(request):
    product_phone=Product_phone.objects.all()
    return render(request,'phone.html',{'product_phone':product_phone})

def smarttv(request):
    product_smarttv=Product_smarttv.objects.all()
    return render(request,'smart tv.html',{'product_smarttv':product_smarttv})

def jeans(request):
    product_jeans=Product_jeans.objects.all()
    return render(request,'jeans.html',{'product_jeans':product_jeans})

def aboutus(request):
    return render(request,'aboutus.html')

def ContactUs(request):
    return render(request,'contactus.html')



def product_detail(request,category,id):
    context={
        # 'contact_computer':get_object_or_404(Product,pk=id),
        'contact_laptop':get_object_or_404(Product_laptop,pk=id)
    }
# get to get data in html use diectionary under variable name while fetching over the other html page and other sub details over it like
# contact.Product_Name to get the product name for specific data, and not to use the variable name while fetching it, so use to call by variable which are under the quote of dictionary or call by dictionary key 

    # print(get_object_or_404(Product,pk=id))
    # print(context.get('contact_computer'))
    # print(id)
    # print(get_object_or_404(Product_laptop,pk=id))
    # print(Product_laptop.objects.get(id=id))
    # return HttpResponse("Hello Testing Detail Page",context)

    # return render(request,'product_detail.html',context)

    if category=='laptop':
        return render(request,'product_detail.html',context)
    elif category=='computer':
        return render(request,'product_detail.html',{
            'contact_laptop':get_object_or_404(Product,pk=id)
        })
    elif category=='washing_machine':
        return render(request,'product_detail.html',{
            'contact_laptop':get_object_or_404(Product_washing_machine,pk=id)
        })
    elif category=='phone':
        return render(request,'product_detail.html',{
        'contact_laptop':get_object_or_404(Product_phone,pk=id)
        })
    elif category=='smarttv':
        return render(request,'product_detail.html',{
            'contact_laptop':get_object_or_404(Product_smarttv,pk=id)
        })
    elif category=='jeans':
        return render(request,'product_detail.html',{
            'contact_laptop':get_object_or_404(Product_jeans,pk=id)
        })
    else:
        return Http404("Page not Found")





# Created new template or page under which getting all details like phone, laptop in one page under product
# def productTemplate(request,name):

#     data = {}
#     heading = ""
#     if name == "laptop":
#         data = Product_laptop.objects.all()
#         heading = "Laptop"

#     elif name == "phone":
#         data = [
#             {
#             'Product_Name' : "Phone-1",
#             "Price" : 500
#         },{
#             'Product_Name' : "Phone-2",
#             "Price" : 700
#         },{
#             'Product_Name' : "Phone-3",
#             "Price" : 800
#         },
#         ]
#         heading = "Mobile Phone"
#     else:
#         data = {}
#         heading ="no data Seleted"
    
#     return render(request, 'productTemplte.html',{
#         "heading" : heading,
#         "data" : data
#     })

