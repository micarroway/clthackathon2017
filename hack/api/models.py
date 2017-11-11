from django.db import models


class Patient(models.Model):
    PatientId = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=150)
    MiddleName = models.CharField(max_length=150, null=True)
    LastName = models.CharField(max_length=150)
    UserName = models.CharField(max_length=150)
    DateOfBirth = models.DateField()
    Gender = models.CharField(max_length=2)
    Race = models.CharField(max_length=10)
    Ethnicity = models.CharField(max_length=10)


class PatientAddress(models.Model):
    PatientAddressId = models.AutoField(primary_key=True)
    Patient = models.ForeignKey(Patient, related_name='addresses', on_delete=models.CASCADE)
    StreetAddress1 = models.CharField(max_length=100)
    StreetAddress2 = models.CharField(max_length=100, null=True)
    City = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    PostalCode = models.CharField(max_length=100)


class PatientInsurance(models.Model):
    PatientInsuranceId = models.AutoField(primary_key=True)
    Patient = models.ForeignKey(Patient, related_name='insurances', on_delete=models.CASCADE)
    PremiumType = models.CharField(max_length=10)
    PremiumCost = models.DecimalField(max_digits=23, decimal_places=2)


class PatientOccupation(models.Model):
    PatientOccupationId = models.AutoField(primary_key=True)
    Patient = models.ForeignKey(Patient, related_name='occupations', on_delete=models.CASCADE)
    CompanyName = models.CharField(max_length=100)
    CompanyLocation = models.CharField(max_length=100)
    PositionTitle = models.CharField(max_length=100)
    Salary = models.DecimalField(max_digits=23, decimal_places=2)


class Symptom(models.Model):
    SymptomId = models.AutoField(primary_key=True)
    Symptom = models.CharField(max_length=100)
    SymptomDescription = models.CharField(max_length=4000)


class Diagnosis(models.Model):
    DiagnosisId = models.AutoField(primary_key=True)
    DiagnosisDescription = models.CharField(max_length=4000)
    Symptom = models.ManyToManyField(Symptom)


class Facility(models.Model):
    FacilityId = models.AutoField(primary_key=True)
    FacilityName = models.CharField(max_length=4000)
    FacilityType = models.CharField(max_length=200)
    NumberOfPhysicians = models.IntegerField()


class FacilityAddress(models.Model):
    FacilityAddressId = models.AutoField(primary_key=True)
    Facility = models.ForeignKey(Facility, related_name='addresses', on_delete=models.CASCADE)
    StreetAddress1 = models.CharField(max_length=100)
    StreetAddress2 = models.CharField(max_length=100, null=True)
    City = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    PostalCode = models.CharField(max_length=100)


class InsuranceCompany(models.Model):
    InsuranceCompanyId = models.AutoField(primary_key=True)
    CompanyName = models.CharField(max_length=4000)
    StreetAddress1 = models.CharField(max_length=100)
    StreetAddress2 = models.CharField(max_length=100, null=True)
    City = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    PostalCode = models.CharField(max_length=100)


class PatientMedicalHistory(models.Model):
    PatientMedicalHistoryId = models.AutoField(primary_key=True)
    Patient = models.ForeignKey(Patient, related_name='history', on_delete=models.CASCADE)
    Facility = models.ForeignKey(Facility, related_name='history', on_delete=models.CASCADE)
    InsuranceCompany = models.ForeignKey(InsuranceCompany, related_name='history', on_delete=models.CASCADE)
    Diagnosis = models.ManyToManyField(Diagnosis)
    Symptom = models.ManyToManyField(Symptom)
    DateOfVisit = models.DateField()
    CostOfVisit = models.DecimalField(max_digits=23, decimal_places=2)
    InsurancePercentage = models.DecimalField(max_digits=11, decimal_places=10)
