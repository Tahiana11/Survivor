#!/usr/bin/env python3
from pydantic import ValidationError, BaseModel, Field, model_validator
from typing import Optional
from datetime import datetime
from enum import Enum
import json


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field(default_factory=datetime.now)
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def verify_alien_contact(self) -> 'AlienContact':
        if not self.contact_id.startswith('AC'):
            raise ValueError("The contact ID must begin with 'AC'")

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified.")

        if self.contact_type == ContactType.TELEPATHIC \
                and self.witness_count < 3:
            raise ValueError("Telepathic contact requires at"
                             " least 3 witnesses")

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) "
                             "must include a received message.")

        return self


def main() -> None:
    print("Alien Contact Log Validation")
    try:
        print("======================================")
        print("Valid contact report:")
        with open("generated_data/alien_contacts.json", "r") as file:
            data = json.load(file)
        with open("generated_data/invalid_contacts.json", "r") as file1:
            data1 = json.load(file1)
        alien = AlienContact(**data[0])

        print("ID:", alien.contact_id)
        print("Type:", alien.contact_type.value)
        print("Location:", alien.location)
        print("Signal:", alien.signal_strength, end="")
        print("/10")
        print("Duration:", alien.duration_minutes, "minutes")
        print("Witness:", alien.witness_count)
        print("Messsage:", alien.message_received)

        alien = AlienContact(**data1[1])
        print("Type:", alien.contact_type.value)

    except ValidationError as e:
        print()
        print("======================================")
        print("Excepted validation error: ")
        print(e.errors()[0]["msg"].removeprefix("Value error, "))

    except FileNotFoundError:
        print(
            "Please download and compile data_exporter.py to obtain"
            " the folder containing the files for testing."
        )


if __name__ == "__main__":
    main()
