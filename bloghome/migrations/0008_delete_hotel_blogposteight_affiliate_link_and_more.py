# Generated by Django 4.2.2 on 2023-07-09 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloghome', '0007_blogpostfour_affiliate_link_blogpostfour_img_1_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Hotel',
        ),
        migrations.AddField(
            model_name='blogposteight',
            name='affiliate_link',
            field=models.TextField(default='https://www.amazon.in/'),
        ),
        migrations.AddField(
            model_name='blogposteight',
            name='img_1',
            field=models.ImageField(null=True, upload_to='static/img/'),
        ),
        migrations.AddField(
            model_name='blogposteight',
            name='img_2',
            field=models.ImageField(null=True, upload_to='static/img/'),
        ),
        migrations.AddField(
            model_name='blogposteight',
            name='img_3',
            field=models.ImageField(null=True, upload_to='static/img/'),
        ),
        migrations.AddField(
            model_name='blogpostfive',
            name='affiliate_link',
            field=models.TextField(default='https://www.amazon.in/'),
        ),
        migrations.AddField(
            model_name='blogpostfive',
            name='img_1',
            field=models.ImageField(null=True, upload_to='static/img/'),
        ),
        migrations.AddField(
            model_name='blogpostfive',
            name='img_2',
            field=models.ImageField(null=True, upload_to='static/img/'),
        ),
        migrations.AddField(
            model_name='blogpostfive',
            name='img_3',
            field=models.ImageField(null=True, upload_to='static/img/'),
        ),
        migrations.AddField(
            model_name='blogpostnine',
            name='affiliate_link',
            field=models.TextField(default='https://www.amazon.in/'),
        ),
        migrations.AddField(
            model_name='blogpostnine',
            name='img_1',
            field=models.ImageField(null=True, upload_to='static/img/'),
        ),
        migrations.AddField(
            model_name='blogpostnine',
            name='img_2',
            field=models.ImageField(null=True, upload_to='static/img/'),
        ),
        migrations.AddField(
            model_name='blogpostnine',
            name='img_3',
            field=models.ImageField(null=True, upload_to='static/img/'),
        ),
        migrations.AddField(
            model_name='blogpostone',
            name='affiliate_link',
            field=models.TextField(default='https://www.amazon.in/'),
        ),
        migrations.AddField(
            model_name='blogpostone',
            name='img_1',
            field=models.ImageField(null=True, upload_to='static/img/'),
        ),
        migrations.AddField(
            model_name='blogpostone',
            name='img_2',
            field=models.ImageField(null=True, upload_to='static/img/'),
        ),
        migrations.AddField(
            model_name='blogpostone',
            name='img_3',
            field=models.ImageField(null=True, upload_to='static/img/'),
        ),
        migrations.AddField(
            model_name='blogpostseven',
            name='affiliate_link',
            field=models.TextField(default='https://www.amazon.in/'),
        ),
        migrations.AddField(
            model_name='blogpostseven',
            name='img_1',
            field=models.ImageField(null=True, upload_to='static/img/'),
        ),
        migrations.AddField(
            model_name='blogpostseven',
            name='img_2',
            field=models.ImageField(null=True, upload_to='static/img/'),
        ),
        migrations.AddField(
            model_name='blogpostseven',
            name='img_3',
            field=models.ImageField(null=True, upload_to='static/img/'),
        ),
        migrations.AddField(
            model_name='blogpostsix',
            name='affiliate_link',
            field=models.TextField(default='https://www.amazon.in/'),
        ),
        migrations.AddField(
            model_name='blogpostsix',
            name='img_1',
            field=models.ImageField(null=True, upload_to='static/img/'),
        ),
        migrations.AddField(
            model_name='blogpostsix',
            name='img_2',
            field=models.ImageField(null=True, upload_to='static/img/'),
        ),
        migrations.AddField(
            model_name='blogpostsix',
            name='img_3',
            field=models.ImageField(null=True, upload_to='static/img/'),
        ),
        migrations.AddField(
            model_name='blogposttwo',
            name='affiliate_link',
            field=models.TextField(default='https://www.amazon.in/'),
        ),
        migrations.AddField(
            model_name='blogposttwo',
            name='img_1',
            field=models.ImageField(null=True, upload_to='static/img/'),
        ),
        migrations.AddField(
            model_name='blogposttwo',
            name='img_2',
            field=models.ImageField(null=True, upload_to='static/img/'),
        ),
        migrations.AddField(
            model_name='blogposttwo',
            name='img_3',
            field=models.ImageField(null=True, upload_to='static/img/'),
        ),
        migrations.AlterField(
            model_name='blogposteight',
            name='description',
            field=models.TextField(default='This is default text field'),
        ),
        migrations.AlterField(
            model_name='blogpostfive',
            name='description',
            field=models.TextField(default='This is default text field'),
        ),
        migrations.AlterField(
            model_name='blogpostnine',
            name='description',
            field=models.TextField(default='This is default text field'),
        ),
        migrations.AlterField(
            model_name='blogpostone',
            name='description',
            field=models.TextField(default='This is default text field'),
        ),
        migrations.AlterField(
            model_name='blogpostseven',
            name='description',
            field=models.TextField(default='This is default text field'),
        ),
        migrations.AlterField(
            model_name='blogpostsix',
            name='description',
            field=models.TextField(default='This is default text field'),
        ),
        migrations.AlterField(
            model_name='blogposttwo',
            name='description',
            field=models.TextField(default='This is default text field'),
        ),
    ]
