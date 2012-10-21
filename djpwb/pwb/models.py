from django.db import models


class Poll(models.Model):
    question = models.CharField(max_length=200, help_text='Your Text')
    pub_date = models.DateTimeField(auto_now_add=True)
    publication_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()


    def __unicode__(self):
        return self.choice

class employee(models.Model):
    first_name  =models.CharField(max_length=200, primary_key=True)
    shirt_sizes =(
        ('S', 'Small'),
        ('M','Medium'),
        ('L','Large'),
        )
    size = models.CharField(max_length=2, choices = shirt_sizes,db_column='emp_size')
    fresh = models.BooleanField(default=True)
    Employment_level=(
        ('JR', 'Junior'),
        ('SN','Senior'),
        ('EX','Executive'),
        ('MG','Manager'),
    )
    type =models.CharField(max_length=2, choices = Employment_level)
