# Terraform

## Terraform Basics

### **<u>Terraform Configuration Syntax</u>**

```terraform
/* Terraform Configuration Syntax */
<BLOCK TYPE> "<BLOCK LABEL>" "<BLOCK LABEL>" {
    # Block Body
    <IDENTIFIER> = <EXPRESSION>
}
```

More info:
- [Terraform Configuration](https://www.terraform.io/docs/configuration/index.html)
- [Terraform Configuration Syntax](https://www.terraform.io/docs/configuration/syntax.html)

### Storing Secret Data

- It is generally considered <b>insecure</b> to store secret data, such as passwords, API keys, and other sensitive information, <b>in the same version control repository</b> as the Terraform configuration.
- This is because version control repositories are often <u>publicly accessible</u>, and if sensitive information is stored in the repository, it can be easily accessed by unauthorized individuals.
- Additionally, version control repositories typically have a history of all changes made to files, so even if sensitive information is deleted at a later point, it can still be retrieved from the repository history.
- To properly secure secret data, it is recommended to store it in a secure and encrypted format, such as in a secure vault or by using a tool specifically designed for storing secrets.

###  
