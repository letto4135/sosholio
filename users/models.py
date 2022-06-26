from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Models a top level domain and domain name
# for users to be in groups pertaining to the domain
class Domain(models.Model):
    top_level = models.CharField(max_length=10, null=True, default=None)
    domain = models.CharField(max_length=100, null=True, default=None)

    def __str__(self):
        return str(self.domain) + "." + str(self.top_level)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, default=Domain)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user_domain = instance.email.split('@')[1]
        Profile.objects.create(
            user=instance,
            domain=Domain.objects.create(
                top_level=user_domain.split('.')[1],
                domain=user_domain.split('.')[0]
            )
         )


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
