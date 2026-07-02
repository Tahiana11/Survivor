#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, List, Tuple


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: List[Tuple[int, str]] = []
        self._rank: int = 0

    @abstractmethod
    def valide(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("No data available in storage")
        return self._storage.pop(0)


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def valide(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True

        if isinstance(data, list):
            return all(isinstance(i, (int, float)) for i in data)

        return False

    def ingest(self, data: Any) -> None:
        if not self.valide(data):
            raise ValueError("Improper numeric data")

        def add_num_to_storage(val: Any) -> None:
            self._rank += 1
            self._storage.append((self._rank, str(float(val))))

        if isinstance(data, (int, float)):
            add_num_to_storage(data)
        else:
            for j in data:
                add_num_to_storage(j)


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def valide(self, data: Any) -> bool:
        if isinstance(data, str):
            return True

        if isinstance(data, list):
            return all(isinstance(i, str) for i in data)

        return False

    def ingest(self, data: Any) -> None:
        if not self.valide(data):
            raise ValueError("Improper text data")

        def add_text_to_storage(val: Any) -> None:
            self._rank += 1
            self._storage.append((self._rank, str(val)))

        if isinstance(data, str):
            add_text_to_storage(data)

        else:
            for j in data:
                add_text_to_storage(j)


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def is_valide_dict(self, d: Any) -> bool:
        if not isinstance(d, dict):
            return False

        for k, v in d.items():
            if isinstance(k, str) and isinstance(v, str):
                return True

        return False

    def valide(self, data: Any) -> bool:
        if isinstance(data, dict):
            return self.is_valide_dict(data)

        if isinstance(data, list):
            return all(self.is_valide_dict(i) for i in data)

        return False

    def ingest(self, data: Any) -> None:
        if not self.valide(data):
            raise ValueError("Improper numeric data")

        def add_log_to_storage(d: Any) -> None:
            self._rank += 1
            log_str = f"{d.get('log_level', '')}: {d.get('log_message', '')}"
            self._storage.append((self._rank, log_str))

        if isinstance(data, dict):
            add_log_to_storage(data)
        else:
            for log in data:
                add_log_to_storage(log)


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")

    print("Testing Numeric Processor...")
    num = NumericProcessor()
    numeric = [0.2, 10, 'hello']
    for n in numeric:
        res = num.valide(n)
        print(f" Trying to validate input '{n}': {res}")

    f: str = "foo"
    print(f" Test invalid ingestion of string"
          f" '{f}' without prior validation:")
    try:
        num.ingest(f)
    except ValueError as e:
        print(f" Got exception: {e}")
    data_num: list[int] = [x + 1 for x in range(5)]
    print(f" Processing data: {data_num}")
    num.ingest(data_num)
    values: int = 3
    print(f" Extracting {values} values...")
    for i in range(values):
        rank, val = num.output()
        print(f" Numeric value {i}: {int(float(val))}")

    print("\nTesting Text Processor...")
    txt = TextProcessor()
    t: str = "42"
    print(f" Trying to valid input '{t}': {txt.valide(t)}")
    data_txt: list[str] = ["Hello", "Nexus", "World"]
    print(f" Processing data: {data_txt}")
    txt.ingest(data_txt)
    vl: int = 1
    print(f" Extracting {vl} value...")
    for i in range(vl):
        r, v = txt.output()
        print(f" Text value {i}: {v}")

    print("\nTesting Log Processor...")
    log = LogProcessor()
    l: str = "Hello"
    print(f" Trying to valide input '{l}': {log.valide(l)}")
    d: list[dict[str, str]] = [
        {
            'log_level': 'NOTICE',
            'log_message': 'Connection to server'
        },
        {
            'log_level': 'ERROR',
            'log_message': 'Unauthorized access!!'
        }
    ]
    print(f" Processing data: {d}")
    log.ingest(d)
    p: int = 2
    print(f" Extracting {p} values...")
    for i in range(p):
        rank, val = log.output()
        print(f"Log entry {i}: {val}")


if __name__ == "__main__":
    main()
