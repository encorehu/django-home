from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView

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

class HomeView(TemplateView):
    template_name = 'home/index.html'

class RootTextView(TemplateView):
    """
    A simple view with mimetype text/plain
    """
    mimetype='text/plain'
    template_name = 'home/%(filename)s.txt'
    allowed_txtfiles =['home/robots.txt','home/authors.txt','home/google_verify_file.txt']

    def render_to_response(self, context, **kwargs):

        self.template_name = self.template_name % context['params']

        if self.template_name not in self.allowed_txtfiles:
            return RedirectView.as_view(url='/')
        else:
            return super(RootTextView, self).render_to_response(
                context,
                content_type='text/plain',
                **kwargs
            )
