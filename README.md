## 1. Project Outline

### 1. **개발 환경 설정**
   - **VSCode 설치 및 설정**: 개발에 필요한 확장 도구 설치 (ESLint, Prettier 등).
   - **Docker 설치 및 설정**: Docker와 Docker Compose 설치 및 기본 설정.
   - **Git 및 GitHub 리포지토리 설정**: 프로젝트의 Monorepo를 관리할 GitHub 리포지토리 생성.

### 2. **프로젝트 구조 설정**
   - **Monorepo 초기 설정**: 루트 디렉토리와 각 서비스(백엔드, 프론트엔드) 폴더 생성.
   - **FastAPI 백엔드 설정**: FastAPI 초기 설정 및 간단한 API 엔드포인트 구현.
   - **Next.js 프론트엔드 설정**: Next.js 초기 설정 및 기본 페이지 구현.
   - **Supabase 설정**: Supabase 프로젝트 생성 및 데이터베이스와 인증 설정.

### 3. **Docker를 통한 로컬 개발 환경 구축**
   - **Docker Compose 설정**: FastAPI, Next.js, Supabase 로컬 인스턴스를 포함하는 Docker Compose 파일 작성.
   - **로컬 개발 환경 실행**: `docker-compose up` 명령어로 모든 서비스를 로컬에서 실행.

### 4. **코드 품질 및 테스트 설정**
   - **Linting 설정**: ESLint (Next.js)와 Pylint/Flake8 (FastAPI) 설정.
   - **Testing 설정**: Jest (Next.js)와 pytest (FastAPI) 테스트 설정 및 기본 테스트 케이스 작성.
   - **Prettier 설정**: 코드 포맷팅을 위한 Prettier 설정.

### 5. **CI/CD 파이프라인 구축**
   - **GitHub Actions 설정**: CI/CD 파이프라인 구성 (Linting, Testing, Docker 이미지 빌드).
   - **Heroku 배포 설정**: Heroku에 FastAPI와 Next.js 애플리케이션 배포.

### 6. **Heroku 및 Supabase 배포**
   - **Heroku 초기 설정**: Heroku CLI를 사용해 Heroku 애플리케이션 생성 및 환경 변수 설정.
   - **Heroku Container Registry**: Docker 이미지를 Heroku에 푸시하여 애플리케이션 배포.
   - **Supabase 연동**: Supabase와 Heroku 애플리케이션 연동, 데이터베이스 및 인증 연동 확인.

### 7. **모니터링 및 최적화**
   - **Sentry 설정**: 애플리케이션의 에러 추적 및 성능 모니터링 설정.
   - **Heroku 로그 모니터링**: Heroku 로그를 통해 애플리케이션 상태 모니터링.

### 8. **지속적인 개발 및 유지보수**
   - **새 기능 개발**: 새로운 기능을 개발하고, CI/CD 파이프라인을 통해 자동으로 배포.
   - **버그 수정 및 최적화**: 로그와 모니터링 데이터를 기반으로 버그 수정 및 성능 최적화.


## 2. 개발환경 설정

### 1. **VSCode 설치 및 설정**

#### 1.1. **VSCode 필수확장도구 **

- **ESLint**: JavaScript/TypeScript 코드의 품질을 유지하는 도구입니다. 
- **Prettier**: 코드 포매터로, 코드 스타일을 일관되게 유지할 수 있습니다.
- **Python**: FastAPI를 위한 Python 개발 도구입니다.
- **Docker**: Docker 컨테이너 관리를 위한 도구입니다.
- **GitLens**: Git 기록을 시각적으로 관리하는 도구입니다.

### 2. **Docker 및 Docker Compose 설치**

#### 2.1. **Docker 설치**
- [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop) 사이트에서 설치 프로그램을 다운로드하고 설치합니다.
- 설치 후, Docker Desktop을 실행합니다. Docker가 정상적으로 설치되었는지 확인하려면 터미널에서 다음 명령을 실행합니다:
  ```bash
  docker --version
  ```
  Docker 버전이 출력되면 설치가 완료된 것입니다.

#### 2.2. **Docker Compose 설치**
Docker Compose는 Docker와 함께 설치되므로, 별도의 설치 과정이 필요하지 않습니다. Docker Compose 버전을 확인하려면 다음 명령을 실행합니다:
  ```bash
  docker-compose --version
  ```
  Docker Compose 버전이 출력되면 설치가 완료된 것입니다.

### 3. **Git 및 GitHub 리포지토리 설정**

#### 3.1. **Git 설치**
- macOS에는 기본적으로 Git이 설치되어 있지만, 최신 버전이 아닌 경우 업데이트를 고려할 수 있습니다. Git이 설치되었는지 확인하려면 터미널에서 다음 명령을 실행합니다:
  ```bash
  git --version
  ```
  Git 버전이 출력되면 설치가 완료된 것입니다. 만약 Git이 설치되지 않았거나 업데이트가 필요하다면 [Git 다운로드 페이지](https://git-scm.com/)에서 최신 버전을 설치할 수 있습니다.

#### 3.2. **GitHub 계정 및 리포지토리 생성**
- [GitHub](https://github.com/)에 접속하여 계정을 생성합니다.
- 새로운 리포지토리를 생성합니다. 프로젝트의 Monorepo를 위해 `my-crm-project`와 같은 이름으로 리포지토리를 생성할 수 있습니다.
  - 리포지토리를 공개 또는 비공개로 설정합니다.
  - `.gitignore` 파일을 추가하고, `Python`, `Node` 항목을 선택합니다.

#### 3.3. **로컬 리포지토리 설정**
- 터미널에서 프로젝트 디렉토리를 생성하고, 해당 디렉토리로 이동합니다:
  ```bash
  mkdir my-crm-project
  cd my-crm-project
  ```
- 로컬 리포지토리를 GitHub 리포지토리와 연결합니다:
  ```bash
  git init
  git remote add origin https://github.com/your-username/my-crm-project.git
  ```
  이 명령에서 `your-username`과 `my-crm-project`를 자신의 GitHub 사용자명과 리포지토리 이름으로 바꿉니다.

#### 3.4. **첫 번째 커밋**
- 프로젝트 루트 디렉토리에 `README.md` 파일을 생성하고 간단한 설명을 추가합니다:
  ```bash
  echo "# My CRM Project" >> README.md
  ```
- 변경 사항을 커밋하고, GitHub에 푸시합니다:
  ```bash
  git add .
  git commit -m "Initial commit"
  git push -u origin main
  ```

### 4. **Supabase 설정**
이 단계에서는 Supabase를 로컬에서 실행하기 위해 필요한 초기 설정을 완료합니다.

#### 4.1. **Supabase CLI 설치**
Supabase CLI는 Supabase 프로젝트를 로컬에서 관리할 수 있게 해줍니다.

- 터미널에서 다음 명령을 실행하여 Supabase CLI를 설치합니다:
  ```bash
  npm install -g supabase
  ```
  
- 설치 후, 다음 명령으로 CLI가 정상적으로 설치되었는지 확인합니다:
  ```bash
  supabase --version
  ```

#### 4.2. **Supabase 프로젝트 초기화**
- 프로젝트 루트 디렉토리에서 Supabase 프로젝트를 초기화합니다:
  ```bash
  supabase init
  ```
- 이 명령어는 Supabase 관련 파일과 디렉토리를 생성합니다.
