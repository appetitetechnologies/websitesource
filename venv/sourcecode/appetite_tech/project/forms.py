from .models import Project
from django import forms

class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('category',
                  'title',
                  'abstract',
                  'cid',
                  'abstract_pdf',
                  )