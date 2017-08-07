# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField(timezone.now())
	def __str__(self):
		return self.question_text

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text
# u can either create an object of class chioce and then give it attribues like:
# choice = Choice()
# choice.question = question1
# choice.choice_text = kdna
# choice.votes = adkjfd

# or

# question1.choice_set.all()
# question1.choice_set.create(attribute_assignment)
# question1.choice_set.count()
