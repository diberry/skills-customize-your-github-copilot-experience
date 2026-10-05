from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field


app = FastAPI(title="Mergington High School Clubs API")


class ClubInput(BaseModel):
    name: str = Field(min_length=2, max_length=60)
    description: str = Field(min_length=10, max_length=200)
    member_count: int = Field(ge=0)


class Club(ClubInput):
    id: int


clubs = [
    Club(
        id=1,
        name="Robotics Club",
        description="Students design and build robots for competitions.",
        member_count=18,
    ),
    Club(
        id=2,
        name="Coding Club",
        description="Students create software projects and practice programming.",
        member_count=24,
    ),
]


@app.get("/clubs", response_model=list[Club])
def list_clubs():
    pass


@app.get("/clubs/{club_id}", response_model=Club)
def get_club(club_id: int):
    pass


@app.post("/clubs", response_model=Club, status_code=status.HTTP_201_CREATED)
def create_club(club_input: ClubInput):
    pass


@app.put("/clubs/{club_id}", response_model=Club)
def update_club(club_id: int, club_input: ClubInput):
    pass


@app.delete("/clubs/{club_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_club(club_id: int, response: Response):
    pass