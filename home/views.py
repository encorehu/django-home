from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class LoginRequiredMixin(object):
    '''usage: make sure LoginRequiredMixin comes first.

    #right:
    class YourNeedLoginView(LoginRequiredMixin, TemplateView):
        template_name = 'index.html'

    #wrong:
    class YourNeedLoginView(TemplateView, LoginRequiredMixin):
        template_name = 'index.html'
    '''
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)
