from django.http import HttpResponse, HttpResponseRedirect, HttpRequest, Http404
from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
import requests, json, urllib, os


def sales_inquiry_form(request):
    return render(request, 'pages/sales_inquiry_form.html')

def sales_inquiry_hubspot_form(request):
    submitted = ''
    r = ''
    data = ''
    if request.method == 'POST':
        #Need to check if hidden field website returned a value. If so then a bot is trying to submit the form. Skip to return redirect(slug).
        website = request.POST['website']
        if website != '':
            slug = request.POST['slug']+'?inquiry-status=unsuccessful#anchor-inquiry-form'
            return redirect(slug)
        else:
            headers = {}
            headers["Content-Type"]='application/x-www-form-urlencoded'
            endpoint = os.environ.get('HUBSPOT_SALES_INQUIRY_FORM')

            # Getting visitors ip address
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')

            #Convert the hs_context dictionary to a string
            hs_context = json.dumps({
                "hutk": request.COOKIES.get('hubspotutk'),
                "ipAddress": ip,
                "pageUrl": request.POST['slug'],
                "pageName": request.POST['page_title'], 
            })

            data = urllib.parse.urlencode({
                'firstname': request.POST['firstname'],
                'lastname': request.POST['lastname'],
                'email': request.POST['email'],
                'company': request.POST['company'],
                'message': request.POST['message'],
                'hs_context': hs_context
            })

            r = requests.post( url = endpoint, data = data, headers = headers)

            if r.status_code == 204:
                slug = request.POST['slug']+'?inquiry-status=success#anchor-inquiry-form'
            else:
                slug = request.POST['slug']+'?inquiry-status=unsuccessful#anchor-inquiry-form'
            return redirect(slug)
    else:
        raise Http404()