from django.http import HttpResponse
from .models import Subscriber
from django.views.decorators.csrf import csrf_exempt


class Subscribers:

    # def get_subscribers(request):
    #     subscribers = Subscriber.objects.all()
    #     data = [{
    #         'email': subscriber.email,
    #         'first_name': subscriber.first_name,
    #         'Active': subscriber.is_active
    #     }
    #         for subscriber in subscribers
    #     ]
    #     return HttpResponse(data, status=200)

    def update_subscriber(request, subscriber_id):
        try:

            if request.method == 'PUT':

                subscriber = Subscriber.objects.get(
                    subscriber_id=subscriber_id)

                subscriber.is_active = False
                subscriber.save()

                return HttpResponse('Subscriber updated successfully', status=200)
            else:
                return HttpResponse('Only available for PUT requests', status=405)
        except Subscriber.DoesNotExist as error:
            return HttpResponse(error, status=404)
        except Exception as error:
            return HttpResponse(error, status=500)
