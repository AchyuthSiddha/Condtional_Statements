from django.shortcuts import render

# Create your views here.
def Cond(request):
    d={'a':201,'b':301,'c':302}
    return render(request,'app/conditional.html',d)


def Loop(request):
    d={'name':'Achyuth'}
    return render(request,'app/Loops.html',d)

