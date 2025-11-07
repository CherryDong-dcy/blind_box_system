from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """自定义用户模型"""

    GENDER_CHOICES = [
        ('M', '男'),
        ('F', '女'),
        ('O', '其他'),
    ]

    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True,
        verbose_name='性别'
    )
    age = models.PositiveIntegerField(null=True, blank=True, verbose_name='年龄')

    # 添加 related_name 避免冲突
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="customuser_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="customuser_set",
        related_query_name="user",
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'