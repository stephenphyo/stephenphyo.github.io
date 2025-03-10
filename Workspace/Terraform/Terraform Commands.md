# Terraform

## Terraform Commands

### **Initialization Command**

| Command  | Description  | 
|:------|:------|
| terraform init | Initialize the Terraform working directory |

### **Core Workflow Commands**

| Command  | Description  | 
|:------|:------|
| terraform validate | Validate the configuration files for syntax and dependency errors |
| terraform plan | Show changes Terraform will apply |
| terraform plan -refresh-only | |
| terraform plan -destroy | |
| terraform apply | Apply the changes to the infrastructure |
| terraform destroy | Delete all resources defined in the configuration |
| terraform fmt | Format Terraform configuration files for consistency |

#### Sync with Real-World Infrastructure

- When infrastructure is manually modified outside of Terraform, Terraform's state file becomes out of sync with reality.
- The Terraform state should be reconciled with real-world infrastructure before making changes to the configuration.
- <b>State file must be updated</b> with the latest resource attributes.

| Command  | Description  | 
|:------|:------|
| terraform refresh | Update the state file without applying changes |

- In Terraform v0.15.4, HashiCorp deprecated terraform refresh and completely removed it in Terraform v1.2.0.
- The reason for deprecation is that terraform apply and terraform plan already refresh the state automatic ally when needed.

Replacement Commands:

| Command  | Description  | 
|:------|:------|
| terraform plan -refresh-only | Show what will change in the state |
| terraform apply -refresh-only | Update state without modifying resources |

### **State Management Commands**

### **Resource Management Commands**

| Command  | Description  | 
|:------|:------|
| terraform import | Import an existing resource into Terraform |
| terraform taint | Mark a resource for <b>recreation</b> (destroy and create) on the next apply |
| terraform untaint | Remove the taint from a resource |

### **Module Management Commands**

### **Provider Management Commands**

### **Workspace Commands**

### **Debugging Commands**

| Command  | Description  | 
|:------|:------|
| terraform output | Display output values from the state file |
| terraform show | Show details about Terraform configuration and state |
| terraform graph | Generate a visual representation of the dependency graph |
| terraform console | Provide an interactive shell for evaluating expressions |