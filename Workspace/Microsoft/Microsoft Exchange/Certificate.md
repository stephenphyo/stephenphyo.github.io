# Microsoft Exchange

## Certificate

### <u>**Generate Certificate Signing Request (CSR)**</u>

```powershell
$certRequest = New-ExchangeCertificate -GenerateReques -FriendlyName "Cert-EXCG01" ` -SubjectName "C=SG, O=Stephen Phyo, CN=mail.stephenphyo.com" -DomainName mail.stephenphyo.com, autodiscover.stephenphyo.com -PrivateKeyExportable $true -KeySize 2048 -Path C:\CSR_Request.csr

```