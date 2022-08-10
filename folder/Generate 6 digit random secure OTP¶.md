# Generate 6 digit random secure OTP


```python
import secrets

#Getting systemRandom class instance out of secrets module
secretsGenerator = secrets.SystemRandom()

print("Generating 6 digit random OTP")
otp = secretsGenerator.randrange(100000, 999999)

print("Secure random OTP is ", otp)
```

    Generating 6 digit random OTP
    Secure random OTP is  254558
    


```python

```
