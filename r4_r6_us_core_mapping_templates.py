# %% [markdown]
# # R4-R6 US Core Mapping Templates
# 
# r4-r6-us-core-mapping-templates.ipynb
# 
# A set of US Core Profile Mapping template - python dictionaries - for converting from FHIR R4 to FHIR R6.  These template are used by the [FHIRPathMappingLanguage](https://github.com/beda-software/FHIRPathMappingLanguage)
# a data DSL designed to convert data from any source to any FHIR Resource.  The templates consist of Python dictionaries that leverage liquid template and FHIRPath syntax to generate the mappings. 
# 
# Outline of How the templates are made and used
# 
# 1. These templates are created using Grok LLM.  See the [fhirmapping instructions prompts](https://github.com/Healthedata1/R6_Sandbox/blob/main/fhirmapping_instructuions_prompts.json). 
# 2. Examples are generated using the [r4_r6_fhirmapper.ipynb
# ](https://github.com/Healthedata1/R6_Sandbox/blob/main/r4_r6_fhirmapper.ipynb) Jupyter file.  This script maps the US Core version 8 examples which are based on FHIR R4 to R6 and loads them into the US Core R6 prototype IG build.
# 3. The examples are validated in the US Core R6 prototype IG build and, if needed, updates to the fhirmapping instructions prompts are made to edit the templates.
#    

# %%
import json
templates = {'DocumentReference':
    {
  "resourceType": "DocumentReference",
  "id": "{{ DocumentReference.id }}",
  "meta": {
    "versionId": "{{ DocumentReference.meta.versionId }}",
    "lastUpdated": "{{ DocumentReference.meta.lastUpdated }}",
    "source": "{{ DocumentReference.meta.source }}",
    "profile": "{[ DocumentReference.meta.profile ]}",
    "security": "{[ DocumentReference.meta.security ]}",
    "tag": "{[ DocumentReference.meta.tag ]}",
    "extension": "{[ DocumentReference.meta.extension ]}"
  },
  "implicitRules": "{{ DocumentReference.implicitRules }}",
  "language": "{{ DocumentReference.language }}",
  "text": "{{ DocumentReference.text }}",
  "contained": "{[ DocumentReference.contained ]}",
  "extension": "{[ DocumentReference.extension.where(url!='http://hl7.org/fhir/us/core/StructureDefinition/us-core-authentication-time') ]}",
  "modifierExtension": "{[ DocumentReference.modifierExtension ]}",
  "masterIdentifier": "{{ DocumentReference.masterIdentifier }}",
  "identifier": "{[ DocumentReference.identifier ]}",
  "version": "{{ DocumentReference.version }}",
  "basedOn": "{[ DocumentReference.basedOn ]}",
  "status": "{{ DocumentReference.status }}",
  "docStatus": "{{ DocumentReference.docStatus }}",
  "modality": "{[ DocumentReference.modality ]}",
  "type": "{{ DocumentReference.type }}",
  "category": "{[ DocumentReference.category ]}",
  "subject": "{{ DocumentReference.subject }}",
  "context": "{[ DocumentReference.context.encounter ]}",
  "event": "{[ DocumentReference.context.event ]}",
  "bodySite": "{[ DocumentReference.context.bodySite ]}",
  "facilityType": "{{ DocumentReference.context.facilityType }}",
  "practiceSetting": "{{ DocumentReference.context.practiceSetting }}",
  "period": "{{ DocumentReference.context.period }}",
  "date": "{{ DocumentReference.date }}",
  "author": "{[ DocumentReference.author ]}",
  "{% if DocumentReference.authenticator.exists() %}": {  "attester": [{
      "mode": {
        "coding": [
          {
            "system": "http://hl7.org/fhir/composition-attestation-mode",
            "code": "official"
          }
        ]
      },
      "time": "{{ DocumentReference.extension.where(url='http://hl7.org/fhir/us/core/StructureDefinition/us-core-authentication-time').valueDateTime }}",
      "party": "{{ DocumentReference.authenticator }}"
  }]
  },
  "custodian": "{{ DocumentReference.custodian }}",
  "relatesTo": "{[ DocumentReference.relatesTo ]}",
  "description": "{{ DocumentReference.description }}",
  "securityLabel": "{[ DocumentReference.securityLabel ]}",
  "content": {
    "{% for item in DocumentReference.content %}": {
      "attachment": "{{ %item.attachment }}",
      "profile": {
        "valueCoding": "{{ %item.format }}",
        "valueCanonical": "{{ null //no direct equivalent in 4.0.1 }}",
        "valueUri": "{{ null //no direct equivalent in 4.0.1 }}"
      }
    }
  }
},
    'Observation':
{
  "resourceType": "Observation",
  "id": "{{ Observation.id }}",
  "meta": {
    "versionId": "{{ Observation.meta.versionId }}",
    "lastUpdated": "{{ Observation.meta.lastUpdated }}",
    "source": "{{ Observation.meta.source }}",
    "profile": "{[ Observation.meta.profile ]}",
    "security": "{[ Observation.meta.security ]}",
    "tag": "{[ Observation.meta.tag ]}",
    "extension": "{[ Observation.meta.extension ]}"
  },
  "implicitRules": "{{ Observation.implicitRules }}",
  "language": "{{ Observation.language }}",
  "text": "{{ Observation.text }}",
  "contained": "{[ Observation.contained ]}",
  "extension": "{[ Observation.extension ]}",
  "modifierExtension": "{[ Observation.modifierExtension ]}",
  "identifier": "{[ Observation.identifier ]}",
  "instantiatesCanonical": "{{ null //no direct equivalent in 4.0.1 }}",
  "instantiatesReference": "{{ null //no direct equivalent in 4.0.1 }}",
  "basedOn": "{[ Observation.basedOn ]}",
  "triggeredBy": [{
    "observation": "{{ null //no direct equivalent in 4.0.1 }}",
    "type": "{{ null //no direct equivalent in 4.0.1 }}",
    "reason": "{{ null //no direct equivalent in 4.0.1 }}"
  }],
  "partOf": "{[ Observation.partOf ]}",
  "status": "{{ Observation.status }}",
  "category": "{[ Observation.category ]}",
  "code": "{{ Observation.code }}",
  "subject": "{{ Observation.subject }}",
  "focus": "{[ Observation.focus ]}",
  "encounter": "{{ Observation.encounter }}",
  "effectiveDateTime": "{{ Observation.effectiveDateTime }}",
  "effectivePeriod": "{{ Observation.effectivePeriod }}",
  "effectiveTiming": "{{ Observation.effectiveTiming }}",
  "effectiveInstant": "{{ Observation.effectiveInstant }}",
  "issued": "{{ Observation.issued }}",
  "performer": "{[ Observation.performer ]}",
  "valueQuantity": "{{ Observation.valueQuantity }}",
  "valueCodeableConcept": "{{ Observation.valueCodeableConcept }}",
  "valueString": "{{ Observation.valueString }}",
  "valueBoolean": "{{ Observation.valueBoolean }}",
  "valueInteger": "{{ Observation.valueInteger }}",
  "valueRange": "{{ Observation.valueRange }}",
  "valueRatio": "{{ Observation.valueRatio }}",
  "valueSampledData": "{{ Observation.valueSampledData }}",
  "valueTime": "{{ Observation.valueTime }}",
  "valueDateTime": "{{ Observation.valueDateTime }}",
  "valuePeriod": "{{ Observation.valuePeriod }}",
  "valueAttachment": "{{ null //no direct equivalent in 4.0.1 }}",
  "valueReference": "{{ null //no direct equivalent in 4.0.1 }}",
  "dataAbsentReason": "{{ Observation.dataAbsentReason }}",
  "interpretation": "{[ Observation.interpretation ]}",
  "note": "{[ Observation.note ]}",
  "bodySite": "{{ Observation.bodySite }}",
  "bodyStructure": "{{ null //no direct equivalent in 4.0.1 }}",
  "method": "{{ Observation.method }}",
  "specimen": "{{ Observation.specimen }}",
  "device": "{{ Observation.device }}",
  "referenceRange": {
    "{% for item in Observation.referenceRange %}": {
      "low": "{{ %item.low }}",
      "high": "{{ %item.high }}",
      "normalValue": "{{ null //no direct equivalent in 4.0.1 }}",
      "type": "{{ %item.type }}",
      "appliesTo": "{[ %item.appliesTo ]}",
      "age": "{{ %item.age }}",
      "text": "{{ %item.text }}"
    }
  },
  "hasMember": "{[ Observation.hasMember ]}",
  "derivedFrom": "{[ Observation.derivedFrom ]}",
  "organizer": "{{ null //no direct equivalent in 4.0.1 }}",
  "component": {
    "{% for item in Observation.component %}": {
      "code": "{{ %item.code }}",
      "valueQuantity": "{{ %item.valueQuantity }}",
      "valueCodeableConcept": "{{ %item.valueCodeableConcept }}",
      "valueString": "{{ %item.valueString }}",
      "valueBoolean": "{{ %item.valueBoolean }}",
      "valueInteger": "{{ %item.valueInteger }}",
      "valueRange": "{{ %item.valueRange }}",
      "valueRatio": "{{ %item.valueRatio }}",
      "valueSampledData": "{{ %item.valueSampledData }}",
      "valueTime": "{{ %item.valueTime }}",
      "valueDateTime": "{{ %item.valueDateTime }}",
      "valuePeriod": "{{ %item.valuePeriod }}",
      "valueAttachment": "{{ null //no direct equivalent in 4.0.1 }}",
      "valueReference": "{{ null //no direct equivalent in 4.0.1 }}",
      "dataAbsentReason": "{{ %item.dataAbsentReason }}",
      "interpretation": "{[ %item.interpretation ]}",
      "referenceRange": {
        "{% for subitem in %item.referenceRange %}": {
          "low": "{{ %subitem.low }}",
          "high": "{{ %subitem.high }}",
          "normalValue": "{{ null //no direct equivalent in 4.0.1 }}",
          "type": "{{ %subitem.type }}",
          "appliesTo": "{[ %subitem.appliesTo ]}",
          "age": "{{ %subitem.age }}",
          "text": "{{ %subitem.text }}"
        }
      }
    }
  }
},
'Condition':
{
  "resourceType": "Condition",
  "id": "{{ Condition.id }}",
  "extension": "{[ Condition.extension ]}",
  "meta": {
    "versionId": "{{ Condition.meta.versionId }}",
    "lastUpdated": "{{ Condition.meta.lastUpdated }}",
    "source": "{{ Condition.meta.source }}",
    "profile": "{[ Condition.meta.profile ]}",
    "security": "{[ Condition.meta.security ]}",
    "tag": "{[ Condition.meta.tag ]}",
    "extension": "{[ Condition.meta.extension ]}"
  },
  "identifier": "{[ Condition.identifier ]}",
 "{% if Condition.clinicalStatus.exists() %}": {"clinicalStatus":
        "{{Condition.clinicalStatus}}"},
  "{% else %}": { 
        "clinicalStatus":{ "coding": [
            {
                "system": "http://terminology.hl7.org/CodeSystem/condition-clinical",
                "code": "unknown",
                "display": "Unknown"
            }
        ],
        "text": "Unknown" 
  }
},
  "verificationStatus": "{{ Condition.verificationStatus }}",
  "category": "{[ Condition.category ]}",
  "severity": "{{ Condition.severity }}",
  "code": "{{ Condition.code }}",
  "bodySite": "{[ Condition.bodySite ]}",
  "bodyStructure": "{[ null //no direct equivalent in 4.0.1 ]}",
  "subject": "{{ Condition.subject }}",
  "encounter": "{{ Condition.encounter }}",
  "onsetDateTime": "{{ Condition.onsetDateTime }}",
  "onsetAge": "{{ Condition.onsetAge }}",
  "onsetPeriod": "{{ Condition.onsetPeriod }}",
  "onsetRange": "{{ Condition.onsetRange }}",
  "onsetString": "{{ Condition.onsetString }}",
  "abatementDateTime": "{{ Condition.abatementDateTime }}",
  "abatementAge": "{{ Condition.abatementAge }}",
  "abatementPeriod": "{{ Condition.abatementPeriod }}",
  "abatementRange": "{{ Condition.abatementRange }}",
  "abatementString": "{{ Condition.abatementString }}",
  "recordedDate": "{{ Condition.recordedDate }}",
  "recorder": "{{ Condition.recorder }}",
  "asserter": "{{ Condition.asserter }}",
  "stage": [
    {
      "summary": "{{ Condition.stage.summary }}",
      "assessment": "{[ Condition.stage.assessment ]}",
      "type": "{{ Condition.stage.type }}"
    }
  ],
  "evidence": [
    {
      "{% for item in Condition.evidence.code %}": {
        "concept": "{{ %item }}"
      }
    },
    {
      "{% for reference in Condition.evidence.detail %}": {
        "reference": "{{ %reference }}"
      }
    }
  ],
  "note": "{[ Condition.note ]}"
},
'Patient': 
{
  "resourceType": "Patient",
  "id": "{{ Patient.id }}",
  "extension": "{[ Patient.extension ]}",
  "meta": {
    "versionId": "{{ Patient.meta.versionId }}",
    "lastUpdated": "{{ Patient.meta.lastUpdated }}",
    "source": "{{ Patient.meta.source }}",
    "profile": "{[ Patient.meta.profile ]}",
    "security": "{[ Patient.meta.security ]}",
    "tag": "{[ Patient.meta.tag ]}",
    "extension": "{[ Patient.meta.extension ]}"
  },
  "identifier": "{[ Patient.identifier ]}",
  "active": "{{ Patient.active }}",
  "name": "{[ Patient.name ]}",
  "telecom": "{[ Patient.telecom ]}",
  "birthDate": "{{ Patient.birthDate }}",
  "deceasedBoolean": "{{ Patient.deceasedBoolean }}",
  "deceasedDateTime": "{{ Patient.deceasedDateTime }}",
  "address": "{[ Patient.address ]}",
  "maritalStatus": "{{ Patient.maritalStatus }}",
  "multipleBirthBoolean": "{{ Patient.multipleBirthBoolean }}",
  "multipleBirthInteger": "{{ Patient.multipleBirthInteger }}",
  "photo": "{[ Patient.photo ]}",
  "contact": [
    {
      "role": "{[ null //no direct equivalent in 4.0.1 ]}",
      "relationship": "{[ Patient.contact.relationship ]}",
      "name": "{{ Patient.contact.name }}",
      "additionalName": "{[ null //no direct equivalent in 4.0.1 ]}",
      "telecom": "{[ Patient.contact.telecom ]}",
      "address": "{{ Patient.contact.address }}",
      "additionalAddress": "{[ null //no direct equivalent in 4.0.1 ]}",
      "gender": "{{ Patient.contact.gender }}",
      "organization": "{{ Patient.contact.organization }}",
      "period": "{{ Patient.contact.period }}"
    }
  ],
  "communication": [
    {
      "language": "{{ Patient.communication.language }}",
      "preferred": "{{ Patient.communication.preferred }}"
    }
  ],
  "generalPractitioner": "{[ Patient.generalPractitioner ]}",
  "managingOrganization": "{{ Patient.managingOrganization }}",
  "link": [
    {
      "other": "{{ Patient.link.other }}",
      "type": "{{ Patient.link.type }}"
    }
  ]
},
'AllergyIntolerance':
{
  "resourceType": "AllergyIntolerance",
  "id": "{{ AllergyIntolerance.id }}",
  "meta": {
    "extension" : "{[ AllergyIntolerance.meta.extension ]}",
    "versionId": "{{ AllergyIntolerance.meta.versionId }}",
    "lastUpdated": "{{ AllergyIntolerance.meta.lastUpdated }}",
    "source": "{{ AllergyIntolerance.meta.source }}",
    "profile": "{[ AllergyIntolerance.meta.profile ]}",
    "security": "{[ AllergyIntolerance.meta.security ]}",
    "tag": "{[ AllergyIntolerance.meta.tag ]}"
  },
  "extension" : "{[ AllergyIntolerance.extension ]}",
  "identifier": "{[ AllergyIntolerance.identifier ]}",
  "clinicalStatus": "{{ AllergyIntolerance.clinicalStatus }}",
  "verificationStatus": "{{ AllergyIntolerance.verificationStatus }}",
  "type": "{{ AllergyIntolerance.type }}",
  "category": "{[ AllergyIntolerance.category ]}",
  "criticality": "{{ AllergyIntolerance.criticality }}",
  "code": "{{ AllergyIntolerance.code }}",
  "patient": "{{ AllergyIntolerance.patient }}",
  "encounter": "{{ AllergyIntolerance.encounter }}",
  "onsetDateTime": "{{ AllergyIntolerance.onsetDateTime }}",
  "onsetAge": "{{ AllergyIntolerance.onsetAge }}",
  "onsetPeriod": "{{ AllergyIntolerance.onsetPeriod }}",
  "onsetRange": "{{ AllergyIntolerance.onsetRange }}",
  "onsetString": "{{ AllergyIntolerance.onsetString }}",
  "recordedDate": "{{ AllergyIntolerance.recordedDate }}",
  "recorder": "{{ AllergyIntolerance.recorder }}",
  "asserter": "{{ AllergyIntolerance.asserter }}",
  "lastReactionOccurrence": "{{ AllergyIntolerance.lastOccurrence }}",
  "note": "{[ AllergyIntolerance.note ]}",
  "reaction": [
    {
      "substance": "{{ AllergyIntolerance.reaction.substance }}",
      "manifestation": [
      {
      "{% for manifestation in AllergyIntolerance.reaction.manifestation %}": {
        "concept": "{{ %manifestation }}"
         }
       }
      ],
      "description": "{{ AllergyIntolerance.reaction.description }}",
      "onset": "{{ AllergyIntolerance.reaction.onset }}",
      "severity": "{{ AllergyIntolerance.reaction.severity }}",
      "exposureRoute": "{{ AllergyIntolerance.reaction.exposureRoute }}",
      "note": "{[ AllergyIntolerance.reaction.note ]}"
    }
  ]
}
}



# %%
def main():
    print("This runs when the script is executed directly.")
    for i in list(templates.keys()):
      print(f"Template = {i}")

if __name__ == "__main__":
    main()


