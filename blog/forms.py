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
                               

class AddPostForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    heading = forms.CharField(label='Heading', max_length=500)
    url = forms.CharField(label='Url', max_length=100)
    paragraph = forms.CharField(label='Paragraph',\
                               widget=forms.Textarea, max_length=1000)
    
    
    
    
