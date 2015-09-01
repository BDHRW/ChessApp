from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm

from .mixin import LoginRequiredMixin


class ProfileView(LoginRequiredMixin, FormView):
    template_name = 'chess/profile.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('Chess:index')

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        return context

    def get_form_kwargs(self):
        """ our form requires a valid user
        """
        kwargs = super(ProfileView, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user,
        })

        return kwargs

    def form_valid(self, form):
        form.save()
        username = self.request.user.username
        password = self.request.POST['new_password2']
        # authenticate the user to login on registration
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super(ProfileView, self).form_valid(form)
