from dataclasses import dataclass, field
from typing import Union

__NAMESPACE__ = "foo"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "foo"

    e: list[Union[bool, int, str]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 3,
            "max_occurs": 3,
        },
    )
