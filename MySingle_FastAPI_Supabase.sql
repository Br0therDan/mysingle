/* Drop Indexes */

DROP INDEX IF EXISTS Index_accounts;
DROP INDEX IF EXISTS index_daily_scrums;
DROP INDEX IF EXISTS index_daily_scrum_task_association;
DROP INDEX IF EXISTS index_daily_scrum_update;
DROP INDEX IF EXISTS index_opportunity;
DROP INDEX IF EXISTS index_orgs;
DROP INDEX IF EXISTS index_profiles_projects;
DROP INDEX IF EXISTS index_project;
DROP INDEX IF EXISTS index_sprint;
DROP INDEX IF EXISTS index_tasks;

/* Drop Triggers */

DROP TRIGGER IF EXISTS trg_generate_full_name ON public.profiles;
DROP TRIGGER IF EXISTS set_timestamp ON public.profiles;

/* Drop Tables */

DROP TABLE IF EXISTS public.daily_scrum_task_association;
DROP TABLE IF EXISTS public.daily_scrum_update;
DROP TABLE IF EXISTS public.daily_scrums;
DROP TABLE IF EXISTS public.profiles_projects;
DROP TABLE IF EXISTS public.tasks;
DROP TABLE IF EXISTS public.sprints;
DROP TABLE IF EXISTS public.projects;
DROP TABLE IF EXISTS public.opportunities;
DROP TABLE IF EXISTS public.accounts;
DROP TABLE IF EXISTS public.profiles;
DROP TABLE IF EXISTS public.organization;

/* Create Tables */

-- 어카운트
CREATE TABLE public.accounts
(
	account_id uuid DEFAULT gen_random_uuid() NOT NULL,
	account_name varchar(100) NOT NULL UNIQUE,
	profile_id uuid NOT NULL,
	account_type varchar(50) DEFAULT 'Prospect' NOT NULL,
	created_at timestamp with time zone DEFAULT NOW(),
	updated_at timestamp with time zone DEFAULT NOW(),
	PRIMARY KEY (account_id)
);

-- 데일리 스크럼
CREATE TABLE public.daily_scrums
(
	daily_scrum_id uuid DEFAULT gen_random_uuid() NOT NULL,
	scrum_date date NOT NULL,
	summary text,
	sprint_id uuid NOT NULL,
	project_id uuid NOT NULL,
	PRIMARY KEY (daily_scrum_id)
);

-- 스크럼-테스크-연결
CREATE TABLE public.daily_scrum_task_association
(
	task_id uuid NOT NULL,
	daily_scrum_id uuid NOT NULL,
	UNIQUE (task_id, daily_scrum_id)
);

-- 데일리 스크럼 업데이트
CREATE TABLE public.daily_scrum_update
(
	update_id uuid DEFAULT gen_random_uuid() NOT NULL,
	yesterday_work text,
	today_work text,
	impediemnts text,
	created_at timestamp with time zone DEFAULT NOW() NOT NULL,
	daily_scrum_id uuid NOT NULL,
	profile_id uuid NOT NULL,
	PRIMARY KEY (update_id)
);

-- 영업기회
CREATE TABLE public.opportunities
(
	opportunity_id uuid DEFAULT gen_random_uuid() NOT NULL,
	opportunity_name varchar(100) NOT NULL,
	close_date date NOT NULL,
	ACV decimal(15,2) NOT NULL,
	account_id uuid NOT NULL,
	stage varchar(50) NOT NULL,
	forecast_category varchar(50) NOT NULL,
	description text,
	currency_code char(3) NOT NULL,
	created_at timestamp with time zone DEFAULT NOW(),
	updated_at timestamp with time zone DEFAULT NOW(),
	profile_id uuid NOT NULL,
	PRIMARY KEY (opportunity_id)
);

-- 조직
CREATE TABLE public.organization
(
	org_id uuid DEFAULT gen_random_uuid() NOT NULL,
	task_name varchar(100),
	org_type varchar(50),
	created_at timestamp with time zone DEFAULT NOW(),
	updated_at timestamp with time zone DEFAULT NOW(),
	PRIMARY KEY (org_id)
);

-- 사용자
CREATE TABLE public.profiles
(
	profile_id uuid DEFAULT gen_random_uuid() NOT NULL,
	username varchar(50) NOT NULL,
	email varchar(50) NOT NULL,
	org_id uuid NOT NULL,
	first_name varchar(30),
	last_name varchar(30),
	job_role varchar(30),
	full_name varchar(50),
	work_email varchar(50),
	is_verified boolean DEFAULT 'false' NOT NULL,
	created_at timestamp with time zone DEFAULT NOW(),
	updated_at timestamp with time zone DEFAULT NOW(),
	PRIMARY KEY (profile_id)
);

-- 사용자-프로젝트 링크
CREATE TABLE public.profiles_projects
(
	profile_id uuid NOT NULL,
	project_id uuid NOT NULL,
	role varchar(20) NOT NULL,
	joined_at timestamp with time zone DEFAULT NOW() NOT NULL,
	UNIQUE (profile_id, project_id)
);

-- 프로젝트
CREATE TABLE public.projects
(
	project_id uuid DEFAULT gen_random_uuid() NOT NULL,
	project_name varchar(100) NOT NULL,
	account_id uuid NOT NULL,
	opportunity_id uuid,
	profile_id uuid NOT NULL,
	description text,
	created_at timestamp with time zone DEFAULT NOW() NOT NULL,
	updated_at timestamp with time zone DEFAULT NOW(),
	PRIMARY KEY (project_id)
);

-- 스프린트
CREATE TABLE public.sprints
(
	sprint_id uuid DEFAULT gen_random_uuid() NOT NULL,
	sprint_name varchar(100) NOT NULL,
	project_id uuid NOT NULL,
	goal varchar(150),
	start_date date NOT NULL,
	end_date date NOT NULL,
	status varchar(50) NOT NULL,
	created_at timestamp with time zone DEFAULT NOW(),
	updated_at timestamp with time zone DEFAULT NOW(),
	PRIMARY KEY (sprint_id)
);

-- 작업
CREATE TABLE public.tasks
(
	task_id uuid DEFAULT gen_random_uuid() NOT NULL,
	task_name varchar(100) NOT NULL,
	description text,
	priority varchar(50) DEFAULT 'Low' NOT NULL,
	status varchar(20) NOT NULL,
	assigned_to uuid NOT NULL,
	sprint_id uuid NOT NULL,
	created_at timestamp with time zone DEFAULT NOW(),
	updated_at timestamp with time zone DEFAULT NOW(),
	PRIMARY KEY (task_id)
);

/* Create Foreign Keys */

ALTER TABLE public.opportunities
	ADD FOREIGN KEY (account_id)
	REFERENCES public.accounts (account_id)
	ON UPDATE CASCADE
	ON DELETE CASCADE;

ALTER TABLE public.projects
	ADD FOREIGN KEY (account_id)
	REFERENCES public.accounts (account_id)
	ON UPDATE CASCADE
	ON DELETE CASCADE;

ALTER TABLE public.daily_scrum_task_association
	ADD FOREIGN KEY (daily_scrum_id)
	REFERENCES public.daily_scrums (daily_scrum_id)
	ON UPDATE CASCADE
	ON DELETE CASCADE;

ALTER TABLE public.daily_scrum_update
	ADD FOREIGN KEY (daily_scrum_id)
	REFERENCES public.daily_scrums (daily_scrum_id)
	ON UPDATE CASCADE
	ON DELETE CASCADE;

ALTER TABLE public.projects
	ADD FOREIGN KEY (opportunity_id)
	REFERENCES public.opportunities (opportunity_id)
	ON UPDATE CASCADE
	ON DELETE CASCADE;

ALTER TABLE public.profiles
	ADD FOREIGN KEY (org_id)
	REFERENCES public.organization (org_id)
	ON UPDATE CASCADE
	ON DELETE CASCADE;

ALTER TABLE public.accounts
	ADD FOREIGN KEY (profile_id)
	REFERENCES public.profiles (profile_id)
	ON UPDATE CASCADE
	ON DELETE CASCADE;

ALTER TABLE public.daily_scrum_update
	ADD FOREIGN KEY (profile_id)
	REFERENCES public.profiles (profile_id)
	ON UPDATE CASCADE
	ON DELETE CASCADE;

ALTER TABLE public.opportunities
	ADD FOREIGN KEY (profile_id)
	REFERENCES public.profiles (profile_id)
	ON UPDATE CASCADE
	ON DELETE CASCADE;

ALTER TABLE public.profiles_projects
	ADD FOREIGN KEY (profile_id)
	REFERENCES public.profiles (profile_id)
	ON UPDATE CASCADE
	ON DELETE CASCADE;

ALTER TABLE public.projects
	ADD FOREIGN KEY (profile_id)
	REFERENCES public.profiles (profile_id)
	ON UPDATE CASCADE
	ON DELETE CASCADE;

ALTER TABLE public.tasks
	ADD FOREIGN KEY (assigned_to)
	REFERENCES public.profiles (profile_id)
	ON UPDATE CASCADE
	ON DELETE CASCADE;

ALTER TABLE public.daily_scrums
	ADD FOREIGN KEY (project_id)
	REFERENCES public.projects (project_id)
	ON UPDATE CASCADE
	ON DELETE CASCADE;

ALTER TABLE public.profiles_projects
	ADD FOREIGN KEY (project_id)
	REFERENCES public.projects (project_id)
	ON UPDATE CASCADE
	ON DELETE CASCADE;

ALTER TABLE public.sprints
	ADD FOREIGN KEY (project_id)
	REFERENCES public.projects (project_id)
	ON UPDATE CASCADE
	ON DELETE CASCADE;

ALTER TABLE public.daily_scrums
	ADD FOREIGN KEY (sprint_id)
	REFERENCES public.sprints (sprint_id)
	ON UPDATE CASCADE
	ON DELETE CASCADE;

ALTER TABLE public.tasks
	ADD FOREIGN KEY (sprint_id)
	REFERENCES public.sprints (sprint_id)
	ON UPDATE CASCADE
	ON DELETE CASCADE;

ALTER TABLE public.daily_scrum_task_association
	ADD FOREIGN KEY (task_id)
	REFERENCES public.tasks (task_id)
	ON UPDATE CASCADE
	ON DELETE CASCADE;

/* Create Triggers */

-- full_name 생성 함수
CREATE OR REPLACE FUNCTION generate_full_name() 
RETURNS TRIGGER AS $$
DECLARE
    first_char text;
BEGIN
    first_char := substring(NEW.first_name, 1, 1);
    IF first_char >= '\uAC00' AND first_char <= '\uD7A3' THEN
        NEW.full_name := NEW.last_name || NEW.first_name;
    ELSE
        NEW.full_name := NEW.first_name || ' ' || NEW.last_name;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- full_name 생성 트리거
CREATE TRIGGER trg_generate_full_name
BEFORE INSERT OR UPDATE ON public.profiles
FOR EACH ROW
EXECUTE FUNCTION generate_full_name();

-- 타임스탬프 업데이트 함수
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- 타임스탬프 업데이트 트리거
CREATE TRIGGER set_timestamp
BEFORE UPDATE ON public.profiles
FOR EACH ROW
EXECUTE FUNCTION update_timestamp();

/* Create Indexes */

CREATE INDEX Index_accounts ON public.accounts (account_id, account_name, profile_id);
CREATE INDEX index_daily_scrums ON public.daily_scrums (daily_scrum_id, scrum_date, sprint_id, project_id);
CREATE INDEX index_daily_scrum_task_association ON public.daily_scrum_task_association (task_id, daily_scrum_id);
CREATE INDEX index_daily_scrum_update ON public.daily_scrum_update (update_id, daily_scrum_id, profile_id);
CREATE INDEX index_opportunity ON public.opportunities (opportunity_id, opportunity_name, account_id, stage, forecast_category, close_date);
CREATE INDEX index_orgs ON public.organization (org_id);
CREATE INDEX index_profiles_projects ON public.profiles_projects (profile_id, project_id, role);
CREATE INDEX index_project ON public.projects (project_id, project_name, account_id, profile_id);
CREATE INDEX index_sprint ON public.sprints (sprint_id, sprint_name, project_id);
CREATE INDEX index_tasks ON public.tasks (task_id, task_name, assigned_to, sprint_id, status, priority);

/* Comments */

COMMENT ON TABLE public.accounts IS '어카운트';
COMMENT ON COLUMN public.accounts.account_id IS '계정ID';
COMMENT ON COLUMN public.accounts.account_name IS '계정명';
COMMENT ON COLUMN public.accounts.profile_id IS '계정관리자';
COMMENT ON COLUMN public.accounts.account_type IS '계정유형 : Prospect | Customer | Partner';
COMMENT ON COLUMN public.accounts.created_at IS '생성일시';
COMMENT ON COLUMN public.accounts.updated_at IS '수정일시';

COMMENT ON TABLE public.daily_scrums IS '데일리 스크럼';
COMMENT ON COLUMN public.daily_scrums.daily_scrum_id IS '데일리스크럼ID';
COMMENT ON COLUMN public.daily_scrums.scrum_date IS '스크럼 날짜';
COMMENT ON COLUMN public.daily_scrums.summary IS 'summary';
COMMENT ON COLUMN public.daily_scrums.sprint_id IS '스프린트ID';
COMMENT ON COLUMN public.daily_scrums.project_id IS '프로젝트ID';

COMMENT ON TABLE public.daily_scrum_task_association IS '스크럼-테스크-연결';
COMMENT ON COLUMN public.daily_scrum_task_association.task_id IS '작업ID';
COMMENT ON COLUMN public.daily_scrum_task_association.daily_scrum_id IS '데일리스크럼ID';

COMMENT ON TABLE public.daily_scrum_update IS '데일리 스크럼 업데이트';
COMMENT ON COLUMN public.daily_scrum_update.update_id IS '스크럼업데이트ID';
COMMENT ON COLUMN public.daily_scrum_update.yesterday_work IS '전날업무내용';
COMMENT ON COLUMN public.daily_scrum_update.today_work IS '오늘업무내용';
COMMENT ON COLUMN public.daily_scrum_update.impediemnts IS '장애물';
COMMENT ON COLUMN public.daily_scrum_update.created_at IS '생성일시';
COMMENT ON COLUMN public.daily_scrum_update.daily_scrum_id IS '데일리스크럼ID';
COMMENT ON COLUMN public.daily_scrum_update.profile_id IS '사용자ID';

COMMENT ON TABLE public.opportunities IS '영업기회';
COMMENT ON COLUMN public.opportunities.opportunity_id IS '기회ID';
COMMENT ON COLUMN public.opportunities.opportunity_name IS '기회명';
COMMENT ON COLUMN public.opportunities.close_date IS '미감일';
COMMENT ON COLUMN public.opportunities.ACV IS '연간계약금액';
COMMENT ON COLUMN public.opportunities.account_id IS '계정ID';
COMMENT ON COLUMN public.opportunities.stage IS '진행단계';
COMMENT ON COLUMN public.opportunities.forecast_category IS '예측범주';
COMMENT ON COLUMN public.opportunities.description IS '상세';
COMMENT ON COLUMN public.opportunities.currency_code IS '통화코드';
COMMENT ON COLUMN public.opportunities.created_at IS '생성일시';
COMMENT ON COLUMN public.opportunities.updated_at IS '수정일시';
COMMENT ON COLUMN public.opportunities.profile_id IS '사용자ID';

COMMENT ON TABLE public.organization IS '조직';
COMMENT ON COLUMN public.organization.org_id IS '조직ID';
COMMENT ON COLUMN public.organization.task_name IS '작업명';
COMMENT ON COLUMN public.organization.org_type IS '조직유형';
COMMENT ON COLUMN public.organization.created_at IS '생성일시';
COMMENT ON COLUMN public.organization.updated_at IS '수정일시';

COMMENT ON TABLE public.profiles IS '사용자';
COMMENT ON COLUMN public.profiles.profile_id IS '사용자ID';
COMMENT ON COLUMN public.profiles.username IS '사용자이름 : IdP 에서 가져옴';
COMMENT ON COLUMN public.profiles.email IS '이메일';
COMMENT ON COLUMN public.profiles.org_id IS '소속회사';
COMMENT ON COLUMN public.profiles.first_name IS '이름';
COMMENT ON COLUMN public.profiles.last_name IS '성';
COMMENT ON COLUMN public.profiles.job_role IS '직책';
COMMENT ON COLUMN public.profiles.full_name IS '성명';
COMMENT ON COLUMN public.profiles.work_email IS '업무용 이메일';
COMMENT ON COLUMN public.profiles.is_verified IS '검증';
COMMENT ON COLUMN public.profiles.created_at IS '생성일시';
COMMENT ON COLUMN public.profiles.updated_at IS '수정일시';

COMMENT ON TABLE public.profiles_projects IS '사용자-프로젝트 링크';
COMMENT ON COLUMN public.profiles_projects.profile_id IS '사용자ID';
COMMENT ON COLUMN public.profiles_projects.project_id IS '프로젝트ID';
COMMENT ON COLUMN public.profiles_projects.role IS '역할';
COMMENT ON COLUMN public.profiles_projects.joined_at IS '참여일';

COMMENT ON TABLE public.projects IS '프로젝트';
COMMENT ON COLUMN public.projects.project_id IS '프로젝트ID';
COMMENT ON COLUMN public.projects.project_name IS '프로젝트명';
COMMENT ON COLUMN public.projects.account_id IS '계정ID';
COMMENT ON COLUMN public.projects.opportunity_id IS '기회ID';
COMMENT ON COLUMN public.projects.profile_id IS '사용자ID';
COMMENT ON COLUMN public.projects.description IS '상세';
COMMENT ON COLUMN public.projects.created_at IS '생성일시';
COMMENT ON COLUMN public.projects.updated_at IS '수정일시';

COMMENT ON TABLE public.sprints IS '스프린트';
COMMENT ON COLUMN public.sprints.sprint_id IS '스프린트ID';
COMMENT ON COLUMN public.sprints.sprint_name IS '스프린트명';
COMMENT ON COLUMN public.sprints.project_id IS '프로젝트ID';
COMMENT ON COLUMN public.sprints.goal IS '목표';
COMMENT ON COLUMN public.sprints.start_date IS '시작일';
COMMENT ON COLUMN public.sprints.end_date IS '종료일';
COMMENT ON COLUMN public.sprints.status IS '상태';

COMMENT ON TABLE public.tasks IS '작업';
COMMENT ON COLUMN public.tasks.task_id IS '작업ID';
COMMENT ON COLUMN public.tasks.task_name IS '작업명';
COMMENT ON COLUMN public.tasks.description IS '상세';
COMMENT ON COLUMN public.tasks.priority IS '중요도';
COMMENT ON COLUMN public.tasks.status IS '상태';
COMMENT ON COLUMN public.tasks.assigned_to IS '담당자ID';
COMMENT ON COLUMN public.tasks.sprint_id IS '스프린트ID';
COMMENT ON COLUMN public.tasks.created_at IS '생성일시';
COMMENT ON COLUMN public.tasks.updated_at IS '수정일시';
