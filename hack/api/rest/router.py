from .viewsets import *
from rest_framework.routers import DefaultRouter


# Routers provide an easy way of automatically determining the URL conf.
router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'patientAddresses', PatientAddressViewSet)
router.register(r'occupations', PatientOccupationViewSet)
router.register(r'insurances', PatientInsuranceViewSet)
router.register(r'symptom', SymptomViewSet)
router.register(r'diagnosis', DiagnosisViewSet)
router.register(r'facility', FacilityViewSet)
router.register(r'facilityAddresses', FacilityAddressViewSet)
router.register(r'insuranceCompany', InsuranceCompanyViewSet)
router.register(r'medicalHistory', PatientMedicalHistoryViewSet)
