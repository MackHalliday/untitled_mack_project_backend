# 2023-12-04 
## Overview
- Create basic Django application
- Create venv 
- Create Views, Urls, and Templates for authentication app
  
# 2023-12-05
## Overview
- Continued building auth functionality with help from the YouTube video [How to Create a Login System in Python Using Django?](https://www.youtube.com/watch?v=1UvTNMH7zDo)
- Started branches

## Creating Signin Page 
- Use `<form>` and `<input>` to create form that accepts first name, last name, username, email, and password 
- Use `{% csrf_token %}` tag within form to generate a CSRF token. Token is used to protect Django application from cross-site request forgery (CSRF) attacks.


## Contrib package
- Django's built tooling [contrib package](https://docs.djangoproject.com/en/4.2/ref/contrib/)
- Can return messages to user after code in View is executed with `messages.success(request, "message")`
  
