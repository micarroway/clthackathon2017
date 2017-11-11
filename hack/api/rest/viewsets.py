from .serializers import *
from rest_framework import viewsets


class PatientAddressViewSet(viewsets.ModelViewSet):
    queryset = PatientAddress.objects.all()
    serializer_class = PatientAddressSerializer


class PatientInsuranceViewSet(viewsets.ModelViewSet):
    queryset = PatientInsurance.objects.all()
    serializer_class = PatientInsuranceSerializer


class PatientOccupationViewSet(viewsets.ModelViewSet):
    queryset = PatientOccupation.objects.all()
    serializer_class = PatientOccupationSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class SymptomViewSet(viewsets.ModelViewSet):
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer


class DiagnosisViewSet(viewsets.ModelViewSet):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer


class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer


class FacilityAddressViewSet(viewsets.ModelViewSet):
    queryset = FacilityAddress.objects.all()
    serializer_class = FacilityAddressSerializer


class InsuranceCompanyViewSet(viewsets.ModelViewSet):
    queryset = InsuranceCompany.objects.all()
    serializer_class = InsuranceCompanySerializer


class PatientMedicalHistoryViewSet(viewsets.ModelViewSet):
    queryset = PatientMedicalHistory.objects.all()
    serializer_class = PatientMedicalHistorySerializer