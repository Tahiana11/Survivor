#!/usr/bin/env python3
from pydantic import ValidationError, BaseModel, Field
from datetime import datetime
from typing import Optional
import json


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=0, le=20)
    power_level: float = Field(ge=0, le=100)
    oxygen_level: float = Field(ge=0, le=100)
    last_maintenance: datetime = Field(default_factory=datetime.now)
    is_operational: bool = Field(default=True)
    notes: Optional[str] = None


def main() -> None:
    print("Space Station Data Validation")

    try:
        print("======================================")
        print("Valid station created:")
        with open("generated_data/space_stations.json", "r") as file:
            data = json.load(file)
        with open("generated_data/invalid_stations.json", "r") as file1:
            data1 = json.load(file1)
        space = SpaceStation(**data[0])
        print("ID: " + space.station_id)
        print("Name: " + space.name)
        print("Crew:", space.crew_size, " people")
        print("Power: ", space.power_level, "%")
        print("Oxygen: ", space.oxygen_level, "%")

        if space.is_operational:
            print("Status: Operational")
        else:
            print("Status: Inoperational")

        print("\n======================================")
        print("Excepted validation error:")
        space1 = SpaceStation(**data1[0])
        print("ID: " + space1.station_id)

    except ValidationError as e:
        print(e.errors()[0]["msg"])

    except FileNotFoundError as e:
        print(
            "Please download and compile data_exporter.py to obtain"
            " the folder containing the files for testing."
        )


if __name__ == "__main__":
    main()
