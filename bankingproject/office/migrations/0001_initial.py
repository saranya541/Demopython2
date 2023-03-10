# Generated by Django 4.1.3 on 2023-02-11 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(choices=[('malappuram', 'malappuram'), ('eranakkulam', 'eranakkulam'), ('kozhikode', 'kozhikode'), ('wayanad', 'wayanad'), ('thrissur', 'thrissur')], max_length=50)),
                ('district', models.CharField(choices=[('Vengara', 'Vengara'), ('Kottakkal', 'Kottakkal'), ('Perithalmanna', 'Perithalmanna'), ('Edappal', 'Edappal'), ('Manjeri', 'Manjeri'), ('Aluva', 'Aluva'), ('Kochi', 'Kochi'), ('Muvattuppuzha', 'Muvattuppuzha'), ('Paravur', 'Paravur'), ('Angamaly', 'Angamaly'), ('Mavoor', 'Mavoor'), ('Mukkam', 'Mukkam'), ('Koyilandi', 'Koyilandi'), ('Ramanattukara', 'Ramanattukara'), ('Feroke', 'Feroke'), ('Mananthavady', 'Mananthavady'), ('kalpetta', 'kalpetta'), ('Panamaram', 'Panamaram'), ('Chavakkad', 'Chavakkad'), ('Chalakkudy', 'Chalakkudy'), ('Irinjalakuda', 'Irinjalakuda')], max_length=50)),
            ],
        ),
    ]
