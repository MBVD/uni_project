from django import forms

class SearchForm(forms.Form):
    text = forms.CharField(label="", max_length=256, widget=forms.TextInput(attrs={"class": "form-control form-control-dark text-bg-dark", 
                                                                                   "type": "search",
                                                                                   "placeholder": "Поиск...",
                                                                                   "aria-label": "Search"}), required=False)
