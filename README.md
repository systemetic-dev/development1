# Notes

-------------------------------------------------------------------------[Day 1]--------------------------------------------------------------------------


# 🚀 DJANGO BACKEND NOTES (Lesson 1–17)

---

# 1️⃣ What is Backend?

- Backend = brain of website 🧠
- It is not visible to users
- It:
  - Receives requests
  - Processes logic
  - Talks to database
  - Sends response

Flow:

```
Browser → Backend → Database → Backend → Browser
```

---

# 2️⃣ What is Django?

- Django = Python backend framework
- Tool to build backend faster
- Handles:
  - Security
  - URLs
  - Database connection
  - Admin panel

Django saves time and prevents common mistakes.

---

# 3️⃣ What is a Django Project?

- Project = big container 📦
- One website = one project
- Holds:
  - Settings
  - URLs
  - Apps

Created using:

```bash
django-admin startproject mysite
```

---

# 4️⃣ Running the Server

Server = program that listens 👂

Run server:

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

127.0.0.1 = your computer
8000 = port (door number)

---

# 5️⃣ What is a Django App?

- App = small worker inside project 👷
- Each app does one job
- Example:
  - Blog app
  - Payment app
  - Auth app

Create app:

```bash
python manage.py startapp blog
```

---

# 6️⃣ Registering an App

Add app to `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'blog',
]
```

Without registration:

- Django ignores app ❌

---

# 7️⃣ What is a View?

View = function that:

- Receives request
- Runs logic
- Returns response

Example:

```python
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello")
```

---

# 8️⃣ URLs (Routing)

URL connects path → view

In `urls.py`:

```python
from blog.views import hello

urlpatterns = [
    path('hello/', hello),
]
```

Flow:

```
URL → View → Response
```

---

# 9️⃣ Templates

Template = HTML page 🖼️
Used to send proper web pages.

In view:

```python
return render(request, 'blog/hello.html')
```

Browser only sees HTML.

---

# 🔟 Passing Data to Template

Send dictionary:

```python
data = {"name": "Dev"}
return render(request, 'blog/hello.html', data)
```

In template:

```html
{{ name }}
```

View sends data.
Template shows data.

---

# 1️⃣1️⃣ Template Logic (if & for)

Conditional:

```html
{% if is_logged_in %} Welcome {% endif %}
```

Loop:

```html
{% for item in items %} {{ item }} {% endfor %}
```

Template has small logic only.

---

# 1️⃣2️⃣ Models (Database Blueprint)

Model = table blueprint 📊

Example:

```python
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
```

Create table:

```bash
python manage.py makemigrations
python manage.py migrate
```

Model = permanent storage 💾

---

# 1️⃣3️⃣ Admin Panel

Admin = control room 🎛️

Create superuser:

```bash
python manage.py createsuperuser
```

Register model:

```python
from .models import Post
admin.site.register(Post)
```

Open:

```
/admin/
```

---

# 1️⃣4️⃣ Showing Database Data

Fetch in view:

```python
posts = Post.objects.all()
return render(request, 'blog/post_list.html', {"posts": posts})
```

In template:

```html
{% for post in posts %} {{ post.title }} {% endfor %}
```

Flow:

```
Model → View → Template
```

---

# 1️⃣5️⃣ Manual Forms

HTML form:

```html
<form method="post">
  {% csrf_token %}
  <input name="title" />
</form>
```

In view:

```python
if request.method == "POST":
    title = request.POST.get("title")
    Post.objects.create(title=title)
```

POST = sending data
GET = asking for page

---

# 1️⃣6️⃣ Django Forms (ModelForm)

Create `forms.py`:

```python
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
```

In view:

```python
form = PostForm(request.POST)
if form.is_valid():
    form.save()
```

Template:

```html
{{ form.as_p }}
```

Django handles:

- Validation
- Saving
- Error messages

---

# 1️⃣7️⃣ App-Level URLs (Clean Structure)

Create:

```
blog/urls.py
```

```python
from django.urls import path
from .views import post_list

urlpatterns = [
    path('', post_list),
]
```

Project `urls.py`:

```python
path('posts/', include('blog.urls')),
```

Project = main gate
App = internal roads

---

# 🧠 Core Backend Flow (Important)

Always remember:

```
Request
   ↓
URL
   ↓
View
   ↓
Model (optional)
   ↓
Template
   ↓
Response
```

That is Django’s heart ❤️

i understand the flow of everything.
