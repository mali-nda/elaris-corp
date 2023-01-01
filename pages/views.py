from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
import datetime
from django.views import View
from django.core.mail import send_mail

from solutions.models import *
from contact.models import *
from pages.models import *

from pages.forms import *
from contact.forms import *
from django.conf import settings

# Create your views here.


class HomeView(View):
	template_name = 'index.html'
	queryset = Solution.objects.all()
	jobs = Job.objects.all()

	def get_queryset(self):
		return self.queryset

	def get_job(self):
		return self.jobs

	def get(self, request):
		context = {
			'solutions': self.get_queryset(),
			'jobs': self.get_job(),
		}

		return render(request, self.template_name, context)


class SolutionView(View):
	template_name = 'solutions.html'
	queryset = Solution.objects.all()

	def get_queryset(self):
		return self.queryset

	def get(self, request):
		context = {
		'solutions': self.get_queryset(),
		}

		return render(request, self.template_name, context)

class AboutView(View):
		template = 'about.html'
		queryset = Employee.objects.all()

		def get_queryset(self):
			return self.queryset

		def get(self, request):
			context = {
				'employees': self.get_queryset(),
			}

			return render(request, self.template, context)


class ContactView(View):
	template_name = 'contact.html'

	def get(self, request):
		form = ContactUsForm()

		context = {
			'form': form,
		}

		return render(request, self.template_name, context)

	def post(self, request):
		form = ContactUsForm(request.POST)

		if request.method == 'POST':
			if form.is_valid():
				form.save()
				subject = 'Contact Us'
				body = {
					'first_name': form.cleaned_data['first_name'], 
	                'last_name': form.cleaned_data['last_name'], 
	                'email': form.cleaned_data['email'], 
	                'details': form.cleaned_data['details'],
				}
				message = "\n".join(body.values())
				# send_mail(subject, message, 'eavhshelumiel@gmail.com', ['eavshelumiel@gmail.com'])
				send_mail(

					subject=subject,
					message=message,
					from_email=settings.EMAIL_HOST_USER,
					recipient_list=['contactelaris@zohomail.com'],
					fail_silently=False
				)
				form = ContactUsForm()
			else:
				form = ContactUsForm()
		else:
			form = ContactUsForm()

		context = {
			'form': form,
		}

		return redirect(thanks)


def thanks(request):
	template = 'thanks.html'
	context = {}

	return render(request, template, context)


def thanks2(request):
	template = 'thanks2.html'
	context = {}

	return render(request, template, context)


def joinus(request):
	template = 'joinus.html'
	jobs = Job.objects.all().order_by('-creation_date')
	context = {
		'jobs': jobs
	}

	return render(request, template, context)


def job_apply(request, myid):
	form = JobDetailForm(request.POST, request.FILES)
	print('hello')
	if request.method == "POST":
		print(request.FILES['resume'])
		applicant_name = request.POST['applicant_name']
		applicant_phone = request.POST['applicant_phone']
		applicant_email = request.POST['applicant_phone']
		resume = request.FILES['resume']
		company = 'ELARIS'
		job_id = myid
		apply_date = datetime.date.today()

		applicant = Application()
		applicant.company = company
		applicant.applicant_email = applicant_email
		applicant.applicant_name = applicant_name
		applicant.applicant_phone = applicant_phone
		applicant.apply_date = apply_date
		applicant.job_id = job_id
		applicant.resume = resume
		applicant.save()
		print(applicant)
		return redirect(thanks2)


def job_detail(request, myid):
	job = Job.objects.get(id=myid)
	description = job.description
	form = JobDetailForm()
	return render(request, "job_detail.html", {'job': job, 'description': description, 'form': form})


def technology_partners(request):
	template = 'technology_partners.html'
	context = {}

	return render(request, template, context)
