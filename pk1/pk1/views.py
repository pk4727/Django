from django.http import HttpResponse                                # for function   
from django.shortcuts import render                                 # for import pages
from service.models import service_custom                           # for render dynamic data of admin
from editor.models import editor_news                               # for render editor data in admin
from django.core.paginator import Paginator                         # for paginator in any page
from django.core.mail import send_mail ,EmailMultiAlternatives      # for sending mail

# def p(request):                                                   # url function                                                      
#     return HttpResponse('<b>-:welcome to pk site:-<b>')

def about(request):
# for sending editor or news all data to the webpage
    editor_data = editor_news.objects.all()

# sending admin data to the webpage with the help of this used only one at a time
    # service_custom_data = service_custom.objects.all().order_by('-service_1')         # used for asscending order rander
    # service_custom_data = service_custom.objects.all().order_by('service_1')          # used for descending order render
    # service_custom_data = service_custom.objects.all().order_by('service_1')[:5]      # add limit to render by slicing but not -ve slicing
    service_custom_data = service_custom.objects.all()                                  # used for rander data of admin dynamicily
    if request.method=="GET":
        val = request.GET.get('servicename')
        if val!=None:
            # service_custom_data = service_custom.objects.filter(service_1=val)            # for search from same word which is in para_title
            service_custom_data = service_custom.objects.filter(service_1__icontains=val)   # for search from 1 to multi character

# for paginator used which is apply in dynamic data for limit and condition of printing in page
    Paginators = Paginator(service_custom_data, 2)      # set limit 
    page_no = request.GET.get('page')                   # for page number
    final_pagenator = Paginators.get_page(page_no)      # for final paginator value
    total_page = final_pagenator.paginator.num_pages     # for total page number

# dictonary for key value pair whichis used in about.html page
    servicedata = {
        # "admin_data":service_custom_data,
        "editor_data":editor_data,
        "admin_data":final_pagenator,
        "last_Page":total_page,
        "page_numbers":[n+1 for n in range(total_page)]
        }

# for multi_mail without html tag
    # send_mail(
        # "testing mail here",
        # "Here is the message for email testing by pradhuman kumar.",
        # "rinakri8789@gmail.com",
        # ["pradhumanpk2019@gmail.com"],
        # fail_silently=False,
    # )

# for multi_mail with html tag 
    subject= "testing mail here"
    message = "Here is the message for email testing by pradhuman kumar."
    to_m = 'pradhumanpk2019@gmail.com'
    from_m = 'rinakri8789@gmail.com'
    email = EmailMultiAlternatives(subject,message,from_m,[to_m])
    email.content_subtype='html'
    email.send()

    return render(request,"about.html",servicedata)

def editor(request,slug):
    news_details = editor_news.objects.get(news_slug=slug)
    data = {"news_data":news_details}
    return render(request,"5.html",data)

def dynamic(request,dy):                                        # dynamic function
    return HttpResponse(dy)

def p1(request):                                   # rander(it return page) for page importing
    data={
    "pk":"pradhuman kumar",
    "page":"page1",
    "vill":"from giridih"
    }                   
    return render(request,"1.html",data)        # (request,"page name")

def p2(request):                                 # usefor "for loop" in html
    data={
    "name":"pradhuman kumar",
    "urln":"pk",
    "distic":"from giridih",
    "family":["kk","sk","dk","pk","rk","dpk","knk"],
    "no":[10,20,30,40,50,60,70,80,90,100],
    "table":[{10:[10,20,30,40,50,60,70,80,90,100],20:[20,40,60,80,100,120,140,160,180,200] }],
    "na_no":[ {"Name":"pk","Phone":8409584727},{"Name":"dk","Phone":7763071522} ]
    }                                              
    return render(request,"2.html",data) 

def p3(request):
        if request.method=="GET":
            output_of_url=request.GET.get('output')
        return render(request,"3.html",{'value':output_of_url})

def p4(request):
    return render(request,"4.html")

def p5(request):
    return render(request,"5.html")

def userformget(request):
    n=0
    try:
        if request.method=="GET":
            n1=int(request.GET['name'])
            n2=int(request.GET['village'])
            n3=int(request.GET['distic'])
            # n4=request.GET.get('name')
            n=n2+n3+n1
    except:
        pass
    return render(request,"userformg.html",{"outputg":n})


from django.http import HttpResponseRedirect
from django.shortcuts import redirect
def userformpost(request):
    nn=0
    data={}
    try:
        if request.method=="POST":
            n5=int(request.POST.get('name'))
            n6=int(request.POST.get('village'))
            n7=int(request.POST.get('distic'))
            # n8=request.GET.get('name')
            nn=n5+n6+n7
            data={"n5":n5,"n6":n6,"n7":n7,"output":nn}
            
            url="/?output={}".format(nn)
            # return HttpResponseRedirect(url)
            # return HttpResponseRedirect('/')
            return redirect(url)
    except:
        pass
    return render(request,"userformp.html",data)

def submitform(request):
    nn=0
    try:
        if request.method=="POST":
            n5=int(request.POST.get('name'))
            n6=int(request.POST.get('village'))
            n7=int(request.POST.get('distic'))
            nn=n5+n6+n7
    except:
        pass
    return HttpResponse(nn)



from .forms import d_forms ,user_inputss
def d_form(request):
    a=d_forms()
    user_form= user_inputss()
    b={'form_used':a,"user_form":user_form}
    return render(request,"d_forms.html",b)

from users_input.models import user_input
def user_inputt(request):
    submit_out=''
    if request.method == "POST":
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        date = request.POST.get('date')
        description = request.POST.get('description')
        input = user_input(name=name,subject=subject,date=date,description=description)
        input.save()
        submit_out = "form submited"
        data = {"out":submit_out}
    return render(request,"d_forms.html",data)

def calculator(request):
    c=''
    data={}
    try:
        if request.method=="POST":
            n=eval(request.POST.get('number1'))
            n1=eval(request.POST.get('number2'))
            opr=request.POST.get('operator')
            if opr=="+":
                c=n+n1
            elif opr=="-":
                c=n-n1
            elif opr=="*":
                c=n*n1
            elif opr=="/":
                c=n/n1 
            data={'n':n,'n1':n1,'output':c}
    except:
        pass
    return render(request,"calculator.html",data)
    

def even(request):
    c=""
    n=""
    if request.method=="POST":

        if request.POST.get("num")=="":                     # used for error comes when we submit without value
            return render(request ,"even_odd.html",{'error':True})
        
        n=eval(request.POST.get("num"))
        if n%2==0:
            c="Even Number"
        else:
            c="Odd Number"

    return render(request ,"even_odd.html",{'n':n,'output':c})


import math
def marksheet(request):
    total=""
    perr=""
    grade=""
    if request.method=="POST":
        m=eval(request.POST.get("Maths"))
        p=eval(request.POST.get("Physic"))
        ch=eval(request.POST.get("Chemistry"))
        co=eval(request.POST.get("Computer"))
        h=eval(request.POST.get("Hindi"))
        total=m+p+ch+co+h
        per=total/5
        perr=math.ceil(per)
        if per>90:
            grade="A1"
        elif per>80 and per<90:
            grade="A"
        elif per>70 and per<80:
            grade="B1"
        elif per>60 and per<70:
            grade="B"
        elif per>50 and per<60:
            grade="C1"   
        elif per>40 and per<50:
            grade="C1"
        else:
            grade="Fail"     
        data={'m':m,'p':p,'ch':ch,'co':co,'h':h,'total':total,'per':perr,'grade':grade}  
        return render(request,"marksheet.html",data)
    return render(request,"marksheet.html")
