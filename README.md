# Chatbot with Whatsapp Web

Trying to make a bot to whatsapp using selenium.

---
### What it needs:
- A whatsapp account with web interface connected.
- A place to persist the profile files, using ```./profile```
- Docker and [Docker Compose](https://docs.docker.com/compose/install/) or any other way to run python

---
### What it does:
- Just open the main page of web.whatsapp.com for now...

---
### How to start:
Run ```docker-compose up```
  - A directory with a new browser profile will be created.

Stop with ```docker-compose down```

---
### To do:
- Add profile persistence
- Detect disconnected profile to scan qr code
- Get browser driver in Dockerfile
- Read chats
- Detect new messages
- ...
