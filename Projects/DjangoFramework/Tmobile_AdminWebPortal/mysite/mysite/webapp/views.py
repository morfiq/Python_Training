# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# import subprocess
# Create your views here.
from django.http import HttpResponse
def index(request):
	return HttpResponse("<h2>HEY!</h2>")
# @register.simple_tag
# def render_help_text(field):
#     if hasattr(field, 'help_text'):
#         return mark_safe(
#             "<a><img src='/static/img/icons/help.gif' title='{help_text}' /></a>".format(**{'help_text': field.help_text})
#         )
#     return ''
# from git import Repo
# Repo.clone_from("github.com:OHIF/Viewers.git", "C:\Users\mohrafiq\Documents\MyHCL\Django_Projects\mysite\webapp\dicom_git_repo")
# subprocess.call([
#     "curl", "https://install.meteor.com/", "|", "sh"
# ], shell=False)

#METEOR_PACKAGE_DIRS="../Packages" meteor npm install