from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db.models import CharField, DateField, URLField, BooleanField, TextField, ImageField, Model, EmailField, \
    SlugField, ForeignKey, PROTECT, JSONField
from django.utils.text import slugify


class User(AbstractUser):
    job = CharField(max_length=255)
    birthday = DateField(auto_created=True)
    website = URLField(max_length=255)
    phone = CharField(max_length=18)
    city = CharField(max_length=255)
    degree = CharField(max_length=255)
    freelance = BooleanField(default=False)
    types = ArrayField(CharField(max_length=255), blank=True, null=True)
    about = TextField()
    image = ImageField(upload_to='profile/')
    social = JSONField(max_length=255)

    @property
    def age(self):
        today = datetime.today()
        return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))


class Message(Model):
    name = CharField(max_length=255)
    email = EmailField(max_length=255)
    subject = CharField(max_length=255)
    message = TextField()


class Category(Model):
    title = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            while Project.objects.filter(slug=self.slug).exists():
                slug = Project.objects.filter(slug=self.slug).first().slug
                if '-' in slug:
                    try:
                        if slug.split('-')[-1] in self.title:
                            self.slug += '-1'
                        else:
                            self.slug = '-'.join(slug.split('-')[:-1]) + '-' + str(int(slug.split('-')[-1]) + 1)
                    except:
                        self.slug = slug + '-1'
                else:
                    self.slug += '-1'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Project(Model):
    title = CharField(max_length=255)
    description = TextField()
    project_date = CharField(max_length=255)
    url = URLField(max_length=255)
    client = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True)
    category = ForeignKey(Category, PROTECT)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            while Project.objects.filter(slug=self.slug).exists():
                slug = Project.objects.filter(slug=self.slug).first().slug
                if '-' in slug:
                    try:
                        if slug.split('-')[-1] in self.title:
                            self.slug += '-1'
                        else:
                            self.slug = '-'.join(slug.split('-')[:-1]) + '-' + str(int(slug.split('-')[-1]) + 1)
                    except:
                        self.slug = slug + '-1'
                else:
                    self.slug += '-1'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ImageList(Model):
    project = ForeignKey(Project, PROTECT, related_name='photos')
    image = ImageField(upload_to='photos/')


class Skill(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name
