from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.template import Context

def generate_pdf(request):
    # Retrieve user and profile information
    user = request.user
    user_profile = user.profile

    # Prepare the context data
    context = {
        'user': user,
    }

    # Render the template
    template = get_template('template.html')
    rendered_html = template.render(context)

     # Set the PDF options for one-page layout
    pdf_options = {
        'page-size': 'A4',
        'dpi': 300,
        'margin-top': '0cm',
        'margin-right': '0cm',
        'margin-bottom': '0cm',
        'margin-left': '0cm',
    }

    # Create a PDF response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="generated_pdf.pdf"'

    # Generate the PDF using xhtml2pdf
    pisa_status = pisa.CreatePDF(rendered_html, dest=response)

    if pisa_status.err:
        return HttpResponse('An error occurred while generating the PDF')

    return response


def preview_information(request):
    # Retrieve user and profile information
    user = request.user
    user_profile = user.profile

    # Prepare the context data
    context = {
        'user': user,
    }

    # Render the template
    template = get_template('template.html')
    rendered_html = template.render(context)

    return HttpResponse(rendered_html)

