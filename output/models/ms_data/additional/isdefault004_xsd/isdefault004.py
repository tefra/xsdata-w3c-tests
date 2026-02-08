from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    str_value: str = field(
        default="abc",
        metadata={
            "name": "str",
            "type": "Element",
            "namespace": "",
        },
    )
    number: int = field(
        default=123,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    bool_value: bool = field(
        default=True,
        metadata={
            "name": "bool",
            "type": "Element",
            "namespace": "",
        },
    )
