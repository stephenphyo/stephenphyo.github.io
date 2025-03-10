# Terraform

## Microsoft Azure: Resource Group

### **Create Resource Group**

```terraform
terraform {
  required_version = ">= 1.0.0"
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = ">= 2.0"
    }    
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "sp-rg-01" {
  location = "eastus"
  name = "sp-rg-01"  
}
```
