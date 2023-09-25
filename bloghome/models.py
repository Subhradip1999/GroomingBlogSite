from django.db import models


'''
this is blog post 1st table.
'''
class BlogPostOne(models.Model):
    index = models.CharField(max_length=5)
    title = models.TextField(default="This is the Title")
    description = models.TextField(default="This is default text field")
    img_path_1 = models.CharField(max_length=100, default="img2.jpg")
    img_path_2 = models.CharField(max_length=100, default=".img2.jpg")
    img_path_3 = models.CharField(max_length=100, default="img2.jpg")
    img_1 = models.ImageField(upload_to='static/img/', null=True)
    img_2 = models.ImageField(upload_to='static/img/', null=True)
    img_3 = models.ImageField(upload_to='static/img/', null=True)
    affiliate_link = models.TextField(default="https://www.amazon.in/")

    def __str__(self):
        return self.index


'''
this is blog post 2nd table.
'''
class BlogPostTwo(models.Model):
    index = models.CharField(max_length=5)
    title = models.TextField(default="This is the Title")
    description = models.TextField(default="This is default text field")
    img_path_1 = models.CharField(max_length=100, default="img2.jpg")
    img_path_2 = models.CharField(max_length=100, default="img2.jpg")
    img_path_3 = models.CharField(max_length=100, default="img2.jpg")
    img_1 = models.ImageField(upload_to='static/img/', null=True)
    img_2 = models.ImageField(upload_to='static/img/', null=True)
    img_3 = models.ImageField(upload_to='static/img/', null=True)
    affiliate_link = models.TextField(default="https://www.amazon.in/")

    def __str__(self):
        return self.index


'''
this is blog post 3rd table.
'''
class BlogPostThree(models.Model):
    index = models.CharField(max_length=5)
    title = models.TextField(default="This is the Title")
    description = models.TextField(default="This is default text field")
    img_path_1 = models.CharField(max_length=100, default="img2.jpg")
    img_path_2 = models.CharField(max_length=100, default="img2.jpg")
    img_path_3 = models.CharField(max_length=100, default="img2.jpg")
    img_1 = models.ImageField(upload_to='static/img/', null=True)
    img_2 = models.ImageField(upload_to='static/img/', null=True)
    img_3 = models.ImageField(upload_to='static/img/', null=True)
    affiliate_link = models.TextField(default="https://www.amazon.in/")

    def __str__(self):
        return self.index


'''
this is blog post 4th table.
'''
class BlogPostFour(models.Model):
    index = models.CharField(max_length=5)
    title = models.TextField(default="This is the Title")
    description = models.TextField(default="This is default text field")
    img_path_1 = models.CharField(max_length=100, default="img2.jpg")
    img_path_2 = models.CharField(max_length=100, default="img2.jpg")
    img_path_3 = models.CharField(max_length=100, default="img2.jpg")
    img_1 = models.ImageField(upload_to='static/img/', null=True)
    img_2 = models.ImageField(upload_to='static/img/', null=True)
    img_3 = models.ImageField(upload_to='static/img/', null=True)
    affiliate_link = models.TextField(default="https://www.amazon.in/")

    def __str__(self):
        return self.index


'''
this is blog post 5th table.
'''
class BlogPostFive(models.Model):
    index = models.CharField(max_length=5)
    title = models.TextField(default="This is the Title")
    description = models.TextField(default="This is default text field")
    img_path_1 = models.CharField(max_length=100, default="img2.jpg")
    img_path_2 = models.CharField(max_length=100, default="img2.jpg")
    img_path_3 = models.CharField(max_length=100, default="img2.jpg")
    img_1 = models.ImageField(upload_to='static/img/', null=True)
    img_2 = models.ImageField(upload_to='static/img/', null=True)
    img_3 = models.ImageField(upload_to='static/img/', null=True)
    affiliate_link = models.TextField(default="https://www.amazon.in/")

    def __str__(self):
        return self.index


'''
this is blog post 6th table.
'''
class BlogPostSix(models.Model):
    index = models.CharField(max_length=5)
    title = models.TextField(default="This is the Title")
    description = models.TextField(default="This is default text field")
    img_path_1 = models.CharField(max_length=100, default="img2.jpg")
    img_path_2 = models.CharField(max_length=100, default="img2.jpg")
    img_path_3 = models.CharField(max_length=100, default="img2.jpg")
    img_1 = models.ImageField(upload_to='static/img/', null=True)
    img_2 = models.ImageField(upload_to='static/img/', null=True)
    img_3 = models.ImageField(upload_to='static/img/', null=True)
    affiliate_link = models.TextField(default="https://www.amazon.in/")

    def __str__(self):
        return self.index


'''
this is blog post 7th table.
'''
class BlogPostSeven(models.Model):
    index = models.CharField(max_length=5)
    title = models.TextField(default="This is the Title")
    description = models.TextField(default="This is default text field")
    img_path_1 = models.CharField(max_length=100, default="img2.jpg")
    img_path_2 = models.CharField(max_length=100, default="img2.jpg")
    img_path_3 = models.CharField(max_length=100, default="img2.jpg")
    img_1 = models.ImageField(upload_to='static/img/', null=True)
    img_2 = models.ImageField(upload_to='static/img/', null=True)
    img_3 = models.ImageField(upload_to='static/img/', null=True)
    affiliate_link = models.TextField(default="https://www.amazon.in/")

    def __str__(self):
        return self.index


'''
this is blog post 8th table.
'''
class BlogPostEight(models.Model):
    index = models.CharField(max_length=5)
    title = models.TextField(default="This is the Title")
    description = models.TextField(default="This is default text field")
    img_path_1 = models.CharField(max_length=100, default="img2.jpg")
    img_path_2 = models.CharField(max_length=100, default="img2.jpg")
    img_path_3 = models.CharField(max_length=100, default="img2.jpg")
    img_1 = models.ImageField(upload_to='static/img/', null=True)
    img_2 = models.ImageField(upload_to='static/img/', null=True)
    img_3 = models.ImageField(upload_to='static/img/', null=True)
    affiliate_link = models.TextField(default="https://www.amazon.in/")

    def __str__(self):
        return self.index


'''
this is blog post 9th table.
'''
class BlogPostNine(models.Model):
    index = models.CharField(max_length=5)
    title = models.TextField(default="This is the Title")
    description = models.TextField(default="This is default text field")
    img_path_1 = models.CharField(max_length=100, default="img2.jpg")
    img_path_2 = models.CharField(max_length=100, default="img2.jpg")
    img_path_3 = models.CharField(max_length=100, default="img2.jpg")
    img_1 = models.ImageField(upload_to='static/img/', null=True)
    img_2 = models.ImageField(upload_to='static/img/', null=True)
    img_3 = models.ImageField(upload_to='static/img/', null=True)
    affiliate_link = models.TextField(default="https://www.amazon.in/")

    def __str__(self):
        return self.index
