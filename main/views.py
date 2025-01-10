from django.shortcuts import render
from django.contrib import messages
from .models import (
		UserProfile,
		Blog,
		Portfolio,
		Testimonial,
		Certificate,
	)
from django.views import generic
from . forms import ContactForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import UserProfile

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class IndexView(generic.TemplateView):
    template_name = "main/index.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        userprofile = None

        # Fetch the UserProfile instance if the user is logged in
        if self.request.user.is_authenticated:
            try:
                userprofile = UserProfile.objects.get(user=self.request.user)
            except UserProfile.DoesNotExist:
                pass  # Handle the case where a UserProfile does not exist

        testimonials = Testimonial.objects.filter(is_active=True)
        certificates = Certificate.objects.filter(is_active=True)
        blogs = Blog.objects.filter(is_active=True)
        portfolio = Portfolio.objects.filter(is_active=True)

     

        context["userprofile"] = userprofile  # Add user profile to context
        context["testimonials"] = testimonials
        context["certificates"] = certificates
        context["blogs"] = blogs
        context["portfolio"] = portfolio
       

        return context



class ContactView(generic.FormView):
	template_name = "main/contact.html"
	form_class = ContactForm
	success_url = "/contact/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Thank you. We will be in touch soon.')
		return super().form_valid(form)
	def form_invalid(self, form):
		messages.error(self.request, 'There was an error in your submission. Please try again.')
		return super().form_invalid(form)


class PortfolioView(generic.ListView):
	model = Portfolio
	template_name = "main/portfolio.html"
	paginate_by = 10

	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class PortfolioDetailView(generic.DetailView):
	model = Portfolio
	template_name = "main/portfolio-detail.html"

class BlogView(generic.ListView):
	model = Blog
	template_name = "main/blog.html"
	paginate_by = 12
	
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class BlogDetailView(generic.DetailView):
	model = Blog
	template_name = "main/blog-detail.html"


def download_resume(request, user_id):
# def download_cv(request, user_id):
    userprofile = get_object_or_404(UserProfile, id=user_id)
    if userprofile.cv_binary:
        response = HttpResponse(userprofile.cv_binary, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{userprofile.user.first_name}_resume.pdf"'
        return response
    return HttpResponse("Resume not found.", status=404)
