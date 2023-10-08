from django import forms
from .models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
        model=TaskModel
        fields=['title', 'description','due_date','priority', 'taskimage']
        labels={'title':'Title', 'description':'Description','due_date':'Due Date', 'priority':'Priority','taskimage':'Image'}
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control', 'rows':'3'}),
            'due_date':forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
            'priority':forms.Select(attrs={'class':'form-control'}),
    
        }
