# Microsoft SQL

## System Tables & Views

### **<u>1. System Catalog Views</u>**

#### **<u>1.1. Database Object Metadata</u>**

|Query | Description |
|----------|----------|
| sys.objects | Information of all Objects within the database |
| sys.schemas | Details of all Schemas |
| sys.tables | Details of all User Tables |
| sys.views | Metadata of Views |
| sys.columns | Column metadata for all tables and views |
| sys.foreign_keys | Details of Foreign Key Constraints |
| sys.key_constraints | Primary & Unique Key Constraints |
| sys.indexes | Details of Indexes |
| sys.triggers | List of Triggers |

#### **<u>1.2. Security & Principals</u>**

|Query | Description |
|----------|----------|
| sys.server_principals | Logins (SQL Logins, Windows Logins, Groups) |
| sys.database_principals | Database Users, Roles & App Roles |
| sys.server_role_members | Server Role Membership |
| sys.database_role_members | Database Role Membership |
| sys.server_permissions | Server-Level Permissions |
| sys.database_permissions | Permissions for Database Objects |

#### **<u>1.3. Storage & Partitioning</u>**

|Query | Description |
|----------|----------|
| sys.partitions | Partition Metadata for Tables & Indexes |
| sys.allocation_units | Details of Storage Allocation |
| sys.extended_properties | Extended properties for objects |
| sys.database_files | Database File Information |
