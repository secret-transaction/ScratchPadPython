__author__ = 'Lyndon'

import endpoints
from hello.models import Greeting
from protorpc import messages
from protorpc import message_types
from protorpc import remote
from google.appengine.ext import db


package = 'Hello'


class GreetingRequest(messages.Message):
    """Greeting that stores a message."""
    message = messages.StringField(1)


class GreetingCollection(messages.Message):
    """Collection of Greetings."""
    items = messages.MessageField(GreetingRequest, 1, repeated=True)


class GreetingResponse(messages.Message):
    greetingId = messages.StringField(1)

STORED_GREETINGS = GreetingCollection(items=[
    GreetingRequest(message='hello world!'),
    GreetingRequest(message='goodbye world!'),
])


@endpoints.api(name='helloworld', version='v1')
class HelloWorldApi(remote.Service):
    """Helloworld API v1."""

    ID_RESOURCE = endpoints.ResourceContainer(
        message_types.VoidMessage, id=messages.IntegerField(1, variant=messages.Variant.INT32))

    @endpoints.method(message_types.VoidMessage, GreetingCollection,
                      path='hellogreeting', http_method='GET',
                      name='greetings.listGreeting')
    def greetings_list(self, unused_request):
        all_greetings = db.GqlQuery('SELECT * FROM Greeting')

        my_list = []
        for g in all_greetings:
            my_list.append(GreetingRequest(message=g.content))

        return GreetingCollection(items=my_list)

    @endpoints.method(GreetingRequest, GreetingResponse,
                      path='greet', http_method='POST',
                      name='greetings.createGreeting')
    def create_greeting(self, request):
        g = Greeting(content=request.message)
        g.put()

        return GreetingResponse(greetingId=str(g.key()))


    @endpoints.method(ID_RESOURCE, GreetingRequest,
                      path='hellogreeting/{id}', http_method='GET',
                      name='greetings.getGreeting')
    def greeting_get(self, request):
        try:
            return STORED_GREETINGS.items[request.id]
        except (IndexError, TypeError):
            raise endpoints.NotFoundException('Greeting %s not found.' %
                                              (request.id,))


APPLICATION = endpoints.api_server([HelloWorldApi])