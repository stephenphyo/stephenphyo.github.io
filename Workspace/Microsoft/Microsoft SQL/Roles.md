# Microsoft SQL

## Roles

### **<u>Check Server-Level Permissions for Current Login</u>**

```sql
SELECT		pr.name AS LoginName, pr.type_desc, pr.is_disabled, perm.permission_name, perm.state_desc
FROM		sys.server_principals pr
LEFT JOIN	sys.server_permissions perm ON perm.grantee_principal_id = pr.principal_id
WHERE		pr.name = SUSER_NAME();
```

### **<u>Check Roles assigned to Current User in Specific Database</u>**

```sql

```

### **<u>Check All Databases which Current User has Access to</u>**

```sql
SELECT	name AS DatabaseName
FROM	sys.databases
WHERE	HAS_DBACCESS(name) = 1;
```