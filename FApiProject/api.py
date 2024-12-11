from fastapi import FastAPI, HTTPException
import uvicorn
from config import *
from models import *
from response_models import *

app = FastAPI(
    title="MyTitle",
    description="PracticeFastAPI",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

@app.get("/users/select/{user_id}")
async def get_users(user_id: int):
    try:
        with DBSettings.get_session() as conn:
            user = conn.query(User).filter(User.id == user_id).first()
            return user
    except:
        raise HTTPException(status_code=404, detail="User not found")

@app.post("/users/add", response_model=UserCreate)
async def add_users(user_name: str, user_role: str):
    user = UserCreate(name=user_name, role=user_role)
    with DBSettings.get_session() as conn:
        roleDB = conn.query(Role).filter(Role.name == user.role).first()
        if (roleDB == None):
            raise HTTPException(status_code=404, detail="We haven't this role")
        else:
            new_user = User(name = user.name, role_id = roleDB.id)
            conn.add(new_user)
            conn.commit()
            print(F"Успешно добавлен новый пользователь: {new_user.name}")
            return user

@app.delete("/users/delete/{user_id}")
async def delete_users(user_id: int):
    with DBSettings.get_session() as conn:
        user = conn.query(User).filter(User.id == user_id).first()
        if (user == None):
            raise HTTPException(status_code=404, detail="User not found")
        conn.delete(user)
        conn.commit()
        print(f"Успешно удалён пользователь: {user.name}")
        return user
    
@app.put("/users/update/{user_id}", response_model=UserUpdate)
async def update_users(user_id: int, new_user_name: str, new_user_role: str):
    with DBSettings.get_session() as conn:
        user = conn.query(User).filter(User.id == user_id).first()
        if (user == None):
            raise HTTPException(status_code=404, detail="User not found")
        
        roleDB = conn.query(Role).filter(Role.name == new_user_role).first()
        if (roleDB == None):
            raise HTTPException(status_code=404, detail="We haven't this role")
        else:
            update_user_request = update(User).where(User.id == user_id).values(name = new_user_name, role_id = roleDB.id)
            conn.execute(update_user_request)
            conn.commit()
            print(f"Успешно обновлены данные пользователя: {user.name}")
            return UserUpdate(id=user.id, name=new_user_name, role=new_user_role)
        
uvicorn.run(app, host="127.0.0.1", port=8000)