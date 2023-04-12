from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'JobsInfo/index.html')


def hydjob(request):
    # jobs_list=hydjob.objects.order_by('date')
    jobs_list=hydjob.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'JobsInfo/hyd.html',context=my_dict)
    # return render(request,'JobsInfo/hyd.html')

def punejobs(request):
    # s='<h1>This is Pune jobs Information</h1>'
    return render(request,'JobsInfo/pune.html')

def chennaijobs(request):
    # s='<h1>This is Chennai jobs Information</h1>'
    return render(request,'JobsInfo/chennai.html')

def bangjobs(request):
    # s='<h1>This is Banglour jobs Information</h1>'
    return render(request,'JobsInfo/bangl.html')



