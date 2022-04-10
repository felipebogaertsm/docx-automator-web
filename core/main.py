from docxtpl import DocxTemplate
import json

if __name__ == '__main__':
    document = DocxTemplate('../samples/template_ctx.docx')
    
    with open('../samples/data.json') as data_file:
        context = json.load(data_file) # getting context from json file

    document.render(context)  # replacing jinja2 tags with json context
    document.save()