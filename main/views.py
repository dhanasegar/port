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


class IndexView(generic.TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        testimonials = Testimonial.objects.filter(is_active=True)
        certificates = Certificate.objects.filter(is_active=True)
        blogs = Blog.objects.filter(is_active=True)
        portfolio = Portfolio.objects.filter(is_active=True)
        
        # List of external image URLs corresponding to the testimonials
        external_urls = [
                 'https://upload.wikimedia.org/wikipedia/en/thumb/8/8c/CSUNS.svg/800px-CSUNS.svg.png',
				'https://ouc.howard.edu/sites/ouc.howard.edu/files/styles/large/public/2024-06/howardu_clocktower_logo.png?itok=2BF477uO',
				'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0Jhk8UKRvnSzsGESJKo2mbgwhVW3S1wvn4VO-Kn8&usqp=CAE&s',
				'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/The_University_of_California_Davis.svg/800px-The_University_of_California_Davis.svg.png',
				'https://cdn.gathertales.com/images/stories/main/43872cd4-2552-404b-a920-eb990fe7728f.webp',
				'https://cdn.gathertales.com/images/stories/main/43872cd4-2552-404b-a920-eb990fe7728f.webp',
				'https://cdn.gathertales.com/images/stories/main/43872cd4-2552-404b-a920-eb990fe7728f.webp',
				]

        context["testimonials"] = testimonials
        context["certificates"] = certificates
        context["blogs"] = blogs
        context["portfolio"] = portfolio
        context["external_urls"] = external_urls  # Pass external image URLs to the template

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
	paginate_by = 10
	
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class BlogDetailView(generic.DetailView):
	model = Blog
	template_name = "main/blog-detail.html"

# def my_view(request):
#     testimonials = Testimonial.objects.all()
#     external_urls = [
#         'https://upload.wikimedia.org/wikipedia/en/thumb/8/8c/CSUNS.svg/800px-CSUNS.svg.png',
#         'https://ouc.howard.edu/sites/ouc.howard.edu/files/styles/large/public/2024-06/howardu_clocktower_logo.png?itok=2BF477uO',
#         'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0Jhk8UKRvnSzsGESJKo2mbgwhVW3S1wvn4VO-Kn8&usqp=CAE&s',
#         'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/The_University_of_California_Davis.svg/800px-The_University_of_California_Davis.svg.png',
#         'https://cdn.gathertales.com/images/stories/main/43872cd4-2552-404b-a920-eb990fe7728f.webp',
#         'https://cdn.gathertales.com/images/stories/main/43872cd4-2552-404b-a920-eb990fe7728f.webp',
#     ]
#     context = {
#         'testimonials': testimonials,
#         'external_urls': external_urls,
#     }
#     return render(request, 'index.html', context)

