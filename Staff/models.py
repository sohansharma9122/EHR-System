from django.db import models

# Create your models here.
class Laboratory_test(models.Model):
    test_id=models.AutoField(primary_key=True)
    test_name=models.CharField(max_length=30)
    test_Price=models.IntegerField(default=10)

    def __str__(self):
        return self.test_name
