from dataclasses import dataclass, field
from typing import List, Union


@dataclass
class Root:
    class Meta:
        name = "root"

    value: List[Union[bool, int, str]] = field(
        init=False,
        default_factory=lambda: ["a", "b", "c", "d", "e", "f"],
        metadata={
            "tokens": True,
        }
    )
