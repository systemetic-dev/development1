# Notes
[Day 1]
    # Backend is the brain of a website or app.
    🧸 Real-life example
     🍦 Ice Cream Shop Story
        You go to an ice cream shop.
        You → customer
        Menu board → frontend
        Shop worker inside → backend
        Freezer room → database
    Steps:
        You say: “I want chocolate ice cream”
        Worker hears you (request)
        Worker checks freezer
        Worker takes ice cream
        Worker gives it to you (response)
        You never see the freezer work.
        You only see the ice cream 🍦

That hidden work = backend

# Django is a tool for building backend.

# What is a Django Project ?
    One website = one Django project

# Django code implementation
    "django-admin startproject mysite" run in terminal 
    It make 
mysite/
│
├── manage.py
│
└── mysite/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py