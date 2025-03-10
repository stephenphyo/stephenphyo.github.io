# Terraform

## Terraform Resource Behavior

Terraform manages resources <b>declaratively</b>, meaning the configuration defines the <b>desired state</b>, and Terraform applies changes to achieve that state.

### **<u>Key Resource Behaviors</u>**

#### 1. Create Resource

- Create resources that <u>exist in the configuration</u> but are <u>not associated</u> with a real infrastructure object <u>in the state</u>.

#### 2. Destroy Resource

- If a resource is <u>removed from the configuration file</u> but it already <u>exists in the state</u>, Terraform destroys it in the next apply.

#### 3. Modify (Update In-Place) Resource

- If a <b><u>mutable property</u></b> of a resource (e.g. tag) is modified in the configuration file, Terraform detects the change and updates the resource in-place accordingly.

#### 4.Replace (Destroy & Create Replacement) Resource

- If an <b><u>immutable property</u></b> of a resource (e.g. instance_type) is modified in the configuration file, Terraform <u>destroys</u> the existing resource and <u>re-creates</u> a new one.