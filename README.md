# Install Fastapi:

```bash
pip install fastapi["standard"]
```

### Generate a self-signed certificate for testing purposes if you don’t have one:

```bash
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes
```

# Start app

1. ### With hypercorn http/2

```bash
hypercorn main:app --bind 0.0.0.0:8443 --certfile cert.pem --keyfile key.pem
```

2. ### With uvicorn http 1.1

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8443 --ssl-keyfile=key.pem --ssl-certfile=cert.pem
```

# Test perfomanse

```bash
python3 script.py
```