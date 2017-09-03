from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class Project(models.Model):
    category=models.CharField(max_length=120)
    title=models.CharField(max_length=120)
    image=models.ImageField()
    abstract=models.TextField(max_length=1200)
    cid=models.IntegerField()
    abstract_pdf=models.FileField(null=True,blank=True)

    def get_absolute_url(self):
        return reverse("project:projectdetail",kwargs={"id",self.id})

    def __str__(self):
        a= str(self.pk) +" "+ str(self.title)
        return a