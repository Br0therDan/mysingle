# frontend/Dockerfile
# 1. 베이스 이미지로 Node.js 18 사용
FROM node:20.10.0-alpine

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 패키지 설치를 위해 package.json 및 package-lock.json 복사
COPY package*.json ./

# 4. 의존성 설치
RUN npm install

# 5. 소스 코드 복사
COPY . .

# 6. Next.js 애플리케이션 빌드
RUN npm run build

# 7. Next.js 서버 실행
CMD ["npm", "start"]