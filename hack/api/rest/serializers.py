from api.models import *
from rest_framework import serializers


class PatientAddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PatientAddress
        fields = '__all__'


class PatientInsuranceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PatientInsurance
        fields = '__all__'


class PatientOccupationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PatientOccupation
        fields = '__all__'


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    addresses = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    insurances = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    occupations = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    history = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = '__all__'


class SymptomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Symptom
        fields = '__all__'


class DiagnosisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Diagnosis
        fields = '__all__'


class FacilitySerializer(serializers.HyperlinkedModelSerializer):
    addresses = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    history = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Facility
        fields = '__all__'


class FacilityAddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FacilityAddress
        fields = '__all__'


class InsuranceCompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InsuranceCompany
        fields = '__all__'


class PatientMedicalHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PatientMedicalHistory
        fields = '__all__'
