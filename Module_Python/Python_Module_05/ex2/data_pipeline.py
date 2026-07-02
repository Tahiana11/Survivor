#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, List, Tuple, Protocol


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

    @abstractmethod
    def print_stats(self) -> None:
        pass

    def output(self, nb: int) -> list[tuple[int, str]]:
        res: list[tuple[int, str]] = []
        for _ in range(nb):
            if not self._storage:
                break

            res.append(self._storage.pop(0))
        return res


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        self.count: int = 0
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
            self.count += 1
            self._rank += 1
            f = float(val)
            stored = str(int(f)) if f == int(f) else str(f)
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

    def is_valide_dict(self, d: Any) -> bool:
        if not isinstance(d, dict) or not d:
            return False

        return all(
            isinstance(k, str) and isinstance(v, str) for k, v in d.items()
        )

    def valide(self, data: Any) -> bool:
        if isinstance(data, dict):
            return self.is_valide_dict(data)

        if isinstance(data, list):
            return all(self.is_valide_dict(i) for i in data)

        return False

    def ingest(self, data: Any) -> None:
        if not self.valide(data):
            raise ValueError("Improper log data")

        def add_log_to_storage(d: Any) -> None:
            self.count += 1
            self._rank += 1
            log_str = f"{d.get('log_level', '')}: {d.get('log_message', '')}"
            self._storage.append((self._rank, log_str))

        if isinstance(data, dict):
            add_log_to_storage(data)
        else:
            for log in data:
                add_log_to_storage(log)

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
                if proc.valide(i):
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
        for p in self._processor:
            data = p.output(nb)
            if data:
                plugin.process_output(data)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===\n")
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
    main()
