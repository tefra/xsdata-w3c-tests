from dataclasses import dataclass, field
from typing import List, Optional, Union


@dataclass
class Ct:
    class Meta:
        name = "ct"

    value: Optional[str] = field(
        default=None
    )
    att: Optional[Union[bool, int, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    e: List[Ct] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 3,
        }
    )
