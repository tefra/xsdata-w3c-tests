from dataclasses import dataclass, field
from typing import List, Union


@dataclass
class Root:
    class Meta:
        name = "root"

    e: List[Union[bool, int, str]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 3,
            "max_occurs": 3,
        }
    )
