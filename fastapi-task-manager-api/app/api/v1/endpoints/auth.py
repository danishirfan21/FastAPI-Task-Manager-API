from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
async def register():
    return {"msg": "Register endpoint"}

@router.post("/login")
async def login():
    return {"msg": "Login endpoint"}

@router.get("/me")
async def get_me():
    return {"msg": "Current user profile"}
