from django.shortcuts import render
from django.contrib import messages
from django.views import generic

from .models import (
    UserProfile,
    Blog,
    Portfolio,
    Testimonial,
    Certificate,
)

from .forms import ContactForm


class IndexView(generic.TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["testimonials"] = Testimonial.objects.filter(is_active=True)
        context["certificates"] = Certificate.objects.filter(is_active=True)
        context["blogs"] = Blog.objects.filter(is_active=True)
        context["portfolio"] = Portfolio.objects.filter(is_active=True)
        return context
    


def update_avatar(request):
	user_profile = UserProfile.objects.get(user=request.user)
	user_profile.avatar_url = 'https://easy-peasy.ai/cdn-cgi/image/quality=80,format=auto,width=700/https://fdczvxmwwjwpwbeeqcth.supabase.co/storage/v1/object/public/images/50dab922-5d48-4c6b-8725-7fd0755d9334/3a3f2d35-8167-4708-9ef0-bdaa980989f9.png'
	user_profile.save()
	return render(request, 'profile.html', {'profile': user_profile})


class ContactView(generic.FormView):
    template_name = "main/contact.html"
    form_class = ContactForm
    success_url = "/contact/"

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Thank you. We will be in touch soon.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There was an error in your submission. Please try again.")
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
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = "main/blog-detail.html"
    