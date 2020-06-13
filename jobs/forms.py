from django import forms

class JobApplicationForm(forms.Form):
    EMPLOYMENT_TYPES = (
        (None, '--Please Choose--'),
        ('ft', 'Full Time'),
        ('pt', 'Part Time'),
        ('contract', 'Contract Work')
    )
    DAYS = (
        ('1', 'MON'),
        ('2', 'TUE'),
        ('3', 'WED'),
        ('4', 'THU'),
        ('5', 'FRI')
    )
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    website = forms.URLField(required=False)
    employment_type = forms.ChoiceField(choices=EMPLOYMENT_TYPES)
    start_date = forms.DateField(help_text="The earliest day you can start.")
    available_days = forms.MultipleChoiceField(choices=DAYS, help_text="Select all the days that you can work.")
    desired_hourly_wage = forms.DecimalField()
    cover_letter = forms.CharField()
    confirmation = forms.BooleanField(label='I certify that the information I have provided is true.')