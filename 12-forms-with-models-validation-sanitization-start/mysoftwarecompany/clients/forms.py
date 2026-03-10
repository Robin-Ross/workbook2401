from django import forms
from .models import Company
<<<<<<< HEAD

from .models import Company, Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email',
                  'company', 'role'
                  ]
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        if Employee.objects.filter(email=email).exists():
            raise forms.ValidationError("An employee with this email already exists.")
        name = cleaned_data.get('name', '')
        description = cleaned_data.get('description', '')
        forbidden_words = ['spam', 'fake', 'scam']
        for word in forbidden_words:
            if word in description.lower() or word in name.lower():
                raise forms.ValidationError(f"The employee contains a forbidden word: {word}")
        return cleaned_data

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'email', 'description']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError("Company name must be at least 3 characters long.")
        return name

    def clean(self):
        # note the line below calls the parent class's clean method to get the cleaned data remember this is from inheritence.
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        # we can search our database
        if Company.objects.filter(email=email).exists():
            raise forms.ValidationError("A company with this email already exists.")
            # note you can also use `self.add_error('email', 'A company with this email already exists.')` to add the error to a specific field instead of the whole form.

        # check for banned words.
        name = cleaned_data.get('name', '')
        description = cleaned_data.get('description', '')
        forbidden_words = ['spam', 'fake', 'scam']
        for word in forbidden_words:
            if word in description.lower() or word in name.lower():
                raise forms.ValidationError(f"The company contains a forbidden word: {word}")

        return cleaned_data
=======
>>>>>>> cfb8630c2034e3dd0bffcd76c27b4b0c6dc1aeeb

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    # Custom validation for the name field
    # the <fieldname> method is used to add custom validation to a field.
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name and len(name) < 2:
            # this will raise an validation error if the name is less than 2 characters long.
            raise forms.ValidationError("Name must be at least 2 characters long.")
        return name

    # Custom validation for the message field
    def clean_message(self):
        message = self.cleaned_data.get('message')
        if message and len(message) < 10:
            raise forms.ValidationError("Message must be at least 10 characters long.")
        return message
    
class CompanyForm(forms.ModelForm):
    # inner Meta class tell django which model to use and which fields to include
    class Meta:
        model = Company
        fields = ['name', 'email', 'description']
    
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError("Company name must be at least 3 characters long.")
        return name
    
    def clean(self):
        # the line below calls the parents class's clean method to get the cleaned data
        # remember this is from inheritence
        # also remember it is super clean!
        cleaned_data = super().clean()
        email = cleaned_data.get('email')

        if Company.objects.filter(email=email).exists():
            # raise forms.ValidationError("A company with this email already exists.")
            self.add_error('email', 'A company with this email already exists.')

        name = cleaned_data.get('name')
        description = cleaned_data.get('description')
        forbidden_words = ['spam', 'fake', 'scam']
        for word in forbidden_words:
            if description and word in description.lower() or name and word in name.lower():
                raise forms.ValidationError(f"The company contains a forbidden word: {word}")
            
        return cleaned_data