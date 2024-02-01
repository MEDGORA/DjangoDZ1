from django.shortcuts import render
from django.http import HttpResponse
import logging

from flask import render_template

logger = logging.getLogger(__name__)

# Create your views here.
def main(request):
    logger.info("main was opened")
    return HttpResponse("Это главная страница. Чтобы увидеть информацию про меня перейдите в /about/.")
    #return render(request, "main.html")

def about(request):
    logger.info("about was opened")
    return HttpResponse("Это страница про меня")
