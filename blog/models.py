from django.db import models
from django.utils import timezone
from user.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    
    #Define Custom Manager
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status="published")
    
    options = (
        ("draft", "Draft"),
        ("published", "Published")
    )
    
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='Published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    status = models.CharField(max_length=10, choices=options, default='published')
    objects = models.Manager() #default Manager
    postobjects = PostObjects() #Custome Manager
    
    class Meta:
        ordering = ('-published',)
        
        def __str__(self):
            return self.title