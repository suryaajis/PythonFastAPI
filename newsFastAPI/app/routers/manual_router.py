from fastapi import APIRouter, HTTPException, status
from ..schemas.post_schema import Post

router = APIRouter()

'''
@router.get("/posts")
def read_posts():
  cursor.execute("""SELECT * FROM posts """)
  posts = cursor.fetchall()
  return {"data": posts}

@router.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(req: Post):
  cursor.execute(""" INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, (req.title, req.content, req.published))
  new_post = cursor.fetchone()
  
  conn.commit()
  return {"data": new_post}
  
@router.get("/posts/{id}")
def read_post_by_id(id: int):
  cursor.execute(""" SELECT * FROM posts WHERE id = %s """, (id,))
  find_post = cursor.fetchone()
  
  if not find_post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with ID {id} was not found")
  
  return {"data": find_post} 

@router.delete("/posts/{id}")
def remove_post(id: int):
  cursor.execute(""" SELECT * FROM posts WHERE id = %s """, (id,))
  find_post = cursor.fetchone()
  
  if not find_post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with ID {id} was not found")
  
  cursor.execute(""" DELETE FROM posts WHERE id = %s RETURNING * """, (id,))
  deleted_post = cursor.fetchone()
  
  conn.commit()
  return {"data": deleted_post, "message": f"Post ID {id} has been deleted"}

@router.put("/posts/{id}")
def update_post(id: int, req: Post):
  cursor.execute(""" SELECT * FROM posts WHERE id = %s """, (id,))
  find_post = cursor.fetchone()
  
  if not find_post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with ID {id} was not found")
  
  cursor.execute(""" UPDATE posts SET title=%s, content=%s, published=%s WHERE id = %s RETURNING * """, (req.title, req.content, req.published, id,))
  updated_post = cursor.fetchone()
  
  conn.commit()
  return {"data": updated_post}
'''