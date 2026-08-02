#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, List, Tuple


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: List[Tuple[int, str]] = []
        self._rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    @abstractmethod
    def print_stats(self) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            return (-1, "No data")
        return self._storage.pop(0)


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        self.count: int = 0
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, bool):
            return False

        if isinstance(data, (int, float)):
            return True

        if isinstance(data, list):
            return all(isinstance(i, (int, float)) for i in data)

        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        def add_num_to_storage(val: Any) -> None:
            self.count += 1
            self._rank += 1
            self._storage.append((self._rank, str(val)))

        if isinstance(data, (int, float)):
            add_num_to_storage(data)
        else:
            for j in data:
                add_num_to_storage(j)

    def print_stats(self) -> None:
        print(
            f"Numeric Processor: total {self.count} items processed,"
            f" remaining {len(self._storage)} on processor"
        )


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        self.count: int = 0
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True

        if isinstance(data, list):
            return all(isinstance(i, str) for i in data)

        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        def add_text_to_storage(val: Any) -> None:
            self.count += 1
            self._rank += 1
            self._storage.append((self._rank, str(val)))

        if isinstance(data, str):
            add_text_to_storage(data)

        else:
            for j in data:
                add_text_to_storage(j)

    def print_stats(self) -> None:
        print(
            f"Text Processor: total {self.count} items processed,"
            f" remaining {len(self._storage)} on processor"
        )


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        self.count: int = 0
        super().__init__()

    def is_valid_dict(self, d: Any) -> bool:
        if not isinstance(d, dict):
            return False

        for k, v in d.items():
            if isinstance(k, str) and isinstance(v, str):
                return True

        return False

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return self.is_valid_dict(data)

        if isinstance(data, list):
            return all(self.is_valid_dict(i) for i in data)

        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        logs: list[dict[str, str]] = [data] if isinstance(data, dict) else data

        for log in logs:
            self.count += 1
            self._rank += 1
            log_str = ": ".join(str(value) for value in log.values())
            self._storage.append((self._rank, log_str))

    def print_stats(self) -> None:
        print(
            f"Log Processor: total {self.count} items processed,"
            f" remaining {len(self._storage)} on processor")


class DataStream:
    def __init__(self) -> None:
        self._processor: List[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processor.append(proc)

    def process_stream(self, stream: List[Any]) -> None:
        for i in stream:
            processed = False
            for proc in self._processor:
                if proc.validate(i):
                    proc.ingest(i)
                    processed = True

            if not processed:
                print(
                    f"DataStream error - Can't process element in stream: {i}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")

        if not self._processor:
            print("No processor found, no data\n")
            return

        for pro in self._processor:
            pro.print_stats()


def main() -> None:
    pro = DataStream()
    print("Initialize Data Stream...")

    stream: List[Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected",
            },
        ],
        42,
        ["Hi", "five"],
    ]
    pro.print_processors_stats()
    print("Registering Numeric Processor\n")
    numeric_proc = NumericProcessor()
    pro.register_processor(numeric_proc)
    print(f"Send first batch of data on stream: {stream}")
    pro.process_stream(stream)
    pro.print_processors_stats()
    print()

    print("Registering other data processors")
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    pro.register_processor(text_proc)
    pro.register_processor(log_proc)
    print("Send the same batch again")
    pro.process_stream(stream)
    pro.print_processors_stats()
    print()
    print(
        "Consume some elements from the data processors: Numeric 3,"
        " Text 2, Log 1"
    )
    for _ in range(3):
        numeric_proc.output()

    for _ in range(2):
        text_proc.output()

    log_proc.output()
    pro.print_processors_stats()


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===\n")
    try:
        main()
    except Exception as e:
        print("Got error:", e)
