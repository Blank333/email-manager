from django.http import HttpResponse
from .models import Subscriber


class Subscribers:

    def update_subscriber(request, subscriber_id):
        try:

            if request.method == 'PUT':

                subscriber = Subscriber.objects.get(
                    subscriber_id=subscriber_id)

                # Unsubscribe the user
                subscriber.is_active = False
                subscriber.save()

                return HttpResponse('Subscriber updated successfully', status=200)
            else:
                return HttpResponse('Only available for PUT requests', status=405)
        except Subscriber.DoesNotExist as error:
            return HttpResponse(error, status=404)
        except Exception as error:
            return HttpResponse(error, status=500)
