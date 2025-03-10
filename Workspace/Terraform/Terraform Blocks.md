# Terraform

## Terraform Blocks

- A block is <u>**a fundamental unit**</u> used to define and configure the infrastructure.
- Blocks are written in **HashiCorp Configuration Language <u>(HCL)</u>** and allow to declare elements within the Terraform code.
- Each block serves a specific purpose and has its own syntax and set of properties.

### **<u>Types of Blocks</u>**

##### Fundamental Blocks
1. Terraform (Setting) Block
2. Provider Block
3. Resource Block

##### Reference Blocks
4. Data (Sources) Block
5. Module Block

##### Variable Blocks
6. (Input) Variable Block
7. Output Block
8. Locals Block
   
### **<u>1. Terraform Block</u>**

Terraform block is used to define **global configuration** and behavior for terraform execution. 

Terraform block includes:

- Required Terraform **version**
- **Backend** for storing state file
- Define **features** (experimental or optional)
- **Variables** used across multiple modules or configurations

```terraform
terraform {
  required_version = ">= 1.0.0"
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = ">= 2.0"
    }
  }
# Terraform State Storage to Azure Storage Container
  backend "azurerm" {
    resource_group_name = "terraform-storage-rg"
    storage_account_name = "terraformstate201"
    container_name = "tfstatefiles"
    key = "terraform.tfstate"
  }   
}
```

### **<u>2. Provider Block</u>**

Provider block is used to configure and define provider for specific cloud or infrastructure platform. This enables Terraform to know which provider to use and how to <u>authenticate</u> with it.

Provider block includes:

- Provider **name and version**
- Authentication **credentials**
- Other provider-specific settings

```terraform
provider "azurerm" {
  features {}
}
```

- Unlike many other objects in the Terraform language, a provider block <u>**may be omitted**</u> if its contents would otherwise be empty.
- Terraform assumes an empty default configuration for any provider that is not explicitly configured.

### **<u>3. Resource Block</u>**

Resource block is used to define and manage infrastructure components.

Resource block includes:

- **Resource Type:** Determines the type of infrastructure object 
- **Resource Local Name:** Used to refer to the resource from somewhere in same Terraform module, but has no significance outside the module's scope
- **Properties** and **attributes** of the resource
- **Dependencies** and **relationships** between resources

Resource Type and Resource Name together serves as an **identifier** for a specific resource and **<u>must be unique within a module</u>**.

**Meta-arguments** can also be used with any resource to change the behavior of the resource.

### **<u>6. Variable Block</u>**

Variable block is used to declare input variables for flexible and dynamic configurations.

- Variables can be defined for arguments which may **vary across environments or deployments**.
- With variable blocks, the configuration can be easily **reused and customized** for different scenarios without modifying the underlying code.
- This provides **parameterization** to the configuration, allowing users to provide parameters during Terraform applies or through variable files.

```terraform
variable "instance_type" {
  description = "EC2 instance type"
  type = string
  default = "t2.micro"
}
```

#### "Description" Argument

- Terraform variables and outputs that set the "description" argument are **<u>not stored in the state file</u>**.
- The "description" argument is used to provide a human-readable description of the variable or output, and it is <u>intended to be used as documentation</u> for other users of the Terraform code.
- The state file is used to store the current state of the infrastructure managed by Terraform, including the values of variables and outputs, however, the "description" argument is not part of the state file, and it is not used by Terraform to manage the infrastructure.
- Instead, it is only used as metadata to describe the variable or output.

### **<u>7. Locals Block</u>**

Locals block is used to declare local variables within Terraform configuration for **easier code readability, reusability, and duplication reduction**.

- Local variables are **temporary** and can be defined within a block to compute and store intermediate values that are used within the same configuration file.
- Once a local value is declared, it can be <u>referenced in expressions</u> as **`local.<NAME>`**.
- These variables are <u>not exposed to other configurations or modules</u> and are purely for <u>internal use within the **same** configuration</u>.
- The ability to easily change the value in a **<u>central place</u>** is the **key advantage** of local values.
- They reduce duplication by storing intermediate values.

```terraform
locals {
  environment = "dev"
  owner = "teamA"
}
```

### **<u>8. Output Block</u>**

Output block can be used to define the values which are displayed as outputs after executing 'terraform apply' or 'terraform output'. By defining output blocks, important information can be extracted from the infrastructure and provide it to users or other systems for further actions or integrations.

- If a module uses local values, those values can be exposed using the "terraform output" directive.
- By using the terraform output directive, an output for a module can be defined which provides information about the local values used within the module.
- This information can then be consumed by other parts of the Terraform configuration, allowing to make use of the values that have been set within the module.
- A **root module** can use outputs to <u>print certain values in the CLI output</u> after running `terraform apply`.
- A **child module** can use outputs to <u>expose</u> a subset of its <u>resource attributes to a parent module</u>.
- When using **remote state**, root module outputs can be accessed by other configurations via a **terraform_remote_state data source**.