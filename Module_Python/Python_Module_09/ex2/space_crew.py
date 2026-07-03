#!/usr/bin/env python3
from pydantic import BaseModel, ValidationError, Field, model_validator
from enum import Enum
from datetime import datetime


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=5, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field(default_factory=datetime.now)
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=3, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=100000.0)

    @model_validator(mode='after')
    def mission_validation(self) -> 'SpaceMission':
        if not self.mission_id.startswith('M'):
            raise ValueError("The mission ID must begin with 'M'.")

        if not any(
            member.rank in
            (Rank.COMMANDER, Rank.CAPTAIN) for member in self.crew
        ):
            raise ValueError("Mission must have at least"
                             " one Commander or Captain.")

        if not any(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active.")

        if self.duration_days > 365:
            total_member = len(self.crew)
            experienced = [member for member in
                           self.crew if member.years_experience >= 5]
            if len(experienced) / total_member < 0.5:
                raise ValueError("Long-duration missions require at least"
                                 " 50% experienced crew members.")

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 40)

    rank = [Rank.COMMANDER, Rank.OFFICER]
    print("Valid mission created:")
    for r in rank:
        try:
            mission = SpaceMission(
                mission_id="M2024_MARS",
                mission_name="Mars Colony Establishement",
                destination="Mars",
                duration_days=900,
                budget_millions=2500.0,
                crew=[
                    CrewMember(
                        member_id="CM001",
                        name="Sarah Connor",
                        rank=r,
                        age=42,
                        specialization="Mission Command",
                        years_experience=18,
                    ),
                    CrewMember(
                        member_id="CM002",
                        name="John Smith",
                        rank=Rank.LIEUTENANT,
                        age=30,
                        specialization="Navigation",
                        years_experience=2,
                    ),
                    CrewMember(
                        member_id="CM003",
                        name="Alice Johnson",
                        rank=Rank.OFFICER,
                        age=28,
                        specialization="Engineering",
                        years_experience=10,
                    ),
                ],
            )

            print("Mission:", mission.mission_name)
            print("ID:", mission.mission_id)
            print("Duration:", mission.duration_days, "days")
            print("Budget: $", end="")
            print(mission.budget_millions, end="M\n")
            print("Crew size:", len(mission.crew))
            print("Crew members:")
            for member in mission.crew:
                print("-", member.name, end=' (')
                print(member.rank.value, end=')')
                print(" -", member.specialization)

        except ValidationError as e:
            print()
            print("=" * 40)
            print("Excepted validation error:")
            for error in e.errors():
                if error["loc"]:
                    print(error["loc"], ":", error["msg"])

                else:
                    print(error['msg'].removeprefix("Value error, "))


if __name__ == "__main__":
    main()
