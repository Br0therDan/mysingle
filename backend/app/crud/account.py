# app/crud/account.py

from sqlalchemy.orm import Session
from app.models.account import Account
from app.schemas.account import AccountCreate, AccountUpdate

def get_account(db: Session, account_id: str):
    return db.query(Account).filter(Account.id == account_id).first()

def get_accounts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Account).offset(skip).limit(limit).all()

def create_account(db: Session, account: AccountCreate):
    db_account = Account(**account.dict())
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

def update_account(db: Session, account_id: str, account: AccountUpdate):
    db_account = get_account(db, account_id)
    if not db_account:
        return None
    for key, value in account.dict(exclude_unset=True).items():
        setattr(db_account, key, value)
    db.commit()
    db.refresh(db_account)
    return db_account

def delete_account(db: Session, account_id: str):
    db_account = get_account(db, account_id)
    if db_account:
        db.delete(db_account)
        db.commit()
    return db_account

# Related operations: Get all contacts related to an account
def get_account_contacts(db: Session, account_id: str):
    account = get_account(db, account_id)
    if account:
        return account.contacts
    return []