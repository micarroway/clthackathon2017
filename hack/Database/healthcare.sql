Create Database healthcare

Use healthcare;

Create Table tpatient
(
	pid Int unsigned Not Null Auto_Increment Primary Key,
    FirstName nvarchar(150) Not Null,
    LastName nvarchar(150) Not Null,
    MiddleName nvarchar(150) Not Null,
    UserName nvarchar(100) Not Null,
    DateOfBirth Date Not Null,
    Gender nvarchar(2) Not Null,
    Race nvarchar(10) Not Null,
    Ethnicity nvarchar(10) Not Null
)

Create Table tPatientAddress
(
	pid Int Unsigned Not Null Primary Key,
	StreetAddress1 nvarchar(100) Not Null,
    StreetAddress2 nvarchar(100) Not Null,
    City nvarchar(100) Not Null,
    State nvarchar(100) Not Null,
    PostalCode nvarchar(100) Not Null
)

Create Table tPatientInsurance
(
	pid Int Unsigned Not Null,
    InsurID Int Unsigned Not Null,
    PremiumType nvarchar(10) Not Null,
    PremiumCost decimal(23,2) Not Null
)
Create Table tPatientOccupation
(
	pid Int Unsigned Not Null Primary Key,
    CompanyName nvarchar(100) Not Null,
    CompanyLocation nvarchar(100) Not Null,
    pTitle nvarchar(100) Not Null,
    Salary decimal(23,2) Not Null
)

Create Table tPatientMedHist
(
	pmhID Int Unsigned Auto_Increment Primary Key,
	pid Int Unsigned Not Null,
    fid Int Unsigned Not Null,
	insurid Int Unsigned Not Null,
    DateofVisit Date Not Null,
    CostOfVist decimal(23,2) Not Null,
    InsurancePercentage numeric(38,20) Not Null,
    Diagnoses nvarchar(4000) Not Null
)

Create Table tPatientMedHistSD
(
	pmhID Int Unsigned Not Null,
    pid Int Unsigned Not Null,
    SymID Int Unsigned Not Null,
    DiagnosesID Int Unsigned Not Null
)

Create Table tSymptom
(
	symID Int Unsigned Not Null,
    Symptom nvarchar(100) Not Null,
    SymptomDesc nvarchar(4000) Not Null
)

Create Table tDiagnoses
(
	diagnosesID Int Unsigned Not Null,
    DiagnosesDesc nvarchar(4000) Not Null
)

Create Table tFacility
(
	fid Int Unsigned Not Null Primary Key,
    FacilityName nvarchar(4000) Not Null,
    FacilityType nvarchar(200) Not Null,
    NumberofPhysicans Int Not Null
)

Create Table tFacilityPrograms
(
	fid Int Unsigned Not Null,
    Program nvarchar(4000) Not Null
)

Create Table tFacilityAddress
(
	fid Int Unsigned Not Null,
	StreetAddress1 nvarchar(100) Not Null,
    StreetAddress2 nvarchar(100) Not Null,
    City nvarchar(100) Not Null,
    State nvarchar(100) Not Null,
    PostalCode nvarchar(100) Not Null
)

Create Table tInsuranceCompany
(
	insurid Int Unsigned Not Null,
    CompanyName nvarchar(4000) Not Null,
	StreetAddress1 nvarchar(100) Not Null,
    StreetAddress2 nvarchar(100) Not Null,
    City nvarchar(100) Not Null,
    State nvarchar(100) Not Null,
    PostalCode nvarchar(100) Not Null
)    
