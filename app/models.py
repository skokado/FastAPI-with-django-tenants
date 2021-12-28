import sqlalchemy as sa
from sqlalchemy.orm import relationship

from app.database import Base, PUBLIC_SCHEMA_NAME

# Create your models here.
class BaseModel(Base):
    __abstract__ = True
    # マルチテナントなモデル定義の方法
    # See also: https://docs.sqlalchemy.org/en/14/changelog/migration_11.html#multi-tenancy-schema-translation-for-table-objects
    __table_args__ = {'schema': PUBLIC_SCHEMA_NAME}

    id = sa.Column(sa.Integer, primary_key=True, index=True)


class Author(BaseModel):
    __tablename__ = 'authors'

    name = sa.Column(sa.String)
    blogs = relationship('Blog', back_populates='author')


class Blog(BaseModel):
    __tablename__ = 'blogs'

    author = relationship(Author, back_populates='blogs')
    author_id = sa.Column(sa.Integer, sa.ForeignKey(Author.id))

    title = sa.Column(sa.String)
    body = sa.Column(sa.Text, default='')
