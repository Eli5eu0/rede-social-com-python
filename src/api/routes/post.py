from fastapi import APIRouter, Depends, Request
from src.services.post import PostService
from src.api.dtos.posts import PostCreation
from src.api.authentication import login_required
from typing import Annotated

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    responses={404: {"description": "Not found"}},
)


@router.post("/create")
@login_required
async def create_post(
    request: Request,
    body: PostCreation, 
    service: Annotated[PostService, Depends(PostService)]
):
    
    response = await service.create_post(
        user= request.current_user, 
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
