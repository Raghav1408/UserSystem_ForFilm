from django.db import models
from django.contrib.auth.models import(
    BaseUserManager, AbstractBaseUser
)
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False, is_crew=False,is_producer=False,is_talent=False,is_service_provider=False):
        " Create and save a user with email id and password "
        if not email:
            raise ValueError('Email address error!')
        if not password:
            raise ValueError('Password error!')

        user_obj = self.model(email=self.normalize_email(email))
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.crew=is_crew
        user_obj.talent=is_talent
        user_obj.producer=is_producer
        user_obj.service_provider=is_service_provider
        user_obj.save(using=self._db)
        return user_obj


    def create_staffuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=300, unique=True,default='123@gmail.com')

#Boolen Flags to determine user is active/inactive and User access to various dashboard

    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    crew = models.BooleanField(default=False)
    talent = models.BooleanField(default=False)
    producer = models.BooleanField(default=False)
    service_provider = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    object = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    @property
    def is_crew(self):
        return self.crew

    @property
    def is_talent(self):
        return self.talent

    @property
    def is_producer(self):
        return self.producer

    @property
    def is_service_provider(self):
        return self.service_provider
