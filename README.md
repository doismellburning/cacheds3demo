# cacheds3demo

A demo of versioned static assets on S3 in Django, using `django.contrib.staticfiles.storage.ManifestFilesMixin` (new in 1.7) and `django-storage`'s `storage.backends.s3boto.S3BotoStorage`.

## Files to look at

* `cacheds3demo/cacheds3demo/settings.py`
* `cacheds3demo/cacheds3demo/storage.py`
* `cacheds3demo/core/urls.py`

## Live Demo

`https://vast-beach-8665.herokuapp.com/favicon.ico` - this will issue a redirect to the equivalent of `{% static 'favicon.ico' %}`, which will be `https://cacheds3demo.s3.amazonaws.com/favicon.961c9e415bbb.ico` (hash may vary).
