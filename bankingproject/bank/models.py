from django.db import models
from django.urls import reverse


# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='branch', blank=True)

    def get_url(self):
        return reverse('bank:district_by_branch', args=[self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = 'branch'
        verbose_name_plural = 'Branches'

    def __str__(self):
        return '{}'.format(self.name)

class District(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='district',blank=True)
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('bank:disbradetail',args=[self.branch.slug,self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = 'district'
        verbose_name_plural = 'Districts'

    def  __str__(self):
        return '{}' .format(self.name)