from typing import List

from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm.session import Session

from app.dependencies import get_db
from app import models, schemas

app = FastAPI()


# Blog endpoint
router = APIRouter(prefix='/blogs', tags=['Blogs'])

# CRUD for Author
@router.get('/author/list', response_model=List[schemas.Author])
def list_authors(db: Session = Depends(get_db)):
    return db.query(models.Author).all()


@router.post('/author/', response_model=schemas.Author)
def create_author(request: schemas.AuthorBase, db: Session = Depends(get_db)):
    new_author = models.Author(
        name=request.name
    )
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author


# CRUD for Blog
@router.get('/blog/list', response_model=List[schemas.Blog])
def list_blogs(db: Session = Depends(get_db)):
    return db.query(models.Blog).all()


@router.get('/blog/list/author/{author_id}', response_model=List[schemas.Blog])
def list_blogs_of_author(author_id: int, db: Session = Depends(get_db)):
    author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if not author:
        raise HTTPException(
            status_code=404,
            detail=f'No author found id={author_id}'
        )
    return author.blogs


@router.post('/blog/', response_model=schemas.Blog)
def create_blog(request: schemas.AuthorBase, db: Session = Depends(get_db)):
    new_blog = models.Blog(
        author_id=request.author_id,
        title=request.title,
        body=request.body,
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

# Register routers
app.include_router(router)
