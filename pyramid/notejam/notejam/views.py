from pyramid.response import Response
from pyramid.view import view_config

from pyramid_simpleform import Form
from pyramid_simpleform.renderers import FormRenderer

from sqlalchemy.exc import DBAPIError

from models import DBSession, MyModel, User
from forms import UserSchema


@view_config(route_name='home', renderer='templates/base.pt')
def my_view(request):
    try:
        one = DBSession.query(MyModel).filter(MyModel.name == 'one').first()
    except DBAPIError:
        return Response('text', content_type='text/plain', status_int=500)
    return {'one': one, 'project': 'notejam'}


@view_config(route_name='signin', renderer='templates/users/signin.pt')
def signin(request):
    form = Form(request, schema=UserSchema())
    if form.validate():
        user = form.bind(User())
        # persist user
        # redirect to signin page
    return dict(renderer=FormRenderer(form))


@view_config(route_name='signup', renderer='templates/users/signup.pt')
def signup(request):
    form = Form(request, schema=UserSchema())
    if form.validate():
        user = form.bind(User())
        ## persist user
        ## redirect to signin page
    return dict(renderer=FormRenderer(form))

    

def account_settings(request):
    pass


def forgot_password(request):
    pass


def notes(request):
    pass


def create_note(request):
    pass


def update_note(request):
    pass


def delete_note(request):
    pass


def create_pad(request):
    pass


def update_pad(request):
    pass


def delete_pad(request):
    pass