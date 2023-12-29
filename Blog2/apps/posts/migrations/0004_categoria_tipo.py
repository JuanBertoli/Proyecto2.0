# Generated by Django 5.0 on 2023-12-29 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_remove_comentario_post_alter_categoria_nombre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='tipo',
            field=models.CharField(choices=[('H', 'Hombre'), ('M', 'Mujer'), ('N', 'Niño'), ('O', 'Oferta')], default="'H'", max_length=1),
            preserve_default=False,
        ),
    ]