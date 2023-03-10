# Login

Login and obtain MelCtl tokens.

## Usage

```shell
melctl login {user|info} [arguments...]
```

## `user` - Login as user

This lets you obtain a user token, valid for a limited amount of time.

```shell
melctl login
```

* You'll be prompted for your LDAP username and password.
* The generated token will be stored in your local MelCTL secret directory

## `info` - Get login status

```shell
melctl login info
```

```
user        profile      valid_until  valid_until_text
----------  ---------  -------------  -------------------
jpclipffel  admin        1656750312   2022-07-02 10:25:12
```

---
