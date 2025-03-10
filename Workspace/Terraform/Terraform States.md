# Terraform

## Terraform States

### **<u>State Management</u>**

- Terraform stores resource metadata in a state file, called <b>terraform.tfstate</b>.
- This state file is critical for tracking resources and detecting drift.
- Primary purpose of Terraform state is to store bindings between objects in a remote system and resource instances declared in the configuration.
- However, the terraform.tfstate file <u><b>does not always match</b></u> the currently built infrastructure since one can manually change resources and therefore drift from the state configuration.
- When infrastructure is manually modified outside of Terraform, Terraform's state file becomes <b>out of sync</b> with reality.
- Terraform has <u>no way to know or track changes made outside of it</u>.

Example terraform.tfstate file:

```json
{
  "version": 4,
  "terraform_version": "1.10.5",
  "serial": 3,
  "lineage": "73c93455-ce06-ba63-1e89-76106d816f50",
  "outputs": {},
  "resources": [
    {
      "mode": "managed",
      "type": "azurerm_resource_group",
      "name": "sp-rg-01",
      "provider": "provider[\"registry.terraform.io/hashicorp/azurerm\"]",
      "instances": [
        {
          "schema_version": 0,
          "attributes": {
            "id": "/subscriptions/94f5d03b-caa4-4374-854a-a6cd80e9418f/resourceGroups/sp-rg-01",
            "location": "eastus",
            "managed_by": "",
            "name": "sp-rg-01",
            "tags": null,
            "timeouts": null
          }
        }
      ]
    }
  ],
  "check_results": null
}
```

<b>Manual update</b> of the state file are <u><b>NOT recommended</b></u> for the following reasons:

- Dangerous practice
- Easy to corrupt state file
- Inconsistencies
- 
### **<u>Taint</u>**

- Terraform has a <b>marker</b> called "<b><u>tainted</u></b>" which it uses to track that an object might be damaged and so a future Terraform plan ought to replace it.
- Terraform automatically marks an object as "tainted" if an error occurs during a multi-step "create" action, because Terraform cannot be sure that the object was left in a fully-functional state.
- The `terraform taint` command informs Terraform that a particular object has become <u>degraded or damaged</u>.
- For Terraform v0.15.2 and later, `terraform taint` command has been deprecated and it is recommended to use **`terraform apply -replace`** instead.
- Terraform represents this by marking the object as "tainted" in the Terraform state, and Terraform will propose to replace it in the next plan.

#### Untaint

- If Terraform currently considers a particular object as tainted but it's actually functioning correctly and <b>need not be replaced</b>, use `terraform untaint` to remove the taint marker from that object.
-  This command will not modify any real remote objects, but will modify the state in order to remove the tainted status.