from django.db import models
from django_tenants.models import TenantMixin, DomainMixin


# Create your models here.
class Company(TenantMixin):
    name = models.CharField('テナント名', max_length=127)


class Domain(DomainMixin):
    pass
