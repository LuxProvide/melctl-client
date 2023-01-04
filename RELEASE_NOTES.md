<!-- vim: set ft=2 ts=Markdown -->

# MelCtl - Client - Releases notes

\[TOC\]

---

## v5 ~ _Pedantic Santa_

### Changes

* Support for MelCtl server 5
* Moved towards a plugin architecture on the client side too

---

## v4 ~ _Specific Virmac_

### Changes

* Added an `s3ds` endpoint
  * List, create and disable S3DS access keys
* Added an `users` endpoint
  * List user(s)
  * List and create users S3DS access keys

### What should you do ?

* Update your MelCtl client to the latest version
* Refresh your token to access your new permissions:
  * Run `melctl login user`

---
