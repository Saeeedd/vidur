import json
from abc import ABC, abstractmethod
from typing import List

from vidur.config import Config
from vidur.entities import Request


class BaseRequestGenerator(ABC):
    def __init__(self, config: Config):
        self._config = config
        self._should_write_json_trace = config.write_json_trace

    def _write_requests_to_file(self, requests: List[Request]) -> None:
        request_dicts = [request.to_dict() for request in requests]
        request_file = f"{self._config.output_dir}/requests.json"
        with open(request_file, "w") as f:
            json.dump(request_dicts, f)

    @abstractmethod
    def generate_requests(self) -> List[Request]:
        pass

    def generate(self) -> List[Request]:
        requests = self.generate_requests()

        if self._should_write_json_trace:
            self._write_requests_to_file(requests)

        return requests
