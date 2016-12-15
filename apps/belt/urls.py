from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register_process$' , views.register_process),
    url(r'^login_process$' , views.login_process),
    url(r'^books$' , views.books),
    url(r'^add$' , views.add_book),
    url(r'^bookprocess$' , views.add_book_process),
    url(r'^book/1$' , views.add_review), # Change this to parameter of book ID
    url(r'^user/1$' , views.dashboard), # We will change the ID dude or Marjan will kill you!
    url(r'^delete_review$' , views.delete_review),
    url(r'^logout$' , views.logout),

]
