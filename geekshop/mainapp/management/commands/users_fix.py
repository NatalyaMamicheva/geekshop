from django.core.management import BaseCommand

from authapp.models import ShopUser, ShopUserProfile


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for user in ShopUser.objects.all():
            user_profile = ShopUserProfile.objects.create(user=user)
            user_profile.save()