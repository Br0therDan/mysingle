from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from app.db.base import SQLModel  # SQLModel의 메타데이터 임포트
from app.core.config import settings  # 설정에서 DATABASE_URL 가져오기

## Alembic config 객체를 통해 사용 중인 .ini 파일의 값을 액세스 함
config = context.config

# 설정파일을 읽어서 로깅 설정을 초기화
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 모델의 메타데이터 객체를 여기에 추가하여 'autogenerate'를 지원함. target_metadata = mymodel.Base.metadata
target_metadata = SQLModel.metadata


def run_migrations_offline() -> None:
    """ 오프라인 모드에서 마이그레이션을 실행
    네트워크를 통한 데이터베이스 연결 없이 데이터베이스 스키마 변경을 추적하고, 마이그레이션 파일을 생성함
    특정 SQL 직접 작성해야 하거나, 데이터베이스를 수동제어 하고자 할때 효과적임
    """
    url = settings.DATABASE_URL
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """온라인모드 마이그레이션 실행
    엔진을 생성하고 컨텍스트와의 연결을 설정 함
    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        url=settings.DATABASE_URL,  # 데이터베이스 URL을 직접 설정
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
