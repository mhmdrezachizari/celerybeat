# file

# 1. Base image
FROM python:3.11-slim

# 2. Set working directory
WORKDIR /app

# 3. Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# 4. Copy project files
COPY . .

# 5. Default command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
