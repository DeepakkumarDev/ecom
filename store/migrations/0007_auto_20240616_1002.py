# Generated by Django 5.0.6 on 2024-06-16 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_customer_phone'),
    ]

    operations = [
        migrations.RunSQL("""
            INSERT  INTO store_collection (title)
            VALUES ('collection1')
        ""","""
            DELETE FROM store_collection
            WHERE title='collection1'
        """)
    ]
