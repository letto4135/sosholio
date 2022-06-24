from django.db import models

# Models a top level domain and domain name
# for users to be in groups pertaining to the domain
class Domain(models.Model):
    top_level = models.CharField(max_length=10)
    domain = models.CharField(max_length=100)


# User model
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
