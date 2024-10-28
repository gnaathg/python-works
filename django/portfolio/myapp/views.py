from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class IndexView(View):
    
    def get(self,request,*args,**kwargs):

        person_data = {
            "id":1,
            "age":22,
            "name":"Sabari",
            "location":"kayamkulam",
            "adress":'adress',
        }
        return render(request,"index.html",{'person':person_data})
    
class ProjectView(View):

    def get(self,request,*args,**kwargs):

        projects=[
            {"id":1,"title":"codehub",
             "description":"project decsription",
             "front_end":"react","back_end":"django"
             },
              {"id":2,"title":"ServiceHub",
             "description":"project decsription",
             "front_end":"Angular","back_end":"django"
             },
              {"id":3,"title":"linksphere",
             "description":"project decsription",
             "front_end":"react","back_end":"django"
             }
        ]

        return render(request,"project.html",{'projects':projects})

class ContactView(View):

    def get(self,request,*args,**kwargs):

        phone = "123456789"
        email = "abc@gmail.com"

        return render(request,"contact.html",{'phone':phone,'eamil':email})

class SkillView(View):

    def get(self,request,*args,**kwargs):

        python = "python"
        django = "django"

        return render(request,"skill.html",{'python':python,'django':django})


class Servicesview(View):

    def get(self,request,*args,**kwargs):

        services=["web app development","ui/ux","dtata analysis"]

        return render(request,"services.html",{'services':services})



