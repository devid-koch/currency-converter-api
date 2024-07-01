import requests
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.conf import settings

@require_GET
def convert_currency(request):
    try:
        amount = float(request.GET.get('amount', 0))
    except ValueError:
        return JsonResponse({'error': 'Invalid amount provided'}, status=400)
    
    to_currency = request.GET.get('to', 'USD')
    from_currency = request.GET.get('from', 'EUR')
    api_key = settings.EXCHANGE_RATE_API_KEY
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': 'Failed to fetch exchange rates', 'details': str(e)}, status=500)

    if data.get('result') != 'success':
        return JsonResponse({'error': 'Invalid response from exchange rate API'}, status=500)

    rates = data.get('conversion_rates', {})
    if to_currency not in rates:
        return JsonResponse({'error': 'Invalid currency code'}, status=400)

    converted_amount = amount * rates[to_currency]

    return JsonResponse({
        'amount': amount,
        'from': from_currency,
        'to': to_currency,
        'converted_amount': converted_amount,
    })
