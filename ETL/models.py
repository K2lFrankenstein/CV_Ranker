from django.db import models
from django.contrib.auth.models import User
#UID

class JobDescription(models.Model):
    UID = models.ForeignKey(User, on_delete=models.CASCADE, related_name="uid_jd")
    jobTittle = models.CharField(max_length=200)
    jobDetails = models.CharField(max_length=50000)
    def __str__(self):
        return self.jobTittle

class StructuredFormate(models.Model):
    UID = models.ForeignKey(User, on_delete=models.CASCADE, related_name="uid")
    jobTittle = models.ForeignKey(JobDescription, null=True, blank=True, on_delete=models.CASCADE, related_name="job_tittle")
    
    resumeName = models.CharField(max_length=150)
    resumeHighlights = models.CharField(max_length=500)
    resumeScore = models.CharField(max_length=150)
    isShared = models.BooleanField(default=False)
    #cv
    skills = models.CharField(max_length=500)
    contactInfo = models.JSONField()
    experience = models.JSONField()
    others = models.JSONField(max_length=5000)
    project = models.JSONField(max_length=50000)
    education = models.JSONField()

    def __str__(self):
        return self.resumeName
