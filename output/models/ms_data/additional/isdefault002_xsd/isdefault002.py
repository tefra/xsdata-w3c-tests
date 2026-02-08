from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    str_value: str = field(
        init=False,
        default="abc",
        metadata={
            "name": "str",
            "type": "Element",
            "namespace": "",
        },
    )
    number: int = field(
        init=False,
        default=123,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    bool_value: bool = field(
        init=False,
        default=True,
        metadata={
            "name": "bool",
            "type": "Element",
            "namespace": "",
        },
    )
