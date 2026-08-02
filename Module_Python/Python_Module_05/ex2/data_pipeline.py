#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, List, Tuple, Protocol


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

    def ingest(self, data: int | float | list[float | int]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        def add_num_to_storage(val: Any) -> None:
            self.count += 1
            self._rank += 1
            stored = str(int(val)) if val == int(val) else str(val)
            self._storage.append((self._rank, stored))

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

    def is_validate_dict(self, d: Any) -> bool:
        if not isinstance(d, dict) or not d:
            return False

        return all(
            isinstance(k, str) and isinstance(v, str) for k, v in d.items()
        )

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return self.is_validate_dict(data)

        if isinstance(data, list):
            return all(self.is_validate_dict(i) for i in data)

        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        logs: list[dict[str, str]] = [data] if isinstance(data, dict) else data

        for log in logs:
            self._rank += 1
            self.count += 1
            log_str = ": ".join(str(value) for value in log.values())
            self._storage.append((self._rank, log_str))

    def print_stats(self) -> None:
        print(
            f"Log Processor: total {self.count} items processed,"
            f" remaining {len(self._storage)} on processor"
        )


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [value for _, value in data]
        print("CSV Output:")
        print(",".join(values))


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        items = []
        for index, value in data:
            safe = value.replace("\\", "\\\\").replace('"', '\\"')
            items.append(f'"item_{index}": "{safe}"')

        res = "{" + ", ".join(items) + "}"
        print("JSON Output:")
        print(res)


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        res: list[tuple[int, str]] = []
        for p in self._processor:
            for _ in range(nb):
                res.append(p.output())
            plugin.process_output(res)


def main() -> None:
    print("Initialize Data Stream...\n")

    pro = DataStream()
    pro.print_processors_stats()

    print("Registering Processors")
    print()
    stream: List[Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {"log_level": "INFO", "log_message": "User wil isconnected"},
        ],
        42,
        ["Hi", "five"],
    ]
    print(f"Send first batch of data on stream: {stream}")
    print()
    num = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    pro.register_processor(num)
    pro.register_processor(text)
    pro.register_processor(log)
    pro.process_stream(stream)
    pro.print_processors_stats()

    nb: int = 3
    print(f"\nSend {nb} processed data from each processor to a CSV plugin:")
    pro.output_pipeline(nb, CSVExportPlugin())

    print()
    pro.print_processors_stats()

    batch: List[Any] = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {
                "log_level": "ERROR", "log_message": "500 server crash"
            },
            {
                "log_level":
                "NOTICE",
                "log_message":
                "Certificate expires in 10 days"
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]
    pro.print_processors_stats()
    print(f"\nSend another batch of data: {batch}")
    pro.process_stream(batch)

    print()
    pro.print_processors_stats()

    nb = 5
    print(f"Send {nb} processed data from each processor to a JSON plugin:")
    pro.output_pipeline(nb, JSONExportPlugin())

    print()
    pro.print_processors_stats()


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===\n")
    try:
        main()
    except Exception as e:
        print("Got error:", e)
