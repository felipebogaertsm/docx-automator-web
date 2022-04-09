from docxtpl import DocxTemplate

if __name__ == '__main__':
    document = DocxTemplate('../samples/template_ctx.docx')
    context = {'device_name': 'Hi'}
    document.render(context)
    document.save()