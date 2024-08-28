# app/tests/test_models.py

from app.models import Account
from sqlmodel import SQLModel, create_engine, Session

def test_account_model():
    account = Account(account_name="Test Account", account_type="Customer")
    assert account.account_name == "Test Account"
    assert account.account_type == "Customer"

def test_account_creation_in_db():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    account = Account(account_name="Test Account", account_type="Customer")

    with Session(engine) as session:
        session.add(account)
        session.commit()
        session.refresh(account)
        assert account.id is not None
        assert account.account_name == "Test Account"
