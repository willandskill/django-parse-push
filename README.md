# django-parse-push #

A simple Django library for pushing notifications thru Parse.

---

**Comes out of the box with**

* Django REST Framework endpoint for registering a device token thru REST
* Basic tests

## Installation ##

1) Install thru PIP

    pip install django-parse-push

2) Add `parse_push` to `settings.INSTALLED_APPS`

```python
    INSTALLED_APPS = (
        # ...,
        parse_push,
    )
```

3) Run migrations

    python manage.py migrate parse_push

4) Add environment vars

```bash
PARSE_APPLICATION_ID=your_parse_application_id
PARSE_REST_API_KEY=your_parse_api_key

# Optional environment vars
PARSE_API_URL=https://api.parse.com
PARSE_API_VERSION=1
```

5) Add REST endpoint to urls.py

```python
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    # ...

    (r'^api/v1/parse-push', include('parse_push.urls')),

    # ...
)
```

## Usage ##

###Example 1###
*A simple Django based example*

```python
from django.contrib.auth import get_user_model

User = get_user_model()
user = User.objects.get(email='donald@duck.com')
device = user.device_set.get_latest('created_at')
device.push({'title': 'Hello World!', 'text': 'Lorem ipsum dolor...'})
```

###Example 2###
*With Django based User model*

```python
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class User(AbstractBaseUser, PermissionsMixin)

    # ...

    def get_full_name(self):
        """ Returns the full name """
        full_name = u"{} {}".format(self.first_name, self.last_name)
        return full_name.strip()

    def push(self, data):
        device = self.device_set.get_latest()
        return device.push(data)
```

###Example 3###
*Barebone client, no dependency on Django*

```python
from parse_push.client import get_client

client = get_client()
client.push('ios', 'devicetokenabcdefghijklmnopqstruvwxyz0123456789', {'foo': 'bar'})
```

You can also configure a Client instance with `APPLICATION_ID` and `REST_API_KEY`

```python
client = Client(application_id='applicationidabcdefghijklmn0123456789', rest_api_key='restapikeyabcdefghijklmn0123456789')
```