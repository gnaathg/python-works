from django.shortcuts import render
from django.views.generic import View
from operations.forms import BmiForm,BmrForm,WeightManagementForm,EmiForm,MileageForm,SignupForm,RegistrationForm

# Create your views here.

class AdditionView(View):

    template_name="addition.html"

    def get(self,request,*args,**kwargs):

        return render(request,self.template_name)

    def post(self,request,*args,**kwargs):

        n1 = request.POST.get("num1")

        n2 = request.POST.get("num2")

        result = int(n1) + int(n2)

        print(result)

        return render(request,self.template_name,{'result' :result})

class SubtractionView(View):

    template_name="subtraction.html"

    def get(self,request,*args,**kwargs):

        return render(request,self.template_name)

    def post(self,request,*args,**kwargs):

        n1 = request.POST.get("num1")

        n2 = request.POST.get("num2")

        result = int(n1) - int(n2)

        print(result)

        return render(request,self.template_name,{'result':result})

class MultiplicationView(View):

    template_name="multiplication.html"

    def get(self,request,*args,**kwargs):

        return render(request,self.template_name)

    def post(self,request,*args,**kwargs):

        n1 = request.POST.get("num1")

        n2 = request.POST.get("num2")

        result = int(n1) * int(n2)

        print(result)

        return render(request,self.template_name,{'result':result})

class DivisionView(View):

    template_name = "division.html"

    def get(self,request,*args,**kwargs):

        return render(request,self.template_name)

    def post(self,request,*args,**kwargs):

        n1 = request.POST.get('num1')

        n2 = request.POST.get("num2")

        result = int(n1)/int(n2)

        print(result)

        return render(request,self.template_name,{'result':result})

class CubeView(View):

    template_name = "cube.html"

    def get(self,request,*args,**kwargs):

        return render(request,self.template_name)

    def post(self,request,*args,**kwargs):

        n1 = request.POST.get('num1')

        result = int(n1)**3

        print(result)

        return render(request,self.template_name,{'result':result})

class BmiView(View):

    template_name = 'bmi.html'

    def get(self,request,*args,**kwargs):

        form_instance = BmiForm

        return render(request,self.template_name,{'form':form_instance})

    def post(self,request,*args,**kwargs):

        form_data = request.POST

        form_instance = BmiForm(form_data)

        if form_instance.is_valid():

            height = form_instance.cleaned_data.get("height")

            weight = form_instance.cleaned_data.get("weight")

            bmi = weight/(height/100)**2

        return render(request,self.template_name,{'form':form_instance,'result':bmi})

def calculate_bmr(height,weight,age,gender):

    if gender == 'male':

                bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)

    else:

                bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

    return bmr

def calorie_intake(bmr,activity):
     
     return float(activity)*bmr

class BmrView(View):

    template_name = 'bmr.html'

    def get(self, request, *args, **kwargs):

        form_instance = BmrForm

        return render(request, self.template_name, {'form': form_instance})

    def post(self, request, *args, **kwargs):

        form_data = request.POST

        form_instance = BmrForm(form_data)

        if form_instance.is_valid():

            data = form_instance.cleaned_data

            height = data.get("height")

            weight = data.get('weight')

            age = data.get('age')

            gender = data.get('gender')

            activity = data.get("activity")

            print(height, weight, activity, age, gender)

            bmr = calculate_bmr(height,weight,age,gender)

            calorie = calorie_intake(bmr,activity)

            print(calorie)

            return render(request, self.template_name, {'form': form_instance, 'result': bmr})

class WeightManagementView(View):

    template_name = "weight_management.html"

    form_class = WeightManagementForm

    def get(self,request,*args,**kwargs):

        form_instance = self.form_class()

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
         
         form_data = request.POST
         
         form_instance = self.form_class(form_data)

         if form_instance.is_valid():
              
              data = form_instance.cleaned_data

              height = data.get("height")

              weight = data.get("weight")

              age = data.get("age")

              gender = data.get("gender")

              activity = data.get("activity")

              mode = data.get("mode")

              duration = data.get("duration") 

              target_weight = data.get("target_weight")

              print(height,weight,age,gender,activity,mode,duration,target_weight)

              bmr = calculate_bmr(height,weight,age,gender)

              calories = calorie_intake(bmr,activity)

              days = duration*7

              target_calorie = target_weight*7700

              daily_target_calorie = target_calorie/days

              total_calorie = 0

              if mode == "gain":
                   
                   total_calorie = calories + daily_target_calorie

              else:
                   
                   total_calorie = calories - daily_target_calorie

              result = f"Calorie to maintain current weight {round(calories)}"

              result2 = f"Daily calories to {mode} to {target_weight}kg in {days} days is {round(total_calorie)}"

         return render(request,self.template_name,{"form":form_instance,"result":result,"result2":result2})

class EmiView(View):

    template_name = "emi.html"

    def get(self,request,*args,**kwargs):

        form_instance = EmiForm()

        return render(request,self.template_name,{'form':form_instance})
    
    def post(self, request, *args, **kwargs):

        form_data = request.POST

        loan = int(form_data.get('loan'))
        annual_interest = float(form_data.get('interest')) / 100
        tenure = int(form_data.get('tenure'))

        
        monthly_interest = annual_interest / 12

       
        emi = loan * monthly_interest * (1 + monthly_interest) ** tenure / ((1 + monthly_interest) ** tenure - 1)

        
        form_instance = EmiForm()

        
        return render(request, self.template_name, {'form': form_instance, 'result':emi})

class MileageView(View):
     
    template_name = "mileage.html"

    form_class = MileageForm

    def get(self,request,*args,**kwargs):
         
        form_instance = self.form_class()

        return render(request,self.template_name,{"form":form_instance})    
    
class SignupView(View):

     template_name = 'signup.html'

     form_class = SignupForm

     def get(self,request,*args,**kwargs):

          form_instance = self.form_class()

          return render (request,self.template_name,{'form':form_instance}) 

class RegistrationView(View):

    template_name = "register.html"

    form_class = RegistrationForm

    def get(self,request,*args,**kwargs):

        form_instance = self.form_class()

        return render(request,self.template_name,{'form':form_instance})


