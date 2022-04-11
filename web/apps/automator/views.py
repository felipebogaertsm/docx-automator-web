import io
import json

from docxtpl import DocxTemplate

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from utils.datetime import get_datetime_ctx


class HomePage(View):
    def get(self, request):
        return render(request, "automator/home.html")

    def post(self, request):
        files = request.FILES
        template_file = files["template"]
        data_file = files["data"]

        document = DocxTemplate(template_file)
        context = json.load(data_file)  # getting context from json file
        context = {**context, **get_datetime_ctx()}
        document.render(context)

        bio = io.BytesIO()
        document.save(bio)

        response = HttpResponse(
            bio.getvalue(), content_type="application/force-download"
        )
        response["Content-Disposition"] = "attachment; filename=document.docx"
        response["Content-Encoding"] = "UTF-8"

        return response
