from django.urls import path
from django.conf import settings

from django.conf.urls.static import static
from Organizer import views

urlpatterns = [
    path('', views.indx, name='organiserIndex'),
    path('organiseEvent', views.organiseEvent, name='organiseEvent'),
    path('formpage/', views.form_name_view, name='form_name'),
    path('organiseEventFormData', views.organiseEventFormData,
         name="organiseEventFormData"),
    path('registeredEvent', views.registeredEvent, name='registeredevent'),
    path('eventRegistered/<int:id>', views.eventEdit, name='eventEdit'),
    path('eventUpdate/<int:id>', views.eventUpdate, name='eventupdate'),
    path('evenDetailsdelete/<int:id>',views.evenDetailsdelete,name='evenDetailsdelete'),
    path('addEventDetails', views.addrubrics, name='addEventDetails'),
    path('editRubrics/<int:id', views.returnEditRubrics, name='editRubrics'),
    path('evenDetailsUpdate/<int:id>',
         views.evenDetailsUpdate, name='evenDetailsUpdate'),
    path('addEvent', views.eventDetails, name='eventdetails'),
    path('shareResourcese', views.shareResource, name='shareResource'),
    path('shareResource', views.resource, name='Resource'),
    path('edit_resource', views.editResource, name='editResource'),
    path('updateShareResources/<int:id>',
         views.updateShareResources, name='update_shareResources'),
    path('blog', views.blog, name='blog'),
    path('blogsDetail', views.blogsDetails, name='blogsDetails'),
    path('WriteBlog', views.writeBlogs, name='WriteBlog'),
    path('sponsorShip', views.sponsorShip, name='sponsorShip'),
    path('sponsorShipDetails', views.sponsorShipDetails,
         name='sponsorShipDetails'),
    path('editSponsorShip', views.editSponsorShip, name='editSponsorShip'),
    path('updateSponsorInfo/<int:id>',
         views.updateSponsorInfo, name='updateSponsorInfo'),
    path('deletesponsor/<int:id>', views.deletesponsor, name='deletesponsor'),
    path('deleteeventdetails/<int:id>',views.deleteeventdetails,name='deleteeventdetails'),
    path('deleteresourcedetails/<int:id>',views.deleteresourcedetails,name='deleteresourcedetails'),
    path('EventLocation', views.EventLocation, name='EventLocation'),
    path('location_view',views.Location_view,name='view_locatiion'),
    path('load_map',views.load_map,name='load_map'),
    path('EventLocationload', views.EventLocationload, name='EventLocationload'),
    path('locationUpdate/<int:id>', views.locationupdate, name='locationupdate'),
    path('locationdelete/<int:id>', views.locationdelete, name='locationdelete'),
    path('profile_org', views.profile_org, name='profile_org'),
    path('editProfile', views.editProfile, name='editProfile'),
	path('req_pdf',views.req_pdf,name="req_pdf"),
    path('updateProfile', views.updateProfile, name='update_profile'),
     path('del_profile/<int:id>',views.del_profile,name='del_profile'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
