### Test
```
    python fake_smtp.py -s 127.0.0.1 -p 2525
    python fake_email.py
```
### Result
- mail/10_26_2021_1635303337.eml
```
    b'From: From Person <from_email@test.com>
    To: To Person <to_email@test.com>
    Subject: Fake SMTP e-mail test

    This is a fake e-mail message.'
```

### References
- https://muffinresearch.co.uk/fake-smtp-server-with-python/
- https://www.tutorialspoint.com/python/python_sending_email.htm
