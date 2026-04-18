import json
from pathlib import Path

from django.http import Http404
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET

_DATA_PATH = Path(__file__).resolve().parent.parent / 'data' / 'challenges.json'

MONTH_ORDER = [
    'january',
    'february',
    'march',
    'april',
    'may',
    'june',
    'july',
    'august',
    'september',
    'october',
    'november',
    'december',
]


def _load_challenges():
    with open(_DATA_PATH, encoding='utf-8') as f:
        return json.load(f)


@require_GET
def index(request):
    challenges = _load_challenges()
    months = []
    for key in MONTH_ORDER:
        if key not in challenges:
            continue
        months.append(
            {
                'slug': key,
                'label': key.replace('_', ' ').title(),
            }
        )
    return render(
        request,
        'challenges/index.html',
        {'months': months},
    )


@require_GET
def month_numeric_redirect(request, month_number):
    try:
        if not 1 <= month_number <= len(MONTH_ORDER):
            raise ValueError('Invalid month number.')
        slug = MONTH_ORDER[month_number - 1]
        return redirect('challenges:month', month=slug, permanent=False)
    except:
        raise Http404('Invalid month number.')

@require_GET
def monthly_challenge(request, month):
    month_key = month.lower()
    challenges = _load_challenges()
    if month_key not in challenges:
        raise Http404('No challenge for this month.')
    entry = challenges[month_key]
    return render(
        request,
        'challenges/month_detail.html',
        {
            'month_label': month_key.replace('_', ' ').title(),
            'title': entry.get('title') or 'Monthly challenge',
            'description': entry.get('description', ''),
        },
    )
