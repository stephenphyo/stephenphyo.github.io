# Microsoft SQL

## Linked Server from Microsoft SQL to Oracle SQL

![xl](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/mssql-oracle-linked-server.png)

<br>

### <u>Download Oracle Database Client</u>

Download Oracle Database Client from [Oracle Software Delivery Cloud](https://edelivery.oracle.com/osdc/faces/SoftwareDelivery)

[![xxl](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-01.png)](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-01.png)

[![xxl](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-02.png)](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-02.png)

[![xxl](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-03.png)](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-03.png)

[![xxl](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-04.png)](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-04.png)

<br>

#### Open Oracle Download Manager

[![xl](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-05.png)](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-05.png)

[![xl](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-06.png)](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-06.png)

[![xl](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-07.png)](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-07.png)

### <u>Install Oracle Database Client in Microsoft SQL Server</u>

[![xl](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-08.png)](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-08.png)

[![xl](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-09.png)](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-09.png)

[![xl](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-10.png)](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-10.png)

[![xl](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-11.png)](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-11.png)

[![xl](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-12.png)](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-12.png)

[![xl](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-13.png)](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-13.png)

[![xl](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-14.png)](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-14.png)

### Retrieve TNSNAMES Configuration from Oracle SQL Database

##### Go to **ORACLE_HOME\network\admin** directory

[![xl](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-15.png)](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-15.png)

[![xl](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-16.png)](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-16.png)

##### Copy TNSNAME of PDB

```txt
ORCL01PDB =
  (DESCRIPTION =
    (ADDRESS = (PROTOCOL = TCP)(HOST = WSVR-ORCL-01.stephenphyo.com)(PORT = 1521))
    (CONNECT_DATA =
      (SERVER = DEDICATED)
      (SERVICE_NAME = orcl01pdb)
    )
  )
```

##### Check **SERVICE_NAME**

```console
lsnrctl status
```

[![xl](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-21.png)](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-21.png)

##### Change **SERVICE_NAME** to **FQDN**

```txt
ORCL01PDB =
  (DESCRIPTION =
    (ADDRESS = (PROTOCOL = TCP)(HOST = WSVR-ORCL-01.stephenphyo.com)(PORT = 1521))
    (CONNECT_DATA =
      (SERVER = DEDICATED)
      (SERVICE_NAME = orcl01pdb.stephenphyo.com)
    )
  )
```

### <u>Create 'tnsnames.ora' File in Oracle Database Client in Microsoft SQL Database</u>

##### Go to **Oracle Base of Oracle Database Client** in Microsoft SQL Database Server

[![xl](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-17.png)](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-17.png)

##### Go to **ORACLE_BASE\network\admin**

[![xl](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-18.png)](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-18.png)

##### Create **tnsnames.ora** File

[![xl](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-19.png)](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-19.png)

##### Copy TNSNAME Configuration from Oracle SQL

[![xl](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-20.png)](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-20.png)

##### Test Connectivity to TNS Listener

[![xl](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-22.png)](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-22.png)

### <u>Enable 'Allow InProcess' for Provider in SSMS</u>

(Database) => Server Objects => Linked Servers => Providers => OraOLEDB.Oracle => (Right-Click) Properties

[![xs](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-23.png)](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-23.png)

[![xl](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-24.png)](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-24.png)

### <u>Create New Linked Server</u>

(Database) => Server Objects => Linked Servers => (Right-Click) New Linked Server

[![xl](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-25.png)](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-25.png)

[![xl](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-26.png)](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-sql/linked-server/linked-mssql-oracle-26.png)

<iframe height="500" src="https://www.youtube.com/embed/kTGFaz15fmM?si=y7eiy3amFs9gVNKO" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>