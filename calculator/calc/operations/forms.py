from django import forms

class BmiForm(forms.Form):

    height = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))

    weight = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))

class BmrForm(forms.Form):

    
    height = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))

    weight = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))

    age = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))

    gender_choices = (
        ("male","male"),
        ("female","female")
    )

    gender = forms.ChoiceField(choices=gender_choices,widget=forms.Select(attrs={"class":"form-control form-select mb-3"}))

    activity_choices = (
        (1.2,"sedentary"),
         (1.375,"lightly active"),
         (1.55,"moderately active"),
         (1.725,"very active"),
         (1.9,"extra active"),
    )

    activity = forms.ChoiceField(choices=activity_choices,widget=forms.Select(attrs={"class":"form-control form-select mb-3"}))

class EmiForm(forms.Form):

    loan = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))

    interest = forms.FloatField(widget=forms.NumberInput(attrs={"class":"form-control"}))

    tenure = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))

class WeightManagementForm(BmrForm):

    mode_choices = (
        ("gain","gain"),
        ("loss","loss"),
    )

    mode = forms.ChoiceField(choices = mode_choices,widget=forms.NumberInput(attrs={"class":"form-control"}))

    duration = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))

    target_weight = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))

class MileageForm(forms.Form):


    distance = forms.FloatField(widget=forms.NumberInput(attrs={"class":"form-control"}))

    fuel = forms.FloatField(widget=forms.NumberInput(attrs={"class":"form-control"}))

class SignupForm(forms.Form):

    first_name = forms.CharField(widget=forms.TextInput(attrs={"class" : "form-control mb-2"}))

    last_name = forms.CharField(widget=forms.TextInput(attrs={"class" : "form-control mb-2"}))

    email = forms.CharField(widget=forms.EmailInput(attrs={"class" : "form-control mb-2"}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={"class" : "form-control mb-2"}))

class RegistrationForm(forms.Form):

    first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    address = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","row":3}))

    city = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    pincode = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    email = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    phone = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    recommendation_choices = (
        ("social media","social media"),
        ("friends","friends"),
        ("on-site","on-site")
    )

    recommendation = forms.ChoiceField(label = "How did you hear about us?",
                                        choices=recommendation_choices,
                                        widget=forms.Select(attrs={"class":"form-control"}))

    other = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    feedback = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","rows":3}))

    suggestion = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    rec_choices = (
        ("yes","Yes"),
        ("maybe","Maybe"),
        ("no","No")
    )

    recommendation_options = forms.ChoiceField(widget=forms.RadioSelect,choices=rec_choices)