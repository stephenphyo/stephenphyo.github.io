# Microsoft Exchange

## Mailbox Database

![Microsoft Exchange](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/microsoft/microsoft-exchange/microsoft-exchange-0001.webp)

### <u>**Rename Mailbox Database**</u>

- By default, a **unique generated** mailbox database is created.
- This mailbox database can be renamed without any disruption.

#### Rename Mailbox Database from EAC (Exchange Admin Cetner)

#### Rename Mailbox Database from EMS (Exchange Management Shell)

<u>Get Mailbox Database</u>

```powershell
Get-MailboxDatabase | fl name, edbfilepath, logfolderpath
```

<u>Rename Mailbox Database</u>

```powershell
Set-MailboxDatabase "current_mailbox_name" -Name "new_mailbox_name"
```

### <u>**Move Mailbox Database**</u>

- Mailbox database and transaction log files can be moved to new locations.
- The database needs to be <u>**dismounted**</u> and <u>**taken offline**</u> to move to new locations.

#### Move Mailbox Database from EMS (Exchange Management Shell)

```powershell
Move-DatabasePath <db_name> -EdbFilePath <non-root location>\<db_name>.edb -LogFolderPath <location>
```
