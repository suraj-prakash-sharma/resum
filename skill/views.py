from django.shortcuts import render

# Create your views here.
def skill(request):
    context={'skill':'active'}
    return render(request,'skilll/skill.html',context)