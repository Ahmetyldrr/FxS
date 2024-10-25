# Generated by Django 4.2.7 on 2024-10-23 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('basemodels', '0002_match'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StatisticsItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('home_value', models.FloatField(blank=True, null=True)),
                ('away_value', models.FloatField(blank=True, null=True)),
                ('home_total', models.IntegerField(blank=True, null=True)),
                ('away_total', models.IntegerField(blank=True, null=True)),
                ('compare_code', models.IntegerField(blank=True, null=True)),
                ('statistics_type', models.CharField(blank=True, max_length=50, null=True)),
                ('value_type', models.CharField(blank=True, max_length=50, null=True)),
                ('render_type', models.IntegerField(blank=True, null=True)),
                ('key', models.CharField(max_length=100)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='statistics_items', to='analiztest.group')),
            ],
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period_name', models.CharField(max_length=10)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='periods', to='basemodels.match')),
            ],
        ),
        migrations.CreateModel(
            name='PercentValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_percentage', models.FloatField(blank=True, null=True)),
                ('away_percentage', models.FloatField(blank=True, null=True)),
                ('home_total', models.IntegerField(blank=True, null=True)),
                ('away_total', models.IntegerField(blank=True, null=True)),
                ('statistics_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='percent_values', to='analiztest.statisticsitem')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='analiztest.period'),
        ),
    ]
