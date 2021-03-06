from django.contrib.auth.models import AbstractBaseUser, User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from . import manager
class User(AbstractBaseUser):
    first_name = models.CharField(_('first name'), max_length=254, blank=False)
    last_name = models.CharField(_('last name'), max_length=254, blank=False)

    email = models.EmailField(_('email address'), max_length=254, unique=True, blank=False)
    phone_number = models.CharField(_('phone_number'), max_length=20, blank=True, default="")

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    USER_TYPE = (
        ('P', 'Paid'),
        ('N', 'Normal'),
    )

    user_type = models.CharField(max_length=1, choices=USER_TYPE, default="N")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="M")
    dob = models.DateField(_('dob'), blank=True, default="9999-01-01")

    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin site.'))

    is_active = models.BooleanField(_('active'), default=False, help_text=_('Designates whether this user should be treated as active. '
                                                                            'Unselect this instead of deleting accounts.'))

    objects = manager.CustomUserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        parts = [self.first_name, self.middle_name, self.last_name]
        return " ".join(x for x in parts if x)

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])

    def password_change(self):
        password = User.objects.make_random_password()
        self.set_password(password)

    def save(self, *args, **kwargs):
        """
        Override save to add User password and send mail for password change
        """
        super(User, self).save(*args, **kwargs)

    def forgot_password(self, *args, **kwargs):
        """
        send random password and link the password edit form
        """

        User.password_change(self)
        super(User, self).save(*args, **kwargs)

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name.strip()

    @property
    def is_superuser(self):
        return self.is_staff

    @property
    def is_admin(self):
        return self.is_staff

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff
