import requests
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.conf import settings

@require_GET
def convert_currency(request):
    amount = float(request.GET.get('amount', 0))
    to_currency = request.GET.get('to', 'USD')
    from_currency = request.GET.get('from', 'EUR')
    api_key = settings.EXCHANGE_RATE_API_KEY
    url = f"http://api.exchangeratesapi.io/v1/latest?access_key={api_key}"

    response = requests.get(url)
    data = response.json()

    if not data['success']:
        return JsonResponse({'error': 'Failed to fetch exchange rates'}, status=500)

    rates = data.get('rates', {})
    if from_currency not in rates or to_currency not in rates:
        return JsonResponse({'error': 'Invalid currency code'}, status=400)

    base_amount = amount / rates[from_currency]
    converted_amount = base_amount * rates[to_currency]

    return JsonResponse({
        'amount': amount,
        'from': from_currency,
        'to': to_currency,
        'converted_amount': converted_amount,
    })
