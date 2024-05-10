from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render
from .models import CSVData
import csv

def sanitize_csv(request):
    categorized_data = {}
    csv_data = CSVData.objects.all()

    # Categorize URLs based on common prefixes
    for data in csv_data:
        prefix = data.url.split('/')[2] if '/' in data.url else ''
        if prefix not in categorized_data:
            categorized_data[prefix] = []
        categorized_data[prefix].append(data.title)

    # Prepare CSV response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="output.csv"'
    writer = csv.writer(response)
    writer.writerow(['Category', 'Titles'])
    for category, titles in categorized_data.items():
        writer.writerow([category, ', '.join(titles)])

    return response
