from typing import Any

from fastapi import APIRouter, Depends
from pydantic.networks import EmailStr

from app import models, schemas
from app.api import deps
from app.core.celery_app import celery_app
from app.utils import send_test_email
from app.data import ALLERGY_LIST, SYMPTOM_LIST

router = APIRouter()


@router.post("/test-celery/", response_model=schemas.Msg, status_code=201)
def test_celery(
    msg: schemas.Msg,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> Any:
    """
    Test Celery worker.
    """
    celery_app.send_task("app.worker.test_celery", args=[msg.msg])
    return {"msg": "Word received"}


@router.post("/test-email/", response_model=schemas.Msg, status_code=201)
def test_email(
    email_to: EmailStr,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> Any:
    """
    Test emails.
    """
    send_test_email(email_to=email_to)
    return {"msg": "Test email sent"}


@router.post("/test-email/", response_model=schemas.Msg, status_code=201)
def test_sms(
    email_to: EmailStr,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> Any:
    """
    Test SMS.
    """
    send_test_email(email_to=email_to)
    return {"msg": "Test email sent"}


@router.get("/allergies")
def get_allergy_list() -> Any:
    """
    Get the list of the allergies
    """
    return {'allergy_list': ALLERGY_LIST}


@router.get("/symtoms")
def get_symptom_list() -> Any:
    """
    Get the list of the symptoms
    """
    return {'symptom_list': SYMPTOM_LIST}
