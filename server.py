import os
from endpoints import *
from utils import get_admin_user, create_admin_user

@app.get("/", include_in_schema=False)
def home(session: SessionDep):
    return "Welcome to sterling-dwellings system API"
