from dataclasses import dataclass, field
from typing import Union


@dataclass
class Root:
    class Meta:
        name = "root"

    value: list[Union[bool, int, str]] = field(
        init=False,
        default_factory=lambda: [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
        ],
        metadata={
            "tokens": True,
        },
    )
