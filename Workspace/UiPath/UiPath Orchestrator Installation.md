# UiPath

## UiPath Orchestrator - Installation

### Prerequisites

.NET Framework 4.7.2 https://dotnet.microsoft.com/en-us/download/dotnet-framework/net472

IIS URL Rewrite https://www.iis.net/downloads/microsoft/url-rewrite

.NET Core Hosting Bundle https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-aspnetcore-3.1.3-windows-hosting-bundle-installer

$cert = New-SelfSignedCertificate -certstorelocation cert:\localmachine\my -dnsname WSVR-UIPO-01.stephenphyo.com
$pwd = ConvertTo-SecureString -String 'ALPHAbetagammatango@123' -Force -AsPlainText
$path = 'cert:\localmachine\my\' + $cert.thumbprint
Export-PfxCertificate -cert $path -FilePath "C:\Users\admin01\Desktop\New folder\cert.pfx" -Password $pwd