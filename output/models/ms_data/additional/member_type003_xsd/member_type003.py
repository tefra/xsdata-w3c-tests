from dataclasses import dataclass, field
from typing import Union


@dataclass
class Root:
    class Meta:
        name = "root"

    e: list[Union[bool, int, str]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 3,
            "max_occurs": 3,
        },
    )
