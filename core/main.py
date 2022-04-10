import datetime
import json

from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm


def get_datetime_ctx():
    date = datetime.datetime.now()
    return {"date": {"day": date.day, "month": date.strftime("%B"), "year": date.year}}


if __name__ == "__main__":
    document = DocxTemplate("../samples/template.docx")

    with open("../samples/data.json") as data_file:
        context = json.load(data_file)  # getting context from json file

    # Replacing image:
    context["image1"]["src"] = InlineImage(
        document, context["image1"]["src"], width=Mm(150)
    )

    context = {**context, **get_datetime_ctx()}

    document.render(context)  # replacing jinja2 tags with json context
    document.save("../samples/template_new.docx")
