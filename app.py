from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

class Person(BaseModel):
    name: str
    occupation: str
    address: str

app = FastAPI()

data = [
  {
    "name": "John Doe",
    "occupation": "Software Engineer",
    "address": "123 Main St"
  },
  {
    "name": "Jane Smith",
    "occupation": "Data Scientist",
    "address": "456 Elm St"
  },
  {
    "name": "Michael Johnson",
    "occupation": "Web Developer",
    "address": "789 Oak St"
  },
  {
    "name": "Emily Brown",
    "occupation": "UX Designer",
    "address": "101 Maple Ave"
  },
  {
    "name": "David Lee",
    "occupation": "Product Manager",
    "address": "202 Pine St"
  },
  {
    "name": "Sarah Taylor",
    "occupation": "Marketing Specialist",
    "address": "303 Cedar St"
  },
  {
    "name": "Chris Evans",
    "occupation": "Graphic Designer",
    "address": "404 Walnut St"
  },
  {
    "name": "Jessica White",
    "occupation": "Financial Analyst",
    "address": "505 Birch St"
  },
  {
    "name": "Matthew Miller",
    "occupation": "Systems Administrator",
    "address": "606 Spruce St"
  },
  {
    "name": "Amanda Martinez",
    "occupation": "HR Coordinator",
    "address": "707 Chestnut St"
  }
]


@app.get("/name")
async def get_person_name():
    list_for_name = []
    for name in data:
        list_for_name.append(name["name"])
    return list_for_name

@app.get("/occupation")
async def get_person_occupation():
    list_for_occupation =[]
    for occupation in data:
        list_for_occupation.append(occupation["occupation"])
    return list_for_occupation

@app.get("/address")
async def get_person_address():
    list_for_address = []
    for address in data:
        list_for_address.append(address["address"])
    return list_for_address