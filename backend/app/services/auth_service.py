from app.utils.security import hash_password, verify_password
from app.core.security import create_access_token


def register_user(db, user_data):
    from app.models.user import User

    hashed_pw = hash_password(user_data.password)

    user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hashed_pw
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def authenticate_user(db, email: str, password: str):
    from app.models.user import User

    user = db.query(User).filter(User.email == email).first()

    if not user:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    token = create_access_token({"sub": str(user.id)})

    return {
        "user": user,
        "access_token": token
    }