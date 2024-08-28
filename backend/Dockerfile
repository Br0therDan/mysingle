# backend/Dockerfile
# 1. 베이스 이미지로 Python 3.9 사용
FROM python:3.12.4-slim

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 의존성 설치를 위해 requirements.txt 복사
COPY requirements.txt .

# 4. 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt

# 5. 소스 코드 복사
COPY . .

# 6. FastAPI 서버 실행
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]