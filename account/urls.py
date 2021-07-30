from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import *

urlpatterns = [

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')

]

# settings

#   manage access

# invite

# copy SSH OR HTTPS

# git clone or git init

# git clone url

# do smth new

# git branch titleofnewbranch
# git branch

# git checkout newbranch
# git branch

# git add .
# git status

# git commit -m 'add new smth'

# git push origin sher

# go to your github

# compate and pul request

# reviewers celect

# merge pull request


# git commit -m '#2'


