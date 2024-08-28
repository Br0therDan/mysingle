# app/api/v1/endpoints/account.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.account import Account, AccountCreate, AccountUpdate
from app.crud.account import (get_account, get_accounts, create_account, update_account, delete_account, get_account_contacts)
from app.db.session import get_db
from app.core.security import get_current_user
from typing import Optional

router = APIRouter()

@router.get("/", response_model=list[Account])
def read_accounts(skip: int = 0, limit: int = 10, account_type: Optional[str] = None, segment: Optional[str] = None, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    query = db.query(Account)
    if account_type:
        query = query.filter(Account.account_type == account_type)
    if segment:
        query = query.filter(Account.segment == segment)
    return query.offset(skip).limit(limit).all()

@router.get("/{account_id}", response_model=Account)
def read_account(account_id: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_account = get_account(db, account_id)
    if not db_account:
        raise HTTPException(status_code=404, detail="Account not found")
    return db_account

@router.post("/", response_model=Account)
def create_new_account(account: AccountCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return create_account(db, account)

@router.put("/{account_id}", response_model=Account)
def update_existing_account(account_id: str, account: AccountUpdate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_account = update_account(db, account_id, account)
    if not db_account:
        raise HTTPException(status_code=404, detail="Account not found")
    return db_account

@router.delete("/{account_id}", response_model=Account)
def delete_existing_account(account_id: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_account = delete_account(db, account_id)
    if not db_account:
        raise HTTPException(status_code=404, detail="Account not found")
    return db_account

@router.get("/{account_id}/contacts", response_model=list)
def read_account_contacts(account_id: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return get_account_contacts(db, account_id)