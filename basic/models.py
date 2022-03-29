from django.db import models


class ModelBase(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    modified_at = models.DateTimeField(null=False, auto_now=True)
    active = models.BooleanField(null=False, default=True)

    class Meta:
        abstract = True


class Course(ModelBase):
    name = models.CharField(max_length=40, null=False)
    students = models.ManyToManyField(
        to='Student',
        through='CourseStudent',
    )

    class Meta:
        db_table = 'course'
        managed = True


class Student(ModelBase):
    name = models.CharField(max_length=100, null=False)
    courses = models.ManyToManyField(
        to='Course',
        through='CourseStudent',
    )

    class Meta:
        db_table = 'student'
        managed = True


class CourseStudent(ModelBase):
    course = models.ForeignKey(
        to='Course',
        on_delete=models.DO_NOTHING,
        db_column='id_course',
        null=False
    )
    student = models.ForeignKey(
        to='Student',
        on_delete=models.DO_NOTHING,
        db_column='id_student',
        null=False,
    )

    class Meta:
        db_table = 'course_student'
        managed = True
        unique_together = [
            ('course', 'student',)
        ]
