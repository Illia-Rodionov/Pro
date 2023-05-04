from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """User Manager."""
    def create_user(self, email=None, password=None):
        if not email:
            raise ValueError("Email address must be provided.")
        if not password:
            raise TypeError("Password must be provided")

        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email=None, password=None):
        user = self.create_user(email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
