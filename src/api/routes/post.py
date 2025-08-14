from fastapi import APIRouter, Depends
from src.services.post import PostService
from src.api.dtos.posts import PostCreation
from src.api.authentication import verify_token
from src.datalayer.models.user import UserModel
from typing import Annotated

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    responses={404: {"description": "Not found"}},
)


@router.post("/create")
async def create_post(
    body: PostCreation, 
    current_user: Annotated[UserModel, Depends(verify_token)],
    service: Annotated[PostService, Depends(PostService)]
):
    
    response = await service.create_post(
        user= current_user, 
        message=body.message
    )
    
    return {"Post": response}

@router.get('/all-posts')
async def get_posts(service: Annotated[PostService, Depends(PostService)]):
    response = await service.get_all_posts()
    return [{"Post": response}]

@router.get('/{user_id}')
async def get_user_posts(
    user_id: int,
    service: Annotated[PostService, Depends(PostService)]
):
    response = await service.get_user_posts(user_id)
    return {"Post": response}
