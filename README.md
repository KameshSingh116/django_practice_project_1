# django_practice_project_1
This is the first project which i am going to make using django to practice what i have learned in django so far

For any doubts clarification you may refer to the other github repo with course of django.
- https://github.com/KameshSingh116/djangoo_course

To connect the frontend to the backend , we need to use a method which is actually a post method.

- method="post"
### This is used to get the data from frontend to the backend
### But vice versa is done using the "context" attribute.

also we use "request.POST" in the views.

Next we need to give something like this {% csrf_token %}
Django uses this to check and verify whether the request to get the frontend data to the backend is coming from this or our own currently used server or not.

Its kind of a security stuff/protocol.
