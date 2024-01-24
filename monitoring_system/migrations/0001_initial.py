# Generated by Django 5.0.1 on 2024-01-24 06:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('pic_phone', models.CharField(max_length=255)),
                ('pic_email', models.CharField(max_length=255)),
                ('pic_title', models.CharField(max_length=255)),
                ('industry', models.CharField(max_length=255)),
                ('website_url', models.CharField(max_length=255)),
                ('logo', models.CharField(max_length=255)),
                ('company_size', models.IntegerField()),
                ('company_address', models.CharField(max_length=255)),
                ('contact_person_name', models.CharField(max_length=255)),
                ('company_email', models.CharField(max_length=255)),
                ('company_phone', models.CharField(max_length=255)),
                ('additional_info', models.TextField()),
                ('date_joined', models.DateField()),
                ('status', models.CharField(choices=[('Aktif', 'Aktif'), ('Tidak', 'Tidak'), ('Hibernasi', 'Hibernasi')], max_length=255)),
                ('last_activity', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StatusProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('pid', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('contract_no', models.CharField(max_length=255)),
                ('contract_date', models.DateField()),
                ('amount_tax', models.IntegerField()),
                ('amount_exc_tax', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('top', models.CharField(max_length=255)),
                ('sow', models.CharField(max_length=255)),
                ('oos', models.CharField(max_length=255)),
                ('detail', models.CharField(max_length=255)),
                ('remarks', models.CharField(max_length=255)),
                ('weight', models.IntegerField()),
                ('priority', models.CharField(choices=[('tinggi', 'tinggi'), ('rendah', 'rendah'), ('sedang', 'sedang')], max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('market_segment', models.CharField(max_length=255)),
                ('tech_use', models.TextField()),
                ('resiko', models.CharField(max_length=255)),
                ('completion_percentage', models.IntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_projects', to='monitoring_system.client')),
                ('end_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='end_user_projects', to='monitoring_system.client')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring_system.statusproject')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('note', models.TextField()),
                ('payer_name', models.CharField(max_length=255)),
                ('payer_account_number', models.CharField(max_length=255)),
                ('receiver_name', models.CharField(max_length=255)),
                ('receiver_account_number', models.CharField(max_length=255)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring_system.project')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent_date', models.DateField()),
                ('due_date', models.DateField()),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('belum dibayar', 'belum dibayar'), ('dibayar', 'dibayar'), ('overdue', 'overdue')], max_length=255)),
                ('note', models.TextField()),
                ('document_file', models.CharField(max_length=255)),
                ('to_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring_system.client')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring_system.project')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('technical_skill', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('Internal', 'Internal'), ('External', 'External')], max_length=255)),
                ('foto_profil', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('join_date', models.DateField()),
                ('short_bio', models.TextField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('linkedin_profile', models.CharField(max_length=255)),
                ('github_profile', models.CharField(max_length=255)),
                ('additional_info', models.TextField()),
                ('date_joined', models.DateField()),
                ('last_login', models.DateTimeField()),
                ('account_status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=255)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring_system.role')),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_id', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring_system.user')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('author', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('category', models.CharField(max_length=255)),
                ('attachment_url', models.CharField(max_length=255)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring_system.project')),
                ('recipient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring_system.user')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('upload_date', models.DateField()),
                ('document_file', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring_system.project')),
                ('uploader_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring_system.user')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_submit', models.DateField()),
                ('date_mulai', models.DateField()),
                ('date_selesai', models.DateField()),
                ('description', models.CharField(max_length=255)),
                ('estimated_completion_date', models.DateField()),
                ('note', models.TextField()),
                ('category', models.CharField(max_length=255)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring_system.project')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring_system.statusproject')),
                ('assigned_engineer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_engineer_id_actions', to='monitoring_system.user')),
                ('assigned_engineer_id_other', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_engineer_id_other_actions', to='monitoring_system.user')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id_actions', to='monitoring_system.user')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='am',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='am_projects', to='monitoring_system.user'),
        ),
        migrations.AddField(
            model_name='project',
            name='pic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pic_projects', to='monitoring_system.user'),
        ),
        migrations.AddField(
            model_name='project',
            name='pm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pm_projects', to='monitoring_system.user'),
        ),
        migrations.AddField(
            model_name='project',
            name='sales',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales_projects', to='monitoring_system.user'),
        ),
        migrations.CreateModel(
            name='EngineerAllocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_engineer', models.CharField(max_length=255)),
                ('allocation_percentage', models.IntegerField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring_system.project')),
                ('engineer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring_system.user')),
            ],
        ),
    ]
