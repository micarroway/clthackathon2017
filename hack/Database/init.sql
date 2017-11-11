BEGIN;
--
-- Create model Diagnosis
--
CREATE TABLE `api_diagnosis` (`DiagnosisId` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `DiagnosisDescription` varchar(4000) NOT NULL);
--
-- Create model Facility
--
CREATE TABLE `api_facility` (`FacilityId` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `FacilityName` varchar(4000) NOT NULL, `FacilityType` varchar(200) NOT NULL, `NumberOfPhysicians` integer NOT NULL);
--
-- Create model FacilityAddress
--
CREATE TABLE `api_facilityaddress` (`FacilityAddressId` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `StreetAddress1` varchar(100) NOT NULL, `StreetAddress2` varchar(100) NOT NULL, `City` varchar(100) NOT NULL, `State` varchar(100) NOT NULL, `PostalCode` varchar(100) NOT NULL, `Facility_id` integer NOT NULL);
--
-- Create model InsuranceCompany
--
CREATE TABLE `api_insurancecompany` (`InsuranceCompanyId` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `CompanyName` varchar(4000) NOT NULL, `StreetAddress1` varchar(100) NOT NULL, `StreetAddress2` varchar(100) NOT NULL, `City` varchar(100) NOT NULL, `State` varchar(100) NOT NULL, `PostalCode` varchar(100) NOT NULL);
--
-- Create model Patient
--
CREATE TABLE `api_patient` (`PatientId` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `FirstName` varchar(150) NOT NULL, `MiddleName` varchar(150) NULL, `LastName` varchar(150) NOT NULL, `UserName` varchar(150) NOT NULL, `DateOfBirth` date NOT NULL, `Gender` varchar(2) NOT NULL, `Race` varchar(10) NOT NULL, `Ethnicity` varchar(10) NOT NULL);
--
-- Create model PatientAddress
--
CREATE TABLE `api_patientaddress` (`PatientAddressId` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `StreetAddress1` varchar(100) NOT NULL, `StreetAddress2` varchar(100) NOT NULL, `City` varchar(100) NOT NULL, `State` varchar(100) NOT NULL, `PostalCode` varchar(100) NOT NULL, `Patient_id` integer NOT NULL);
--
-- Create model PatientInsurance
--
CREATE TABLE `api_patientinsurance` (`PatientInsuranceId` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `PremiumType` varchar(10) NOT NULL, `PremiumCost` numeric(23, 2) NOT NULL, `Patient_id` integer NOT NULL);
--
-- Create model PatientMedicalHistory
--
CREATE TABLE `api_patientmedicalhistory` (`PatientMedicalHistoryId` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `DateOfVisit` date NOT NULL, `CostOfVisit` numeric(23, 2) NOT NULL, `InsurancePercentage` numeric(11, 10) NOT NULL, `Diagnoses` varchar(4000) NOT NULL, `Facility_id` integer NOT NULL, `InsuranceCompany_id` integer NOT NULL, `Patient_id` integer NOT NULL);
--
-- Create model PatientMedicalHistorySymptomDiagnosis
--
CREATE TABLE `api_patientmedicalhistorysymptomdiagnosis` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Diagnosis_id` integer NOT NULL, `PatientMedicalHistory_id` integer NOT NULL);
--
-- Create model PatientOccupation
--
CREATE TABLE `api_patientoccupation` (`PatientOccupationId` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `CompanyName` varchar(100) NOT NULL, `CompanyLocation` varchar(100) NOT NULL, `PositionTitle` varchar(100) NOT NULL, `Salary` numeric(23, 2) NOT NULL, `Patient_id` integer NOT NULL);
--
-- Create model Symptom
--
CREATE TABLE `api_symptom` (`SymptomId` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Symptom` varchar(100) NOT NULL, `SymptomDescription` varchar(4000) NOT NULL);
--
-- Add field Symptom to patientmedicalhistorysymptomdiagnosis
--
ALTER TABLE `api_patientmedicalhistorysymptomdiagnosis` ADD COLUMN `Symptom_id` integer NOT NULL;
ALTER TABLE `api_facilityaddress` ADD CONSTRAINT `api_facilityaddress_Facility_id_6b683b2b_fk_api_facil` FOREIGN KEY (`Facility_id`) REFERENCES `api_facility` (`FacilityId`);
ALTER TABLE `api_patientaddress` ADD CONSTRAINT `api_patientaddress_Patient_id_84c39b1a_fk_api_patient_PatientId` FOREIGN KEY (`Patient_id`) REFERENCES `api_patient` (`PatientId`);
ALTER TABLE `api_patientinsurance` ADD CONSTRAINT `api_patientinsurance_Patient_id_9853e520_fk_api_patie` FOREIGN KEY (`Patient_id`) REFERENCES `api_patient` (`PatientId`);
ALTER TABLE `api_patientmedicalhistory` ADD CONSTRAINT `api_patientmedicalhi_Facility_id_e08c7da5_fk_api_facil` FOREIGN KEY (`Facility_id`) REFERENCES `api_facility` (`FacilityId`);
ALTER TABLE `api_patientmedicalhistory` ADD CONSTRAINT `api_patientmedicalhi_InsuranceCompany_id_82d14e57_fk_api_insur` FOREIGN KEY (`InsuranceCompany_id`) REFERENCES `api_insurancecompany` (`InsuranceCompanyId`);
ALTER TABLE `api_patientmedicalhistory` ADD CONSTRAINT `api_patientmedicalhi_Patient_id_2673024d_fk_api_patie` FOREIGN KEY (`Patient_id`) REFERENCES `api_patient` (`PatientId`);
ALTER TABLE `api_patientmedicalhistorysymptomdiagnosis` ADD CONSTRAINT `api_patientmedicalhi_Diagnosis_id_0f7835aa_fk_api_diagn` FOREIGN KEY (`Diagnosis_id`) REFERENCES `api_diagnosis` (`DiagnosisId`);
ALTER TABLE `api_patientmedicalhistorysymptomdiagnosis` ADD CONSTRAINT `api_patientmedicalhi_PatientMedicalHistor_2fde7426_fk_api_patie` FOREIGN KEY (`PatientMedicalHistory_id`) REFERENCES `api_patientmedicalhistory` (`PatientMedicalHistoryId`);
ALTER TABLE `api_patientoccupation` ADD CONSTRAINT `api_patientoccupatio_Patient_id_df8d6d3d_fk_api_patie` FOREIGN KEY (`Patient_id`) REFERENCES `api_patient` (`PatientId`);
ALTER TABLE `api_patientmedicalhistorysymptomdiagnosis` ADD CONSTRAINT `api_patientmedicalhi_Symptom_id_dfbea790_fk_api_sympt` FOREIGN KEY (`Symptom_id`) REFERENCES `api_symptom` (`SymptomId`);
COMMIT;
