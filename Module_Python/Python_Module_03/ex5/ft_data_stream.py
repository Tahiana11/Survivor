#!/usr/bin/env python3
from typing import Generator
import random


def gen_event() -> Generator[tuple[str, str], None, None]:
    players: list[str] = [
        "bob",
        "alice",
        "charlie"
    ]

    actions: list[str] = [
       "run",
       "eat",
       "sleep",
       "grab",
       "move",
       "climb",
       "swim",
       "release"
    ]

    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(
        remains: list[tuple[str, str]]) -> Generator[
            tuple[str, str], None, None
        ]:
    while remains:
        index = random.randrange(len(remains))
        event = remains[index]
        remains[:] = remains[:index] + remains[index + 1:]
        yield event


def main() -> None:
    my_gen = gen_event()
    for i in range(1000):
        name, action = next(my_gen)
        print(f"Event {i}: Player {name} did action {action}")

    remains: list[tuple[str, str]] = [next(my_gen) for _ in range(10)]
    print(f"Built list of 10 events: {remains}")

    for e in consume_event(remains):
        print(f"Got event from list: {e}")
        print(f"Remains in list: {remains}")


if __name__ == "__main__":
    main()
