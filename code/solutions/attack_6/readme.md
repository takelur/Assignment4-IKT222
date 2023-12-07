# Attack 6

## Background

This attack was a reverse engineering task where I was supposed to gain access to a top secret database.


## Solution

By using Cutter I discovered that the login verification on the *reverse.engineering-bin* binary was just a simple string comparison. As shown below:

```bash
lea     rdi, str.Login_to_Regjeringen_State_Secrets
# ImGui for GUI
call    ImGui::Begin(char const*, bool*, int)
# Creates username and password input fields
lea     rsi, main::username ; 0xe0f40 ; int64_t arg4
lea     rdi, str.Brukernavn ; 0x9d0a8 ; int64_t arg6
lea     rsi, main::password ; 0xe0e40 ; int64_t arg4
lea     rdi, str.Passord ; 0x9d0b3 ; int64_t arg6
call    ImGui::InputText

# Compares username
movabs  rax, 0x6e696d7374617473 ; 'statsmin'
cmp     qword main::username, rax ; 0xe0f40
movabs  rax, 0x72657473696e69 ; 'inister'
cmp     qword data.000e0f46, rax ; 0xe0f46

# Compares a password
cmp     dword main::password, 0x616e7265
```

The hardcoded username it compares with is "statsminister" and the hardcoded password is in hexadecimal "616e7265" which is equal to "anre" in ASCII. But remember that a stack uses LIFO so in reality the password is the reverse: "erna".

Logging in to the database with
```
Username: statsminister
Password: erna
```

was succesful and I was able to read all the top secret information!