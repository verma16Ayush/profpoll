from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save

class Professor(models.Model):
    DEPT_CHOICES = (
        ('archi', 'architecture' ),
        ('msc', 'material-science-engineering'),
        ('chemee', 'chemical-engineering'),
        ('che', 'chemistry'),
        ('ce', 'civil-engineering'),
        ('cse', 'computer-science-engineering'),
        ('ee', 'electrical-engineering'),
        ('ece', 'electronics-communication-engineering'),
        ('hs', 'humanities-social-sciences'),
        ('math', 'mathematics'),
        ('mech', 'mechanical-engineering'),
        ('phy', 'physics',),
        ('man', 'management-studies'),
    )


    name = models.CharField(max_length=200, blank=True, null=True)
    dept = models.CharField(max_length=200, blank=True, null=True, choices=DEPT_CHOICES)
    designation = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    portfolio_url = models.URLField(max_length=800, null=True, blank=True)

    def __str__(self):
        return self.name



class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    karma = models.IntegerField(null=False, blank=False, default=0)
    bio = models.TextField(null=True, blank=True, max_length=250)
    def __str__(self):
        return self.user.username


class Comment(models.Model):
    prof = models.ForeignKey(Professor, null=True, on_delete=models.CASCADE)
    stud = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
    content = models.TextField(max_length=1500, null=True, blank=True, editable=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.stud.user.username + '\'s review of ' + self.prof.name
    

class Upvotes(models.Model):
    VOTE_CHOICES = (
        (1, 'upvote'),
        (-1, 'downvote'),
    )
    user_id = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
    comment_id = models.ForeignKey(Comment, null=True, on_delete=models.CASCADE)
    value = models.IntegerField(null=True, blank=True, choices=VOTE_CHOICES)

    def __str__(self):
        return str(self.id)


class Ratings(models.Model):
    RATING_CHOICES = (
        (0, 'worst'),
        (1, 'bad'),
        (2, 'ok'),
        (3, 'nice'),
        (4, 'good'),
        (5, 'best'),
    )
    user_id = models.ForeignKey(Student, null=True, on_delete=models.CASCADE, unique=True)
    prof_id = models.ForeignKey(Professor, null=True, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    rating = models.IntegerField(default=0, null=False, blank=False, choices=RATING_CHOICES)

    def __str__(self):
        return str(self.id)


def create_student(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)

post_save.connect(create_student, sender=User)