from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):
    SPECIES_CHOICES = [
        ('DOG', 'Dog'),
        ('CAT', 'Cat'),
        ('OTHER', 'Other'),
    ]
    
    STATUS_CHOICES = [
        ('AVAILABLE', 'Available'),
        ('PENDING', 'Application Processing'),
        ('ADOPTED', 'Adopted'),
    ]
    
    name = models.CharField('Name', max_length=100)
    species = models.CharField('Species', max_length=10, choices=SPECIES_CHOICES)
    age = models.IntegerField('Age')
    gender = models.CharField('Gender', max_length=10, choices=[('M', 'Male'), ('F', 'Female')])
    description = models.TextField('Description')
    image = models.ImageField('Photo', upload_to='pets/')
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, default='AVAILABLE')
    created_at = models.DateTimeField('Created At', auto_now_add=True)
    updated_at = models.DateTimeField('Updated At', auto_now=True)

    class Meta:
        verbose_name = 'Pet'
        verbose_name_plural = 'Pets'

    def __str__(self):
        return self.name

class AdoptionApplication(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending Review'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]
    
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='applications', verbose_name='Pet')
    name = models.CharField('Applicant Name', max_length=100)
    phone = models.CharField('Phone Number', max_length=20)
    email = models.EmailField('Email')
    address = models.TextField('Address')
    reason = models.TextField('Adoption Reason')
    status = models.CharField('Application Status', max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField('Application Time', auto_now_add=True)
    updated_at = models.DateTimeField('Updated At', auto_now=True)

    class Meta:
        verbose_name = 'Adoption Application'
        verbose_name_plural = 'Adoption Applications'

    def __str__(self):
        return f"{self.name} - {self.pet.name}"

class VolunteerApplication(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending Review'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]

    name = models.CharField('Name', max_length=100)
    email = models.EmailField('Email')
    phone = models.CharField('Phone Number', max_length=20)
    location  = models.CharField(
        'Location',
        max_length=100,
        default='',    
        blank=True
    )
    interests = models.JSONField(
        'Interests',
        default=list,   
        blank=True
    )
    experience = models.TextField('Experience')
    availability = models.TextField('Availability')
    motivation = models.TextField('Motivation')
    status = models.CharField(
        'Status',
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )
    created_at = models.DateTimeField('Created At', auto_now_add=True)
    updated_at = models.DateTimeField('Updated At', auto_now=True)

    class Meta:
        verbose_name = 'Volunteer Application'
        verbose_name_plural = 'Volunteer Applications'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.get_status_display()})"