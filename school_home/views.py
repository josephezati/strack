from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.views.generic import (
	ListView,
	DetailView,
	UpdateView,
	CreateView
	)

from .models import *



# class HomeView(DetailView):
# 	model = School
# 	template_name = "school_home/home.html"
# 	def get_context_data(self, **kwargs):
# 		context = super(HomeView, self).get_context_data(**kwargs)
# 		context['all_schools'] = School.objects.all().order_by('-id')
# 		all_regs = School.objects.values("region").annotate(Count("id"))
# 		context['all_resources'] = Resource.objects.all().order_by('-id')
# 		context['teachers'] = Teacher.objects.all().order_by('-id')[:10]
# 		context['deos'] = Deo.objects.all().order_by('-id')
# 		context['teacher_transfers'] = TransferTeacher.objects.all().order_by('-id')
# 		context['deo_transfers'] = TransferDeo.objects.all().order_by('-id')
# 		context['allocated_resources'] = AllocateResource.objects.all().order_by('-id')
		# return context

# School related views..................................................................................
# School related views..................................................................................

class SchoolListView(ListView):
	model = School
	context_object_name = 'schools'
	ordering = ['-id']

class SchoolDetailView(DetailView):
	model = School
	# request.session['sch_id'] = School.id

class SchoolCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
	raise_exception = True  # <<<---
	model = School
	fields =['name','motto','email','yr_est','regstatus','reg_no','yr_reg','cen_no',
	'cennostatus','yr_cnr','schtype','level','access','category','section',
	'ownership','district','region','logo']
	template_name = "school_home/school_form.html"
	def get_context_data(self, **kwargs):
		context = super(SchoolCreateView, self).get_context_data(**kwargs)
		page = self.request.GET.get('page')
		schools = Paginator(self.model.objects.all().order_by('-id'), 10)
		context["schools"] = schools.get_page(page)
		return context

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.save()
		return redirect('new-school')
	def test_func(self):
		if self.request.user.groups.values_list('id', flat=True).first() == 2:
			return True
		return False

class SchoolUpdateView(UpdateView):
	model = School
	fields =['name','motto','email','yr_est','regstatus','reg_no','yr_reg','cen_no',
	'cennostatus','yr_cnr','schtype','level','access','category','section',
	'ownership','district','region','logo']
	template_name = "school_home/school_form.html"
	def get_context_data(self, **kwargs):
		context = super(SchoolUpdateView, self).get_context_data(**kwargs)
		page = self.request.GET.get('page')
		schools = Paginator(self.model.objects.all().order_by('-id'), 10)
		context["schools"] = schools.get_page(page)
		return context

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.save()
		return redirect('new-school')

# Teacher related views..................................................................................
# Teacher related views..................................................................................

class TeacherCreateView(CreateView):
	model = Teacher
	fields =['name','reg_no','email','status','gender','date_registered','district','region','photo']
	def get_context_data(self, **kwargs):
		context = super(TeacherCreateView, self).get_context_data(**kwargs)
		page = self.request.GET.get('page')
		teachers = Paginator(self.model.objects.all().order_by('-id'), 10)
		context["teachers"] = teachers.get_page(page)
		return context

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.save()
		return redirect('new-teacher')

class TeacherUpdateView(UpdateView):
	model = Teacher
	fields =['name','reg_no','email','status','gender','date_registered','district','region','photo']
	def get_context_data(self, **kwargs):
		context = super(TeacherUpdateView, self).get_context_data(**kwargs)
		page = self.request.GET.get('page')
		teachers = Paginator(self.model.objects.all().order_by('-id'), 10)
		context["teachers"] = teachers.get_page(page)
		return context

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.save()
		return redirect('new-teacher')

class TeacherListView(ListView):
	model = Teacher
	context_object_name = 'teachers'
	ordering = ['-id']

class TeacherDetailView(DetailView):
	model = Teacher

class TeacherTransferListView(ListView):
	model = TransferTeacher
	context_object_name = 'teacher_transfers'
	ordering = ['-id']

class TransferTeacherCreateView(CreateView):
	model = TransferTeacher
	fields =['teacher','school','date_transfered','date_valid','designation']
	def get_context_data(self, **kwargs):
		context = super(TransferTeacherCreateView, self).get_context_data(**kwargs)
		page = self.request.GET.get('page')
		transfers = Paginator(self.model.objects.all().order_by('-id'), 10)
		context["transfers"] = transfers.get_page(page)
		return context

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.save()
		return redirect('transfer-teacher')

class TransferTeacherUpdateView(UpdateView):
	model = TransferTeacher
	fields =['teacher','school','date_transfered','date_valid','designation']
	def get_context_data(self, **kwargs):
		context = super(TransferTeacherUpdateView, self).get_context_data(**kwargs)
		page = self.request.GET.get('page')
		transfers = Paginator(self.model.objects.all().order_by('-id'), 10)
		context["transfers"] = transfers.get_page(page)
		return context

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.save()
		return redirect('transfer-teacher')


class DesignationCreateView(CreateView):
	model = Designation
	fields =['des_type']
	def get_context_data(self, **kwargs):
		context = super(DesignationCreateView, self).get_context_data(**kwargs)
		context["des"] = self.model.objects.all().order_by('-id')
		return context

	def form_valid(self, form):
		form.save()
		return redirect('designation')

class DesignationUpdateView(UpdateView):
	model = Designation
	fields =['des_type']
	def get_context_data(self, **kwargs):
		context = super(DesignationUpdateView, self).get_context_data(**kwargs)
		context["des"] = self.model.objects.all().order_by('-id')
		return context

	def form_valid(self, form):
		form.save()
		return redirect('designation')

# Deo related views..................................................................................
# Deo related views..................................................................................

class DeoCreateView(CreateView):
	model = Deo
	fields =['name','email','status','gender','district','region','photo']
	def get_context_data(self, **kwargs):
		context = super(DeoCreateView, self).get_context_data(**kwargs)
		page = self.request.GET.get('page')
		deos = Paginator(self.model.objects.all().order_by('-id'), 10)
		context["deos"] = deos.get_page(page)
		return context

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.save()
		return redirect('new-deo')

class DeoUpdateView(UpdateView):
	model = Deo
	fields =['name','email','status','gender','district','region','photo']
	def get_context_data(self, **kwargs):
		context = super(DeoUpdateView, self).get_context_data(**kwargs)
		page = self.request.GET.get('page')
		deos = Paginator(self.model.objects.all().order_by('-id'), 10)
		context["deos"] = deos.get_page(page)
		return context

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.save()
		return redirect('new-deo')

class DeoListView(ListView):
	model = Deo
	context_object_name = 'deos'
	ordering = ['-id']

class DeoDetailView(DetailView):
	model = Deo
	def get_context_data(self, **kwargs):
		context = super(DeoDetailView, self).get_context_data(**kwargs)
		context['deotransfers'] = TransferDeo.objects.filter(deo=self.object)
		return context

class TransferDeoCreateView(CreateView):
	model = TransferDeo
	fields =['deo','district','date_transfered','date_valid']
	def get_context_data(self, **kwargs):
		context = super(TransferDeoCreateView, self).get_context_data(**kwargs)
		page = self.request.GET.get('page')
		deotransfers = Paginator(self.model.objects.all().order_by('-id'), 10)
		context["deotransfers"] = deotransfers.get_page(page)
		return context

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.save()
		return redirect('transfer-deo')

class TransferDeoUpdateView(UpdateView):
	model = TransferDeo
	fields =['deo','district','date_transfered','date_valid']
	def get_context_data(self, **kwargs):
		context = super(TransferDeoUpdateView, self).get_context_data(**kwargs)
		page = self.request.GET.get('page')
		deotransfers = Paginator(self.model.objects.all().order_by('-id'), 10)
		context["deotransfers"] = deotransfers.get_page(page)
		return context

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.save()
		return redirect('transfer-deo')

# Fac related views..................................................................................
# Fac related views..................................................................................

class FacilityCreateView(CreateView):
	model = Facility
	fields =['facility_type','description','quantity','status','photo']
	template_name = "school_home/facility_form.html"
	def get_context_data(self, **kwargs):
		context = super(FacilityCreateView, self).get_context_data(**kwargs)
		context["facilities"] = self.model.objects.all().order_by('-id')
		return context

	def form_valid(self, form):
		form.instance.user = self.request.user
		# form.instance.school = self.request.session.get['sch_id']
		form.save()
		return HttpResponseRedirect("")
		# return redirect('new-facility')

# School settings related views..................................................................................
# School settings views..................................................................................

class OwnershipCreateView(CreateView):
	model = Ownership
	fields =['own_type']
	def get_context_data(self, **kwargs):
		context = super(OwnershipCreateView, self).get_context_data(**kwargs)
		context["own_types"] = self.model.objects.all().order_by('-id')
		return context
	def form_valid(self, form):
		if form.is_valid():
			form.save()
			return redirect('ownership')

class OwnershipUpdateView(UpdateView):
	model = Ownership
	fields =['own_type']
	def get_context_data(self, **kwargs):
		context = super(OwnershipUpdateView, self).get_context_data(**kwargs)
		context["own_types"] = self.model.objects.all().order_by('-id')
		return context
	def form_valid(self, form):
		if form.is_valid():
			form.save()
			return redirect('ownership')

class SectionCreateView(CreateView):
	model = Section
	fields =['sec_type']
	def get_context_data(self, **kwargs):
		context = super(SectionCreateView, self).get_context_data(**kwargs)
		context["sec_types"] = self.model.objects.all().order_by('-id')
		return context
	def form_valid(self, form):
		if form.is_valid():
			form.save()
			return redirect('section')

class SectionUpdateView(UpdateView):
	model = Section
	fields =['sec_type']
	def get_context_data(self, **kwargs):
		context = super(SectionUpdateView, self).get_context_data(**kwargs)
		context["sec_types"] = self.model.objects.all().order_by('-id')
		return context
	def form_valid(self, form):
		if form.is_valid():
			form.save()
			return redirect('section')

class CategoryCreateView(CreateView):
	model = Category
	fields =['cat_type']
	def get_context_data(self, **kwargs):
		context = super(CategoryCreateView, self).get_context_data(**kwargs)
		context["cat_types"] = self.model.objects.all().order_by('-id')
		return context
	def form_valid(self, form):
		if form.is_valid():
			form.save()
			return redirect('category')

class CategoryUpdateView(UpdateView):
	model = Category
	fields =['cat_type']
	def get_context_data(self, **kwargs):
		context = super(CategoryUpdateView, self).get_context_data(**kwargs)
		context["cat_types"] = self.model.objects.all().order_by('-id')
		return context
	def form_valid(self, form):
		if form.is_valid():
			form.save()
			return redirect('category')

class LevelCreateView(CreateView):
	model = Level
	fields =['lev_name']
	def get_context_data(self, **kwargs):
		context = super(LevelCreateView, self).get_context_data(**kwargs)
		context["levels"] = self.model.objects.all().order_by('-id')
		return context
	def form_valid(self, form):
		if form.is_valid():
			form.save()
			return redirect('level')

class LevelUpdateView(UpdateView):
	model = Level
	fields =['lev_name']
	def get_context_data(self, **kwargs):
		context = super(LevelUpdateView, self).get_context_data(**kwargs)
		context["levels"] = self.model.objects.all().order_by('-id')
		return context
	def form_valid(self, form):
		if form.is_valid():
			form.save()
			return redirect('level')

class AccessCreateView(CreateView):
	model = Access
	fields =['acc_type']
	def get_context_data(self, **kwargs):
		context = super(AccessCreateView, self).get_context_data(**kwargs)
		context["acc_types"] = self.model.objects.all().order_by('-id')
		return context
	def form_valid(self, form):
		if form.is_valid():
			form.save()
			return redirect('access')

class AccessUpdateView(UpdateView):
	model = Access
	fields =['acc_type']
	def get_context_data(self, **kwargs):
		context = super(AccessUpdateView, self).get_context_data(**kwargs)
		context["acc_types"] = self.model.objects.all().order_by('-id')
		return context
	def form_valid(self, form):
		if form.is_valid():
			form.save()
			return redirect('access')

class RegstatusCreateView(CreateView):
	model = Regstatus
	fields =['rs_type']
	def get_context_data(self, **kwargs):
		context = super(RegstatusCreateView, self).get_context_data(**kwargs)
		context["rs_types"] = self.model.objects.all().order_by('-id')
		return context
	def form_valid(self, form):
		if form.is_valid():
			form.save()
			return redirect('regstatus')

class RegstatusUpdateView(UpdateView):
	model = Regstatus
	fields =['rs_type']
	def get_context_data(self, **kwargs):
		context = super(RegstatusUpdateView, self).get_context_data(**kwargs)
		context["rs_types"] = self.model.objects.all().order_by('-id')
		return context
	def form_valid(self, form):
		if form.is_valid():
			form.save()
			return redirect('regstatus')

class CennostatusCreateView(CreateView):
	model = Cennostatus
	fields =['cns']
	def get_context_data(self, **kwargs):
		context = super(CennostatusCreateView, self).get_context_data(**kwargs)
		context["statuses"] = self.model.objects.all().order_by('-id')
		return context
	def form_valid(self, form):
		if form.is_valid():
			form.save()
			return redirect('cennostatus')

class CennostatusUpdateView(UpdateView):
	model = Cennostatus
	fields =['cns']
	def get_context_data(self, **kwargs):
		context = super(CennostatusUpdateView, self).get_context_data(**kwargs)
		context["statuses"] = self.model.objects.all().order_by('-id')
		return context
	def form_valid(self, form):
		if form.is_valid():
			form.save()
			return redirect('cennostatus')

class SchtypeCreateView(CreateView):
	model = Schtype
	fields =['sch_type']
	def get_context_data(self, **kwargs):
		context = super(SchtypeCreateView, self).get_context_data(**kwargs)
		context["types"] = self.model.objects.all().order_by('-id')
		return context
	def form_valid(self, form):
		if form.is_valid():
			form.save()
			return redirect('schtype')

class SchtypeUpdateView(UpdateView):
	model = Schtype
	fields =['sch_type']
	def get_context_data(self, **kwargs):
		context = super(SchtypeUpdateView, self).get_context_data(**kwargs)
		context["types"] = self.model.objects.all().order_by('-id')
		return context
	def form_valid(self, form):
		if form.is_valid():
			form.save()
			return redirect('schtype')

class DistrictCreateView(CreateView):
	model = District
	fields =['dis_name']
	def get_context_data(self, **kwargs):
		context = super(DistrictCreateView, self).get_context_data(**kwargs)
		page = self.request.GET.get('page')
		districts = Paginator(self.model.objects.all().order_by('-id'), 10)
		context["districts"] = districts.get_page(page)
		return context
	def form_valid(self, form):
		if form.is_valid():
			form.save()
			return redirect('district')

class DistrictUpdateView(UpdateView):
	model = District
	fields =['dis_name']
	def get_context_data(self, **kwargs):
		context = super(DistrictUpdateView, self).get_context_data(**kwargs)
		page = self.request.GET.get('page')
		districts = Paginator(self.model.objects.all().order_by('-id'), 10)
		context["districts"] = districts.get_page(page)
		return context
	def form_valid(self, form):
		if form.is_valid():
			form.save()
			return redirect('district')

class RegionCreateView(CreateView):
	model = Region
	fields =['reg_name']
	def get_context_data(self, **kwargs):
		context = super(RegionCreateView, self).get_context_data(**kwargs)
		context["regions"] = self.model.objects.all().order_by('-id')
		return context
	def form_valid(self, form):
		if form.is_valid():
			form.save()
			return redirect('region')

class RegionUpdateView(UpdateView):
	model = Region
	fields =['reg_name']
	def get_context_data(self, **kwargs):
		context = super(RegionUpdateView, self).get_context_data(**kwargs)
		context["regions"] = self.model.objects.all().order_by('-id')
		return context
	def form_valid(self, form):
		if form.is_valid():
			form.save()
			return redirect('region')

# Fac settings related views..................................................................................
# Fac settings related views..................................................................................

class FacilityTypeView(CreateView):
    model = FacType
    fields =['facility_type']
    template_name = "school_home/facility_type_form.html"
    def get_context_data(self, **kwargs):
        context = super(FacilityTypeView, self).get_context_data(**kwargs)
        context["fac_types"] = self.model.objects.all().order_by('-id')
        return context
    def form_valid(self, form):
    	if form.is_valid():
    		form.save()
    		return redirect('factype')

class FacilityTypeUpdateView(UpdateView):
    model = FacType
    fields =['facility_type']
    template_name = "school_home/facility_type_form.html"
    def get_context_data(self, **kwargs):
        context = super(FacilityTypeUpdateView, self).get_context_data(**kwargs)
        context["fac_types"] = self.model.objects.all().order_by('-id')
        return context
    def form_valid(self, form):
    	if form.is_valid():
    		form.save()
    		return redirect('factype')

class FacilityStatusView(CreateView):
    model = FacStatus
    fields =['facility_status']
    template_name = "school_home/facility_status_form.html"
    def get_context_data(self, **kwargs):
        context = super(FacilityStatusView, self).get_context_data(**kwargs)
        context["statuses"] = self.model.objects.all().order_by('-id')
        return context
    def form_valid(self, form):
    	if form.is_valid():
    		form.save()
    		return redirect('facstatus')
    	
class FacilityStatusUpdateView(UpdateView):
    model = FacStatus
    fields =['facility_status']
    template_name = "school_home/facility_status_form.html"
    def get_context_data(self, **kwargs):
        context = super(FacilityStatusUpdateView, self).get_context_data(**kwargs)
        context["statuses"] = self.model.objects.all().order_by('-id')
        return context
    def form_valid(self, form):
    	if form.is_valid():
    		form.save()
    		return redirect('facstatus')

class TeacherStatusCreateView(CreateView):
    model = TeacherStatus
    fields =['teacher_status']
    def get_context_data(self, **kwargs):
        context = super(TeacherStatusCreateView, self).get_context_data(**kwargs)
        context["statuses"] = self.model.objects.all().order_by('-id')
        return context
    def form_valid(self, form):
    	if form.is_valid():
    		form.save()
    		return redirect('teacher-status')


# Teacher settings related views..................................................................................
# Teacher settings views..................................................................................

class TeacherStatusUpdateView(UpdateView):
    model = TeacherStatus
    fields =['teacher_status']
    def get_context_data(self, **kwargs):
        context = super(TeacherStatusUpdateView, self).get_context_data(**kwargs)
        context["statuses"] = self.model.objects.all().order_by('-id')
        return context
    def form_valid(self, form):
    	if form.is_valid():
    		form.save()
    		return redirect('teacher-status')

class GenderCreateView(CreateView):
    model = Gender
    fields =['gender']
    def get_context_data(self, **kwargs):
        context = super(GenderCreateView, self).get_context_data(**kwargs)
        context["gender_types"] = self.model.objects.all().order_by('-id')
        return context
    def form_valid(self, form):
    	if form.is_valid():
    		form.save()
    		return redirect('gender')

class GenderUpdateView(UpdateView):
    model = Gender
    fields =['gender']
    def get_context_data(self, **kwargs):
        context = super(GenderUpdateView, self).get_context_data(**kwargs)
        context["gender_types"] = self.model.objects.all().order_by('-id')
        return context
    def form_valid(self, form):
    	if form.is_valid():
    		form.save()
    		return redirect('gender')

# Resource related views..................................................................................
# Resource related views..................................................................................

class ResourceSourceCreateView(CreateView):
	model = ResourceSource
	fields =['resource_source']
	def get_context_data(self, **kwargs):
		context = super(ResourceSourceCreateView, self).get_context_data(**kwargs)
		page = self.request.GET.get('page')
		resource_sources = Paginator(self.model.objects.all().order_by('-id'), 10)
		context["resource_sources"] = resource_sources.get_page(page)
		return context
	def form_valid(self, form):
		if form.is_valid():
			form.save()
			return redirect('resource-source')

class ResourceSourceUpdateView(UpdateView):
	model = ResourceSource
	fields =['resource_source']
	def get_context_data(self, **kwargs):
		context = super(ResourceSourceUpdateView, self).get_context_data(**kwargs)
		page = self.request.GET.get('page')
		resource_sources = Paginator(self.model.objects.all().order_by('-id'), 10)
		context["resource_sources"] = resource_sources.get_page(page)
		return context
	def form_valid(self, form):
		if form.is_valid():
			form.save()
			return redirect('resource-source')

class ResourceListView(ListView):
	model = Resource
	context_object_name = 'resources'
	ordering = ['-id']

class ResourceTypeCreateView(CreateView):
    model = ResourceType
    fields =['resource_type']
    def get_context_data(self, **kwargs):
        context = super(ResourceTypeCreateView, self).get_context_data(**kwargs)
        context["resource_types"] = self.model.objects.all().order_by('-id')
        return context
    def form_valid(self, form):
    	if form.is_valid():
    		form.save()
    		return redirect('resource-type')

class ResourceTypeUpdateView(UpdateView):
    model = ResourceType
    fields =['resource_type']
    def get_context_data(self, **kwargs):
        context = super(ResourceTypeUpdateView, self).get_context_data(**kwargs)
        context["resource_types"] = self.model.objects.all().order_by('-id')
        return context
    def form_valid(self, form):
    	if form.is_valid():
    		form.save()
    		return redirect('resource-type')

class ResourceCreateView(CreateView):
	model = Resource
	fields =['description','resource_type','source','quantity','amount','year','photo']
	def get_context_data(self, **kwargs):
		context = super(ResourceCreateView, self).get_context_data(**kwargs)
		page = self.request.GET.get('page')
		resources = Paginator(self.model.objects.all().order_by('-id'), 10)
		context["resources"] = resources.get_page(page)
		return context
	def form_valid(self, form):
		if form.is_valid():
			form.instance.user = self.request.user
			form.save()
			return redirect('resource')

class ResourceUpdateView(UpdateView):
	model = Resource
	fields =['description','resource_type','source','quantity','amount','year','photo']
	def get_context_data(self, **kwargs):
		context = super(ResourceUpdateView, self).get_context_data(**kwargs)
		page = self.request.GET.get('page')
		resources = Paginator(self.model.objects.all().order_by('-id'), 10)
		context["resources"] = resources.get_page(page)
		return context
	def form_valid(self, form):
		if form.is_valid():
			form.instance.user = self.request.user
			form.save()
			return redirect('resource')

class ResourceDetailView(DetailView):
	model = Resource
	def get_context_data(self, **kwargs):
		context = super(ResourceDetailView, self).get_context_data(**kwargs)
		page = self.request.GET.get('page')
		allocated = Paginator(AllocateResource.objects.filter(resource=self.object).order_by('-id'), 10)
		context["allocated"] = allocated.get_page(page)
		return context

class AllocateResourceCreateView(CreateView):
	model = AllocateResource
	fields =['resource','school','quantity','amount','date_allocated','date_valid','year']
	def get_context_data(self, **kwargs):
		context = super(AllocateResourceCreateView, self).get_context_data(**kwargs)
		page = self.request.GET.get('page')
		allocate_resources = Paginator(self.model.objects.all().order_by('-id'), 10)
		context["allocate_resources"] = allocate_resources.get_page(page)
		return context
	def form_valid(self, form):
		if form.is_valid():
			form.instance.user = self.request.user
			form.save()
			return redirect('allocate-resource')

class AllocateResourceUpdateView(UpdateView):
	model = AllocateResource
	fields =['resource','school','quantity','amount','date_allocated','date_valid','year']
	def get_context_data(self, **kwargs):
		context = super(AllocateResourceUpdateView, self).get_context_data(**kwargs)
		page = self.request.GET.get('page')
		allocate_resources = Paginator(self.model.objects.all().order_by('-id'), 10)
		context["allocate_resources"] = allocate_resources.get_page(page)
		return context
	def form_valid(self, form):
		if form.is_valid():
			form.instance.user = self.request.user
			form.save()
			return redirect('allocate-resource')

class ResourceListView(ListView):
	model = Resource
	context_object_name = 'resources'
	ordering = ['-id']

class AllocateResourceListView(ListView):
	model = AllocateResource
	context_object_name = 'allocated_resources'
	ordering = ['-id']

class ProductCreateView(LoginRequiredMixin, CreateView):
	model = Product
	fields =['title','description','price','phone_contact','photo']
	def get_context_data(self, **kwargs):
		context = super(ProductCreateView, self).get_context_data(**kwargs)
		page = self.request.GET.get('page')
		products = Paginator(self.model.objects.filter(user=self.request.user).order_by('-id'), 10)
		context["products"] = products.get_page(page)
		return context
	def form_valid(self, form):
		if form.is_valid():
			form.instance.user = self.request.user
			form.save()
			return redirect('product')

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Product
	fields =['title','description','price','phone_contact','status','photo']
	def get_context_data(self, **kwargs):
		context = super(ProductUpdateView, self).get_context_data(**kwargs)
		context["products"] = self.model.objects.filter(user=self.request.user).order_by('-id')
		return context
	def form_valid(self, form):
		if form.is_valid():
			form.instance.user = self.request.user
			form.save()
			return redirect('product')
	def test_func(self):
		product = self.get_object()
		if self.request.user == product.user:
			return True
		return False

class ProductListView(ListView):
	model = Product
	context_object_name = 'products'
	ordering = ['-id']

class UserProducts(ListView):
	model = Product
	def get_context_data(self, **kwargs):
		context = super(UserProducts, self).get_context_data(**kwargs)
		page = self.request.GET.get('page')
		products = pagenator = Paginator(self.model.objects.filter(user=self.request.user).order_by('-id'), 2)
		context["products"] = products.get_page(page)
		return context

class ProductDetailView(DetailView):
	model = Product

class ProductStatusCreateView(CreateView):
    model = ProductStatus
    fields =['status']
    def get_context_data(self, **kwargs):
        context = super(ProductStatusCreateView, self).get_context_data(**kwargs)
        context["statuses"] = self.model.objects.all().order_by('-id')
        return context
    def form_valid(self, form):
    	if form.is_valid():
    		form.save()
    		return redirect('product-status')

class ProductStatusUpdateView(UpdateView):
    model = ProductStatus
    fields =['status']
    def get_context_data(self, **kwargs):
        context = super(ProductStatusUpdateView, self).get_context_data(**kwargs)
        context["statuses"] = self.model.objects.all().order_by('-id')
        return context
    def form_valid(self, form):
    	if form.is_valid():
    		form.save()
    		return redirect('product-status')

def home(request):
	all_schools = School.objects.count()
	all_deos = Deo.objects.count()
	all_teachers = Teacher.objects.count()
	all_resources = Resource.objects.count()
	all_trtransfer = TransferTeacher.objects.count()
	all_deotransfer = TransferDeo.objects.count()
	return render(request, 'school_home/home.html', {'title': 'Home', 
		'all_schools':all_schools, 
		'all_deos':all_deos, 
		'all_teachers':all_teachers, 
		'all_resources':all_resources, 
		'all_trtransfer':all_trtransfer, 
		'all_deotransfer':all_deotransfer })

def schools(request):
	return render(request, 'school_home/schools.html', {'title': 'Schools'})

def teachers(request):
	return render(request, 'school_home/teachers.html', {'title': 'Teachers'})

def deos(request):
	return render(request, 'school_home/deos.html', {'title': 'DEOs'})

def resources(request):
	return render(request, 'school_home/resources.html', {'title': 'Resources'})

def marketing(request):
	product_list = Product.objects.filter(status=1).order_by('-id')
	products_sold = Product.objects.filter(user=request.user, status=2).order_by('-id')
	paginator = Paginator(product_list, 5)
	page = request.GET.get('page')
	products = paginator.get_page(page)
	return render(request, 'school_home/marketing.html', {'title': 'Marketing', 'products':products, 'products_sold':products_sold})

def communication(request):
	return render(request, 'school_home/communication.html', {'title': 'Communication'})

def settings(request):
	return render(request, 'school_home/settings.html', {'title': 'Settings'})