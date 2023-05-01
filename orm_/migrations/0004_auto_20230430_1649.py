# Generated by Django 3.2 on 2023-04-30 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orm_', '0003_alter_student_stu_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(db_table='student_course', null=True, related_name='stu', to='orm_.Course'),
        ),
        migrations.AlterField(
            model_name='student',
            name='details',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stu', to='orm_.studentdetail'),
        ),
        migrations.AlterField(
            model_name='student',
            name='stu_class',
            field=models.ForeignKey(db_column='class_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stu', to='orm_.classes'),
        ),
    ]
