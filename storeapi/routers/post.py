from fastapi import APIRouter

from storeapi.models.post import UserPost, UserPostIn

router = APIRouter()

posts_table = {}

@router.post("/", response_model=UserPost)
async def create_post(post: UserPostIn):
    data = post.model_dump()
    last_record_id = len(posts_table)
    new_post = {**data, "id": last_record_id}
    posts_table[last_record_id] = new_post
    return new_post

@router.get("/post", response_model=list[UserPost])
async def get_all_posts():
    return list(posts_table.values())