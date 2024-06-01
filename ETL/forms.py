# forms.py
from django import forms



# class MultipleFileInput(forms.ClearableFileInput):
#     allow_multiple_selected = True


# class MultipleFileField(forms.FileField):
#     def __init__(self, *args, **kwargs):
#         kwargs.setdefault("widget", MultipleFileInput())
#         super().__init__(*args, **kwargs)

#     def clean(self, data, initial=None):
#         single_file_clean = super().clean
#         if isinstance(data, (list, tuple)):
#             result = [single_file_clean(d, initial) for d in data]
#         else:
#             result = [single_file_clean(data, initial)]
#         return result


# class FileFieldForm(forms.Form):
#     file_field = MultipleFileField()




#  Itteration 2 by perplexity 

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    widget = MultipleFileInput()
    default_validators = []

    def to_python(self, value):
        if not value:
            return []
        elif isinstance(value, list):
            return [super(MultipleFileField, self).to_python(v) for v in value]
        else:
            return [super(MultipleFileField, self).to_python(value)]

class FileFieldForm(forms.Form):
    file_field = MultipleFileField(required=True)
    job_title = forms.CharField(required=True)
    job_description = forms.CharField(widget=forms.Textarea, required=False)
    job_description_file = forms.FileField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        job_title = cleaned_data.get('job_title')
        job_description = cleaned_data.get('job_description')
        job_description_file = cleaned_data.get('job_description_file')
        file_field = cleaned_data.get('file_field')

        if not job_title:
            self.add_error('job_title', 'Job title is required.')

        if not file_field:
            self.add_error('file_field', 'At least one CV file is required.')

        if not job_description and not job_description_file:
            raise forms.ValidationError('Either job description text or job description file is required.')

        if job_description and not job_title:
            raise forms.ValidationError('Job title is required when providing a text description.')

        return cleaned_data