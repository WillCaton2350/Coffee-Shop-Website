from django.db import models as m

class review_Models(m.Model):
    name= m.CharField(max_length=255)
    email= m.CharField(max_length=255)
    phone= m.IntegerField()
    review= m.CharField(max_length=255)