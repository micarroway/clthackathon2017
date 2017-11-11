from api.models import *
from rest_framework import routers, serializers, viewsets


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientAddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PatientAddress
        fields = '__all__'


class PatientAddressViewSet(viewsets.ModelViewSet):
    queryset = PatientAddress.objects.all()
    serializer_class = PatientAddressSerializer


class PatientInsuranceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PatientInsurance
        fields = '__all__'


class PatientInsuranceViewSet(viewsets.ModelViewSet):
    queryset = PatientInsurance.objects.all()
    serializer_class = PatientInsuranceSerializer

class PatientOccupationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PatientOccupation
        fields = '__all__'


class PatientOccupationViewSet(viewsets.ModelViewSet):
    queryset = PatientOccupation.objects.all()
    serializer_class = PatientOccupationSerializer


class SymptomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Symptom
        fields = '__all__'


class SymptomViewSet(viewsets.ModelViewSet):
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer


class DiagnosisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Diagnosis
        fields = '__all__'


class DiagnosisViewSet(viewsets.ModelViewSet):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer


class FacilitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Facility
        fields = '__all__'


class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer


class FacilityAddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FacilityAddress
        fields = '__all__'


class FacilityAddressViewSet(viewsets.ModelViewSet):
    queryset = FacilityAddress.objects.all()
    serializer_class = FacilityAddressSerializer


class InsuranceCompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InsuranceCompany
        fields = '__all__'


class InsuranceCompanyViewSet(viewsets.ModelViewSet):
    queryset = InsuranceCompany.objects.all()
    serializer_class = InsuranceCompanySerializer


class PatientMedicalHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PatientMedicalHistory
        fields = '__all__'


class PatientMedicalHistoryViewSet(viewsets.ModelViewSet):
    queryset = PatientMedicalHistory.objects.all()
    serializer_class = PatientMedicalHistorySerializer


class PatientMedicalHistorySymptomDiagnosisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PatientMedicalHistorySymptomDiagnosis
        fields = '__all__'


class PatientMedicalHistorySymptomDiagnosisViewSet(viewsets.ModelViewSet):
    queryset = PatientMedicalHistorySymptomDiagnosis.objects.all()
    serializer_class = PatientMedicalHistorySymptomDiagnosisSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'patient/address', PatientAddressViewSet)
router.register(r'patient/insurance', PatientInsuranceViewSet)
router.register(r'patient/occupation', PatientOccupationViewSet)
router.register(r'symptom', SymptomViewSet)
router.register(r'diagnosis', DiagnosisViewSet)
router.register(r'facility', FacilityViewSet)
router.register(r'facility/address', FacilityAddressViewSet)
router.register(r'insuranceCompany', InsuranceCompanyViewSet)
router.register(r'patient/medicalHistory', PatientMedicalHistoryViewSet)
router.register(r'patient/medicalHistory/symptomDiagnosis', PatientMedicalHistorySymptomDiagnosisViewSet)
