import logging
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from auth.auth import get_current_user
from config.database import async_get_db
from crud.product_crud import crud_product
from schemas.product import ProductCreate, ProductRead, ProductUpdate
from schemas.user import UserIn

router = APIRouter(
    prefix="/product",
    tags=["product"]
)


@router.post("/", status_code=201, response_model=ProductRead)
async def create_product(
        data: ProductCreate,
        session: Annotated[AsyncSession, Depends(async_get_db)],
        user: UserIn = Depends(get_current_user)
):
    """
    Create a new product.

    Args:
        data (ProductCreate): Details of the new product.
        session (AsyncSession): Database session.
        user (UserIn): Current user's details.

    Returns:
        ProductRead: Details of the newly created product.
    """
    try:
        created_product: ProductRead = await crud_product.create(db=session, object=data)
    except IntegrityError as e:
        logging.error(e)
        await session.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Product is already exists!"
        )
    else:
        return created_product


@router.get("/{product_id}", status_code=201, response_model=ProductRead)
async def read_product(
        product_id: str,
        session: Annotated[AsyncSession, Depends(async_get_db)],
        user: UserIn = Depends(get_current_user)
):
    """
    Read a product.

    Args:
        session (AsyncSession): Database session.
        product_id (str): ID of the product.
        user (UserIn): Current user's details.

    Returns:
        ProductRead: Details of the newly created product.
    """

    red_product: ProductRead = await crud_product.get(
        db=session, schema_to_select=ProductRead,
        id=product_id, is_deleted=False
    )
    return red_product


@router.patch("/{product_id}")
async def patch_product(
        product_id: str,
        values: ProductUpdate,
        session: Annotated[AsyncSession, Depends(async_get_db)],
        user: UserIn = Depends(get_current_user)
):
    """
    Patch a product.

    Args:
        values (ProductUpdate): Values to update the product with.
        product_id (str): ID of the product.
        session (AsyncSession): Database session.
        user (UserIn): Current user's details.

    Returns:
        None
    """
    await crud_product.update(db=session, object=values, id=product_id)
    return {"message": "Product updated"}


@router.delete("/{product_id}")
async def delete_product(
        product_id: str,
        session: Annotated[AsyncSession, Depends(async_get_db)],
        user: UserIn = Depends(get_current_user)
):
    """
    Delete a product.

    Args:
        session (AsyncSession): Database session.
        product_id (str): ID of the product.
        user (UserIn): Current user's details.

    Returns:
        None
    """
    await crud_product.delete(db=session, id=product_id)
    return {"message": "Product deleted"}
