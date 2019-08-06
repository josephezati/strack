from django.urls import path
from .views import *
from . import views

urlpatterns = [
    # Home related urls-----------------------------------------------------------------------------
    path('', views.home, name='strack-home'),
    # School related urls-----------------------------------------------------------------------------
    path('schools/', views.schools, name='strack-schools'),
    path('schools/new/', SchoolCreateView.as_view(), name='new-school'),
    path('schools/view/', SchoolListView.as_view(), name='view-schools'),
    path('schools/<int:pk>/', SchoolDetailView.as_view(), name='school-details'),
    path('schools/<int:pk>/update/', SchoolUpdateView.as_view(), name='update-school'),
    path('schools/<int:pk>/facility/',FacilityCreateView.as_view(), name='new-facility'),
    path('schools/ownership/', OwnershipCreateView.as_view(), name='ownership'),
    path('schools/ownership/<int:pk>/update/', OwnershipUpdateView.as_view(), name='ownership-update'),
    path('schools/access/', AccessCreateView.as_view(), name='access'),
    path('schools/access/<int:pk>/update/', AccessUpdateView.as_view(), name='access-update'),
    path('schools/section/', SectionCreateView.as_view(), name='section'),
    path('schools/section/<int:pk>/update/', SectionUpdateView.as_view(), name='section-update'),
    path('schools/level/', LevelCreateView.as_view(), name='level'),
    path('schools/level/<int:pk>/update/', LevelUpdateView.as_view(), name='level-update'),
    path('schools/category/', CategoryCreateView.as_view(), name='category'),
    path('schools/category/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    path('schools/schtype/', SchtypeCreateView.as_view(), name='schtype'),
    path('schools/schtype/<int:pk>/update/', SchtypeUpdateView.as_view(), name='schtype-update'),
    path('schools/regstatus/', RegstatusCreateView.as_view(), name='regstatus'),
    path('schools/regstatus/<int:pk>/update/', RegstatusUpdateView.as_view(), name='regstatus-update'),
    path('schools/cennostatus/', CennostatusCreateView.as_view(), name='cennostatus'),
    path('schools/cennostatus/<int:pk>/update/', CennostatusUpdateView.as_view(), name='cennostatus-update'),
    path('schools/district/<int:pk>/update/', DistrictUpdateView.as_view(), name='district-update'),
    path('schools/district/', DistrictCreateView.as_view(), name='district'),
    path('schools/region/', RegionCreateView.as_view(), name='region'),
    path('schools/region/<int:pk>/update/', RegionUpdateView.as_view(), name='region-update'),
    # Facility related urls-----------------------------------------------------------------------------
    path('schools/factype/', FacilityTypeView.as_view(), name='factype'),
    path('schools/factype/<int:pk>/update/', FacilityTypeUpdateView.as_view(), name='factype-update'),
    path('schools/facstatus/', FacilityStatusView.as_view(), name='facstatus'),
    path('schools/facstatus/<int:pk>/update/', FacilityStatusUpdateView.as_view(), name='facstatus-update'),
    
    # Teacher related urls-----------------------------------------------------------------------------

    path('teachers/', views.teachers, name='strack-teachers'),
    path('teachers/new/', TeacherCreateView.as_view(), name='new-teacher'),
    path('teachers/view/', TeacherListView.as_view(), name='view-teachers'),
    path('teachers/transfer/view/', TeacherTransferListView.as_view(), name='view-teacher-transfers'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher-details'),
    path('teachers/<int:pk>/update/', TeacherUpdateView.as_view(), name='update-teacher'),
    path('teachers/gender/', GenderCreateView.as_view(), name='gender'),
    path('teachers/gender/<int:pk>/update/', GenderUpdateView.as_view(), name='update-gender'),
    path('teachers/status/', TeacherStatusCreateView.as_view(), name='teacher-status'),
    path('teachers/status/<int:pk>/update/', TeacherStatusUpdateView.as_view(), name='update-teacher-status'),
    path('teachers/transfer/', TransferTeacherCreateView.as_view(), name='transfer-teacher'),
    path('teachers/transfer/<int:pk>/update/', TransferTeacherUpdateView.as_view(), name='update-transfer'),
    path('teachers/designation/', DesignationCreateView.as_view(), name='designation'),
    path('teachers/designation/<int:pk>/update/', DesignationUpdateView.as_view(), name='update-designation'),
    # DEO related urls-----------------------------------------------------------------------------
    path('DEOs/', views.deos, name='strack-deos'),
    path('DEOs/new/', DeoCreateView.as_view(), name='new-deo'),
    path('DEOs/view/', DeoListView.as_view(), name='view-deos'),
    path('DEOs/<int:pk>/', DeoDetailView.as_view(), name='deo-details'),
    path('DEOs/<int:pk>/update/', DeoUpdateView.as_view(), name='update-deo'),
    path('DEOs/transfer/', TransferDeoCreateView.as_view(), name='transfer-deo'),
    path('DEOs/transfer/<int:pk>/update/', TransferDeoUpdateView.as_view(), name='update-deo-transfer'),
    # Resource related urls-----------------------------------------------------------------------------
    path('resources/', views.resources, name='strack-resources'),
    path('resources/type/', ResourceTypeCreateView.as_view(), name='resource-type'),
    path('resources/type/<int:pk>/update/', ResourceTypeUpdateView.as_view(), name='update-resource-type'),
    path('resources/source/', ResourceSourceCreateView.as_view(), name='resource-source'),
    path('resources/source/<int:pk>/update/', ResourceSourceUpdateView.as_view(), name='update-resource-source'),
    path('resources/resource/', ResourceCreateView.as_view(), name='resource'),
    path('resources/resource/<int:pk>/', ResourceDetailView.as_view(), name='resource-detail'),
    path('resources/view/', ResourceListView.as_view(), name='view-resources'),
    path('resources/resource/<int:pk>/update/', ResourceUpdateView.as_view(), name='update-resource'),
    path('resources/allocate/', AllocateResourceCreateView.as_view(), name='allocate-resource'),
    path('resources/allocate/view/', AllocateResourceListView.as_view(), name='allocated-resources'),
    path('resources/allocate/<int:pk>/update/', AllocateResourceUpdateView.as_view(), name='update-allocate-resource'),
    # Marketing related urls-----------------------------------------------------------------------------
    path('marketing/', views.marketing, name='strack-marketing'),
    path('marketing/new-product/', ProductCreateView.as_view(), name='product'),
    path('marketing/<int:pk>/update/', ProductUpdateView.as_view(), name='update-product'),
    path('marketing/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('marketing/user-products/', UserProducts.as_view(), name='user-products'),
    path('marketing/product-status/', ProductStatusCreateView.as_view(), name='product-status'),
    path('marketing/product-status/<int:pk>/update/', ProductStatusUpdateView.as_view(), name='update-product-status'),

    # Communication related urls-----------------------------------------------------------------------------
    path('communication/', views.communication, name='strack-communication'),
    # Settings related urls-----------------------------------------------------------------------------
    path('settings/', views.settings, name='strack-settings'),
]
