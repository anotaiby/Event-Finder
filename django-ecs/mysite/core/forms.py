from django import forms


class NameForm(forms.Form):

    title = forms.CharField(label='title', max_length=200, widget=forms.TextInput(
        attrs={'placeholder': 'Enter the name of the event'}))
    time = forms.DateTimeField(
        input_formats=['%Y-%m-%d %H:%M:%S'], help_text='eg: 2021-10-25 14:30:00')
    venue = forms.CharField(label='venue', max_length=200, widget=forms.TextInput(
        attrs={'placeholder': 'Where is the event happening'}))
    desc = forms.CharField(label='desc', max_length=200, widget=forms.TextInput(
        attrs={'placeholder': 'Describe the event here'}))
    contact = forms.CharField(label='contact', max_length=200, widget=forms.TextInput(
        attrs={'placeholder': 'Describe the event here'}))
    image = forms.ImageField(label='Event Poster')
