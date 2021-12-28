# FastAPI-with-django-tenants

django-tenants を使った、マルチテナントなFastAPI(SQLAlchemy)サンプル

# Usage

## テナント作成

```shell
$ docker-compose up -d db

$ cd app/admin
$ # Shared アプリのマイグレーション
$ ./manage.py migrate_schemas --shared
$ # 管理用テナント(public)の作成
$ ./manage.py create_tenant
schema name: public
テナント名: public
domain: public.localhost
is primary (leave blank to use 'True'): # Empty Enter

$ ./manage.py create_tenant_superuser --schema public
$ ./manage.py runserver
# => browse http://public.localhost:8000/admin
# (管理画面からテナントとドメインを作成する)
```

## API起動

```shell
$ # cd $WORKSPACE_DIR
$ uvicorn app.main:app --port 8001 --reload
# => browse http://localhost:8001/docs/
```
