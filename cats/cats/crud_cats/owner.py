from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class OwnerCreateView(LoginRequiredMixin, CreateView):
	"""
	Sub-class of the CreateView to automatically pass the request
	to the form and add the owner to the saved object.
	"""

	def form_valid(self, form):
		print('form_valid called')
		object = form.save(commit=False)
		object.owner = self.request.user
		object.save()
		return super(OwnerCreateView, self).form_valid(form)



class OwnerUpdateView(LoginRequiredMixin, UpdateView):
	msg = 'Update get_queryset called'
	def get_queryset(self):
		print(self.msg)
		qs = super(OwnerUpdateView, self).get_queryset()
		return qs.filter(owner=self.request.user)


class OwnerDeleteView(LoginRequiredMixin, DeleteView):
	msg = 'Delete get_queryset called'
	def get_queryset(self):
		print(self.msg)
		qs = super(OwnerDeleteView, self).get_queryset()
		return qs.filter(owner=self.request.user)