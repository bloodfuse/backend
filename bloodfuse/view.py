from django.shortcuts import redirect, render
# from django.views.decorators import csrf_exempt
from django.http import HttpResponse

import git

from dj_rest_auth.registration.views import VerifyEmailView, ConfirmEmailView

# @csrf_exempt
# def update_from_github(request):
#     if request.method == "POST":
#         '''
#         pass the path of the diectory where your project will be
#         stored on PythonAnywhere in the git.Repo() as parameter.
#         Here the name of my directory is "test.pythonanywhere.com"
#         '''
#         repo = git.Repo("bloodfuse.pythonanywhere.com ")
#         origin = repo.remotes.origin
#         origin.pull()
#     return HttpResponse("Code updated successfully")


def redirect_to_index(request):
    return redirect("index")


class CustomEmailVerification(ConfirmEmailView):
    template_name = "ConfirmEmail.html"

    def get_template_names(self):
        template_name = "ConfirmEmail.html"
        return [template_name]
    
    def get(self, *args, **kwargs):
        print('<<<<<<<<<<<< Working >>>>>>>>>>>>>>>>>...')
        return super().get()