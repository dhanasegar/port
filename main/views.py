from django.shortcuts import render
from django.contrib import messages
from .models import (
    UserProfile,
    Blog,
    Portfolio,
    Testimonial,
    Certificate,
    SocialMediaLink)
from django.views import generic
from .forms import ContactForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import SocialMediaLink  # Assuming you have a model for social links

from django.shortcuts import render
from main.models import SocialMediaLink

# def footer_view(request):
#     # Fetch the first SocialMediaLink record
#     social_media = SocialMediaLink.objects.get()

#     # Print the entire social_media object
#     print(social_media)

#     # Print individual fields to see the values
#     print("Facebook URL:", social_media.fb)
#     print("Instagram URL:", social_media.ig)
#     print("Twitter URL:", social_media.tw)
#     print("LinkedIn URL:", social_media.li)

#     # Render the template and pass the social_media data
#     return render(request, 'main/partials/footer.html', {'social_media': social_media})

def footer_view(request):
    # Fetch the first social media link record from the database
    social_media = SocialMediaLink.objects.first()

    # Pass the data to the template using the context dictionary
    context = {
        'social_media': social_media
    }

    return render(request, 'base.html', context)



class IndexView(generic.TemplateView):
	template_name = "main/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		testimonials = Testimonial.objects.filter(is_active=True)
		certificates = Certificate.objects.filter(is_active=True)
		blogs = Blog.objects.filter(is_active=True)
		portfolio = Portfolio.objects.filter(is_active=True)
		
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
    userprofile = get_object_or_404(UserProfile, id=user_id)
    if userprofile.cv_binary:
       
        response = HttpResponse(userprofile.cv_binary, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{userprofile.user.first_name}_resume.pdf"'
        return response
    return HttpResponse("Resume not found.", status=404)
