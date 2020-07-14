import logging
import logging.config
import sys

from django.http import JsonResponse
from rest_framework.decorators import api_view

from .ai import rain_fall_prediction as rp

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
        }
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO'
    }
}


@api_view(["GET"])
def predict(request):
    temp = float(request.GET.get('temp'))
    humid = float(request.GET.get('humid'))

    logging.config.dictConfig(LOGGING)

    pr = rp.predict(temp, humid)
    logging.info(type(pr))

    content = {"precipitation": pr}
    return JsonResponse(content)
