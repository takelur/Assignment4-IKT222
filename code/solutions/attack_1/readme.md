# Attack 1

## Background

This first attack was performed to gain access to the first dashboard behind authentication on the fake [government website](https://regjeringen.uiaikt.no/).

The [login form](https://portal.regjeringen.uiaikt.no/) has a timing error as given by the code below:
```python
int total_time = 0;

if (a.length() != b.length()) {
    return total_time;
}

for (size_t i = 0; i <= a.length(); ++i) {
    if (a[i] != b[i]) {
        return total_time;
    }
    total_time++;
}
return total_time;
```
This allows me to try different passwords and guess towards the correct one by comparing the total_time taken.

## Solution

By running the script in *main.py* the password will be bruteforced by first finding the correct password length by the time taken to check the password each time, and then it will begin bruteforcing the actual password.

Running the script with `python3 main.py` will give the following result:

`Password for jonas.dahl is KattenMinErKul120`