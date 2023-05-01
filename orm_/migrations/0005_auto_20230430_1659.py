# Generated by Django 3.2 on 2023-04-30 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orm_', '0004_auto_20230430_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(db_table='student_course', null=True, related_name='students', to='orm_.Course'),
        ),
        migrations.AlterField(
            model_name='student',
            name='details',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='orm_.studentdetail'),
        ),
        migrations.AlterField(
            model_name='student',
            name='stu_class',
            field=models.ForeignKey(db_column='class_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='orm_.classes'),
        ),
    ]