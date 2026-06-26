from fastapi import FastAPI

app = FastAPI()# this create an app called "app"




#this import the routes building in a diferent file
from routes.auth_routes import auth_router 
from routes.order_routes import order_router



#this include the routes in the app
app.include_router(auth_router)
app.include_router(order_router)