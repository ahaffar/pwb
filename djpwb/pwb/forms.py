from django import forms
from django.forms.util import ErrorList 
from django.utils.safestring import mark_safe

class ContactsForm(forms.Form):
	subject = forms.CharField(help_text='A valid email address, please.',widget=forms.TextInput(attrs={'class':'input-xxlarge'}))
	message = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'class':'input-xxlarge'}), label='Message', error_messages={'required':'Please enter a descriptive text which descripe your Problem'})
	email = forms.EmailField(required=False, label='Email', widget=forms.TextInput(attrs={'class':'input-xxlarge'}))


class DivErrorList(ErrorList):
     def __unicode__(self):
         return self.as_divs()
     def as_divs(self):
         if not self: return u''
         return mark_safe('<div class="errorlist">%s</div>' % ''.join([u'<div class="error">%s</div>' % e for e in self]))


#------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------#
class complain(forms.Form):
	username = forms.CharField()
	subject = forms.CharField(max_length=30)
	email = forms.CharField(required=False)
	msg = forms.CharField(max_length=2000)

