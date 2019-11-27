from django.db import models

EMPLOYEES = (
    ('avnish','AVNISH'),
    ('akhilesh', 'AKHILESH'),
    ('smijith','SMIJITH'),
    ('vinod','VINOD'),
    ('ankur','ANKUR'),
)


class Task(models.Model):
    taskid = models.AutoField(primary_key=True)
    taskdesc = models.CharField(max_length=1000)
    assigned_to = models.CharField(max_length=16, choices=EMPLOYEES)
    deadline = models.DateField(max_length=20)
    class Meta:
        db_table = "task"
