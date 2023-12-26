from dataclasses import dataclass, field
from typing import List


@dataclass
class Root:
    class Meta:
        name = "root"

    uid: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    kid: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )


@dataclass
class Uid:
    class Meta:
        name = "uid"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
