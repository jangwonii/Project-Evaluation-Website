from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    average_rating = models.FloatField(default=3)
    
    def __str__(self):
        return self.title
    
    @property
    def total_ratings(self):
        return self.rating_set.count()

class Rating(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    score = models.IntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        ratings = self.project.rating_set.all()
        avg = sum(r.score for r in ratings) / ratings.count() if ratings.exists() else 0
        self.project.average_rating = avg
        self.project.save()
    
    def __str__(self):
        return f"{self.project.title} - {self.score}점"
