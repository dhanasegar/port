from django.shortcuts import render, redirect, get_object_or_404
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
        
        # Adding additional context for empty states (optional)
        context["has_testimonials"] = context["testimonials"].exists()
        context["has_certificates"] = context["certificates"].exists()
        context["has_blogs"] = context["blogs"].exists()
        context["has_portfolio"] = context["portfolio"].exists()

        return context


def update_avatar(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        user_profile.avatar_url = 'https://easy-peasy.ai/cdn-cgi/image/quality=80,format=auto,width=700/https://fdczvxmwwjwpwbeeqcth.supabase.co/storage/v1/object/public/images/50dab922-5d48-4c6b-8725-7fd0755d9334/3a3f2d35-8167-4708-9ef0-bdaa980989f9.png'
        user_profile.save()
        messages.success(request, "Your avatar has been updated successfully!")
    except UserProfile.DoesNotExist:
        messages.error(request, "User profile not found.")
        return redirect('profile')  # You can redirect to a profile page or a fallback

    return redirect('profile')  # Redirect to the profile page after successful update


class ContactView(generic.FormView):
    template_name = "main/contact.html"
    form_class = ContactForm
    success_url = "/contact/"

    def form_valid(self, form):
        try:
            form.save()
            messages.success(self.request, "Thank you. We will be in touch soon.")
        except Exception as e:
            messages.error(self.request, f"An error occurred: {e}")
            return super().form_invalid(form)
        
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There was an error in your submission. Please try again.")
        return super().form_invalid(form)


class PortfolioView(generic.ListView):
    model = Portfolio
    template_name = "main/portfolio.html"
    paginate_by = 10
    context_object_name = 'portfolios'  # Custom name for the context variable

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    template_name = "main/portfolio-detail.html"


class BlogView(generic.ListView):
    model = Blog
    template_name = "main/blog.html"
    paginate_by = 10
    context_object_name = 'blogs'  # Custom name for the context variable

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = "main/blog-detail.html"
