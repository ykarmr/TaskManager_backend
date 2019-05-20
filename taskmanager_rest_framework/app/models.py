from django.db import models
from phone_field import PhoneField
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=32)
    mail = models.EmailField()
    phone = PhoneField(blank=True, help_text='Contact phone number')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        # 主キーとnameを表示させて見やすくする
        # ex) 1: Alice
        return "{}: {}".format(self.pk, self.name)

    __str__ = __repr__  # __str__にも同じ関数を適用

class Group(models.Model):
        name = models.CharField(max_length=32)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __repr__(self):
            # 主キーとnameを表示させて見やすくする
            # ex) 1: Alice
            return "{}: {}".format(self.pk, self.name)

        __str__ = __repr__  # __str__にも同じ関数を適用

class User_Joined_Group(models.Model):
    group=models.ForeignKey(Group,on_delete=models.PROTECT)
    user=models.ForeignKey(User,on_delete=models.PROTECT)

class User_Has_Task(models.Model):
    task_name = models.CharField(max_length=32)
    comment=models.TextField(blank=True)
    user=models.ForeignKey(User,on_delete=models.PROTECT)
