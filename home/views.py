from django.shortcuts import render
import time
import json
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


async def home(request):
    for i in range(1, 10):
        channel_layer = get_channel_layer()
        data = {'count': i}
        await (channel_layer.group_send)(
            'test_consumer_group', {
                'type': 'send_notification',
                'value': json.dumps(data)
            }
        )
        time.sleep(1)
    return render(request, 'home.html')
