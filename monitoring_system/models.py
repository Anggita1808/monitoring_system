from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=255)

class StatusProject(models.Model):
    nama = models.CharField(max_length=255)

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    technical_skill = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=[("Internal", "Internal"), ("External", "External")])
    foto_profil = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    join_date = models.DateField()
    short_bio = models.TextField()
    gender = models.CharField(max_length=255, choices=[("Male", "Male"), ("Female", "Female")])
    department = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    linkedin_profile = models.CharField(max_length=255)
    github_profile = models.CharField(max_length=255)
    additional_info = models.TextField()
    date_joined = models.DateField()
    last_login = models.DateTimeField()
    account_status = models.CharField(max_length=255, choices=[("Active", "Active"), ("Inactive", "Inactive")])

class Title(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_id = models.CharField(max_length=255)

class Client(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    pic_phone = models.CharField(max_length=255)
    pic_email = models.CharField(max_length=255)
    pic_title = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    website_url = models.CharField(max_length=255)
    logo = models.CharField(max_length=255)
    company_size = models.IntegerField()
    company_address = models.CharField(max_length=255)
    contact_person_name = models.CharField(max_length=255)
    company_email = models.CharField(max_length=255)
    company_phone = models.CharField(max_length=255)
    additional_info = models.TextField()
    date_joined = models.DateField()
    status = models.CharField(max_length=255, choices=[("Aktif", "Aktif"), ("Tidak", "Tidak"), ("Hibernasi", "Hibernasi")])
    last_activity = models.DateTimeField()

class Project(models.Model):
    year = models.IntegerField()
    pid = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.ForeignKey(StatusProject, on_delete=models.CASCADE)
    customer = models.ForeignKey(Client, related_name='customer_projects', on_delete=models.CASCADE)
    end_user = models.ForeignKey(Client, related_name='end_user_projects', on_delete=models.CASCADE)
    sales = models.ForeignKey(User, related_name='sales_projects', on_delete=models.CASCADE)
    pm = models.ForeignKey(User, related_name='pm_projects', on_delete=models.CASCADE)
    am = models.ForeignKey(User, related_name='am_projects', on_delete=models.CASCADE)
    pic = models.ForeignKey(User, related_name='pic_projects', on_delete=models.CASCADE)
    contract_no = models.CharField(max_length=255)
    contract_date = models.DateField()
    amount_tax = models.IntegerField()
    amount_exc_tax = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    top = models.CharField(max_length=255)
    sow = models.CharField(max_length=255)
    oos = models.CharField(max_length=255)
    detail = models.CharField(max_length=255)
    remarks = models.CharField(max_length=255)
    weight = models.IntegerField()
    priority = models.CharField(max_length=255, choices=[("tinggi", "tinggi"), ("rendah", "rendah"), ("sedang", "sedang")])
    type = models.CharField(max_length=255)
    market_segment = models.CharField(max_length=255)
    tech_use = models.TextField()
    resiko = models.CharField(max_length=255)
    completion_percentage = models.IntegerField()

class EngineerAllocation(models.Model):
    engineer = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    nama_engineer = models.CharField(max_length=255)
    allocation_percentage = models.IntegerField()

class Payment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    payment_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.TextField()
    payer_name = models.CharField(max_length=255)
    payer_account_number = models.CharField(max_length=255)
    receiver_name = models.CharField(max_length=255)
    receiver_account_number = models.CharField(max_length=255)

# class FinancePO(models.Model):
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     date = models.DateField()
#     po = models.CharField(max_length=255)
#     invoice_number = models.CharField(max_length=255)
#     status = models.ForeignKey(StatusProject, on_delete=models.CASCADE)
#     dop = models.DateField()
#     note = models.TextField()
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     receiver_name = models.CharField(max_length=255)
#     receiver_account_number = models.CharField(max_length=255)
#     payer_name = models.CharField(max_length=255)
#     payer_account_number = models.CharField(max_length=255)

class Invoice(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    to_contact = models.ForeignKey(Client, on_delete=models.CASCADE)
    sent_date = models.DateField()
    due_date = models.DateField()
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=255, choices=[("belum dibayar", "belum dibayar"), ("dibayar", "dibayar"), ("overdue", "overdue")])
    note = models.TextField()
    document_file = models.CharField(max_length=255)

# class FinancialTransaction(models.Model):
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     date = models.DateField()
#     transaction_type = models.CharField(max_length=255)
#     status = models.CharField(max_length=255, choices=[("belum dibayar", "belum dibayar"), ("dibayar", "dibayar"), ("overdue", "overdue")])
#     dop = models.DateField()
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     note = models.TextField()

class ProjectAction(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date_submit = models.DateField()
    date_mulai = models.DateField()
    date_selesai = models.DateField()
    description = models.CharField(max_length=255)
    estimated_completion_date = models.DateField()
    note = models.TextField()
    status = models.ForeignKey(StatusProject, on_delete=models.CASCADE)
    assigned_engineer_id = models.ForeignKey(User, related_name='assigned_engineer_id_actions', on_delete=models.CASCADE)
    assigned_engineer_id_other = models.ForeignKey(User, related_name='assigned_engineer_id_other_actions', on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, related_name='user_id_actions', on_delete=models.CASCADE)
    category = models.CharField(max_length=255)

class ProjectNote(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    recipient_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(max_length=255)
    attachment_url = models.CharField(max_length=255)

class ProjectDocument(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    uploader_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    upload_date = models.DateField()
    document_file = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
