from django.contrib.auth import authenticate, login
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm

class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = "/"

    def form_valid(self, form):
        # save the user first
        form.save()
        # get the username and password
        username = self.request.POST['username']
        password = self.request.POST['password1']
        # authenticate the user to login on registration
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super(RegisterView, self).form_valid(form)
