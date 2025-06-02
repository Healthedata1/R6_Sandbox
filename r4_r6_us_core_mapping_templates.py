# %% [markdown]
# # R4-R6 US Core Mapping Templates
# 
# r4-r6-us-core-mapping-templates.ipynb
# 
# A set of US Core Profile Mapping template for converting from FHIR R4 to FHIR R6.  These template are used by the [FHIRPathMappingLanguage](https://github.com/beda-software/FHIRPathMappingLanguage)
# a data DSL designed to convert data from any source to any FHIR Resource.  The templates consist of Python dictionaries that leverage liquid template and FHIRPath syntax to generate the mappings. 

# %%
import json
templates = {'AllergyIntolerance':'''
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
  "lastOccurrence": "{{ AllergyIntolerance.lastOccurrence }}",
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
''',
}


# %%
def main():
    print("This runs when the script is executed directly.")
    for i in list(templates.keys()):
      print(f"Template = {i}")

if __name__ == "__main__":
    main()


