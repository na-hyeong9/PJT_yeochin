
from django.db import models
from datetime import datetime, timezone, timedelta
from django.conf import settings

# Create your models here.

class Qna(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="image/%Y/%m/%d", blank=True)
    hits = models.PositiveIntegerField(default=0)
    closed = models.BooleanField(default=False)
    tag = models.ManyToManyField('tag.Tag', verbose_name = "태그")
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = "community_board"
        verbose_name = "qna"
        verbose_name_plural = "qna"    
    
    @property
    def created_string(self):
        time = datetime.now(tz=timezone.utc) - self.created_at

        if time < timedelta(minutes=1):
            return "방금 전"
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + "분 전"
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + "시간 전"
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.created_at.date()
            return str(time.days) + "일 전"
        else:
            return False
        
        
    @property
    def click(self):
        self.hits += 1
        self.save()

    @property
    def full_name(self):
        return f"{self.last_name}{self.first_name}"

class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name="태그명")
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "community_tag"
        verbose_name = "태그"
        verbose_name_plural = "태그"

class Answer(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    qna = models.ForeignKey(Qna, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    @property
    def created_string(self):
        time = datetime.now(tz=timezone.utc) - self.created

        if time < timedelta(minutes=1):
            return "방금 전"
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + "분 전"
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + "시간 전"
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.created.date()
            return str(time.days) + "일 전"
        else:
            return False