from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0036_certificate_datarequest_dupc_links_riccouncil_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('faq_url', models.URLField()),
        ('feedback_url', models.URLField()),
            ],
        ),
    ]