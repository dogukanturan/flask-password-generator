# Flask Password Generator
A simple password generator built with Flask and built for testing DevOps processes.

# Usage
### Python
```bash
pip install -r requirements.txt
python app.py
```

### Docker
```bash
docker run -d -e PORT=80 -p 8080:80 dturan/flask-password-generator
```
# Test
```bash
curl "http://localhost:8080/10"
```
