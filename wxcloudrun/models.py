from datetime import datetime

from django.db import models


# Roll a dice model
class Rolls(models.Model):
    id = models.AutoField
    discount = models.IntegerField(max_length=11, default=10)
    createdAt = models.DateTimeField(default=datetime.now(), )
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Rolls'  # 数据库表名