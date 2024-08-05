from django import forms

class ArticleForm(forms.Form):
	title = forms.CharField()
	content = forms.CharField()

	def clean_title(self):
		cleaned_data = self.cleaned_data
		print(cleaned_data)
		title = cleaned_data.get("title")
		print("Title is ", title)
		return title

	def clean(self):
		cleaned_data = self.cleaned_data
		print("Cleaned data is ", cleaned_data)
		return cleaned_data