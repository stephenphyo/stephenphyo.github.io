# Oracle SQL

## Oracle Home Directory

#### Oracle Base

- In Oracle Database Installer, **Oracle Base** directory can be set.
- This is the **top-level** directory where all Oracle-related files are stored.

#### Oracle Home

- Oracle Home is the actual installaiton directory of Oracle Database software.
- The installer follows the **Optimal Flexible Architecture (OFA) standard**, which organizes Oracle installations into structured directories.
- If the Oracle Base is set to, for example, **C:\oracle21c**, the installer automatically set the Oracle Home directory as **C:\oracle21c\homes\OraDB21Home1**.
- Oracle provides <u>**Multi-Home Support**</u>, i.e. multiple installations (multiple database versions or client versions) **under a single Oracle Base**.
- The **homes** directory allows multiple Oracle Homes to coexist within the same Oracle Base.

#### Standard Naming

- The installer uses **homes\OraDB21Home1** as a default name for the first home (if Oracle 21c Database is being installed) to avoid conflicts and keep installations organized.
- If another Oracle version is installed later, it might create **C:\oracle21c\homes\OraDB21Home2**.
- The **OraDB21Home1** name follows Oracle's convention:
    1. OraDB: Oracle Database
    2. 21: Version 21c
    3. Home1: First Installation
- The Oracle Home field can be **manually changed**.
- However, Oracle's best practice is to use **homes\\** for clarity and consistency.
