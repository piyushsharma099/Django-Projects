from django.db import models

# Create your models here.
# class branch(models.Model):
#     branch=models.CharField(max_length=10,null=False)

#     def __str__(self):
#         return self.name

# class session(models.Model):
#     session=models.IntegerField(default=0)

#     def __str__(self):
#         return self.name


class student(models.Model):
    title=models.CharField(max_length=30)
    co_name=models.CharField(max_length=20)
    abstract=models.CharField(max_length=200)
    branch=models.CharField(max_length=10)
    session=models.IntegerField(default=0)
    # session=models.ForeignKey(session,on_delete=models.CASCADE)  
    team_m=models.CharField(max_length=40)

    def __str__(self):
        return "%s %s %s %s %s %s" %(self.title ,self.co_name,self.abstract,self.branch,self.session,self.team_m)
