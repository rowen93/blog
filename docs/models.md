# imports  (commands)                                       (comments)
from django.db import models                        imports the model class
from django.utils import timezone                   imports the time fuction
from django.contrib.auth.models import User         imports built in User model

## django shell - manage database
python manage.py shell 
>>> 
from blog.models import Post
from django.contrib.auth.models import User
User.objects.all()
User.objects.filter(username="TestUser")           
User.objects.filter(last_name="smith")    
User.objects.filter(username="rebecca93", last_name="owen", location="ashton")  
user = User.objects.filter(username="TestUser").first()
- gets the first item in the list and signs it to the user variable
user.id                                          
- returns the id number of that user
user.pk                                            
- returns the primary key of that user
eg. user.first_name, user.date_joined, user.is_active
user = User.objects.get(id=1)                      
- will return one object
User.objects.filter(username="TestUser")            
- will always return a list
Post.objects.all()
bec = User.objects.all().first()
Post.objects.create(title="Pocket Fitness",  content="Domain purchase complete! :)", author=bec)
to give each class a name in shell/admin do below ...
    def __str__(self):
        return self.title

 Post.objects.create(title="Pocket Fitness",  content="Domain purchase complete! :)", author_id=2)    
(title__icontains="maccies") <__icontains - this searches for upper and lower case :) strings>   
reverse foreign key look up as below (gets all posts/products/entries/pics by user)
User.objects.get(id=1).post_set.all()