django-media
============

A reusable [Django](http://www.djangoproject.com/) application to store and manage media. This application was originally created by [Nathan Borror](http://nathanborror.com/) for [django-basic-apps](https://github.com/nathanborror/django-basic-apps), his collection of simple prebuilt Django applications.


How it Works
------------

Models are included for storing audio, photos, and video, as well as sets of these three objects. URLs (using generic views) and templates are included for displaying these objects.


Requirements
------------

* [Python Imaging Library](http://www.pythonware.com/products/pil/) is required for getting photo EXIF data.


Installation
------------

django-media is available on PyPI and can be installed with PIP.

    pip install django-media

Alternatively, you may download the source and install it.

    python setup.py install




Setup
-----

Add `media` to your `settings.INSTALLED_APPS`.


### URLs

If you wish to use the default URL structure, you may do so by adding them to your project's URL patterns. For example:

    urlpatterns = patterns('',
        ...
        (r'^photos/', include('media.urls.photos')),
