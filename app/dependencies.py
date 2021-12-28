from typing import Generator

from fastapi import HTTPException
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.sql import exists, select, text

from app.database import engine, PUBLIC_SCHEMA_NAME


def exists_schema(db: Session, schema_name: str):
    q = exists(
        select(
            [text('schema_name')]).select_from(text('information_schema.schemata')
        ).where(text(f"schema_name = '{schema_name}'"))
    )
    return db.query(q).scalar()


def get_db(schema_name: str) -> Generator[Session, None, None]:
    # マルチテナントなデータベース構成をスキーマ分割によって実現するための設定
    # See also: https://docs.sqlalchemy.org/en/14/changelog/migration_11.html#multi-tenancy-schema-translation-for-table-objects
    # https://github.com/sqlalchemy/sqlalchemy/discussions/5978#discussioncomment-406283
    SessionLocal = sessionmaker(
        autocommit=False, autoflush=False,
        bind=engine.execution_options(schema_translate_map={
            None: schema_name,
            PUBLIC_SCHEMA_NAME: schema_name,
        }),
    )
    db = SessionLocal()
    if not exists_schema(db, schema_name):
        raise HTTPException(
            status_code=404,
            detail=f'tenant {schema_name} does not exist.'
        )
    try:
        yield db
    finally:
        db.close()
