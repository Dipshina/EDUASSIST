from django import forms # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore
from django.core.exceptions import ValidationError # type: ignore
from django.core.validators import RegexValidator # type: ignore
from .models import Note, Profile, TODO

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        validators=[
            RegexValidator(
                regex=r'^(?!\d+$)[A-Za-z0-9_]{3,30}$',
                message='Username must be alphanumeric, 3 to 30 characters long, and cannot be numeric-only.'
            )
        ],
        error_messages={'required': 'Please provide a username.'}
    )
    email = forms.EmailField(
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
                message='Enter a valid email address.'
            )
        ]
    )
    first_name = forms.CharField(
        max_length=30, 
        required=False,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z\- ]{1,50}$',
                message='First name should only contain alphabetic characters, spaces, or hyphens, and be 1 to 50 characters long.'
            )
        ]
    )
    last_name = forms.CharField(
        max_length=30, 
        required=False,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z\- ]{1,50}$',
                message='Last name should only contain alphabetic characters, spaces, or hyphens, and be 1 to 50 characters long.'
            )
        ]
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        validators=[
            RegexValidator(
                regex=r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$',
                message='Password must be at least 8 characters long and include at least one uppercase letter, one lowercase letter, one number, and one special character.'
            )
        ],
        error_messages={'required': 'Please provide a password.'}
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput,
        error_messages={
            'required': 'Please confirm your password.',
            'password_mismatch': 'The two password fields didn’t match.',
        }
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        # Remove help texts for specific fields
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        
        # Customize placeholders
        self.fields['password1'].widget.attrs.update({'placeholder': 'Enter your password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm your password'})

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists.")
        return email



class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']  

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class TODOForm(forms.ModelForm):
    class Meta:
        model = TODO
        fields = ['title', 'description', 'status', 'priority', 'due_date']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter task description here...'})
        }

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter note content here...'})
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError("Please enter a title.")
        return title