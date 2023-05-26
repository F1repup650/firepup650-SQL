from typing import Any

def alias(Function): ...

__VERSION__: str
__NEW__: str
__LICENSE__: str

class sql:
    def addTable(self, tableName: str, mode: int = ..., address: str = ...) -> None: ...
    def __init__(self, filename: str) -> None: ...
    def setTable(self, tableName: str) -> None: ...
    def get(self, name: str) -> Any: ...
    def set(self, name: str, value: object) -> int: ...
    def delete(self, name: str) -> None: ...
    def deleteAll(self) -> None: ...
    def close(self) -> None: ...
