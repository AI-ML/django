from django import forms

class ContactForm(forms.Form):
    your_name = forms.CharField(label='Name', max_length=100)
    your_email = forms.EmailField(label='Email')
    your_message = forms.CharField(label='Message',\
                                widget=forms.Textarea, max_length=5000)


class CommentForm(forms.Form):
    your_name = forms.CharField(label='Name', max_length=100)
    your_email = forms.EmailField(label='Email')
    your_comment = forms.CharField(label='Comment',\
                               widget=forms.Textarea, max_length=1000)
