from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Root:
    class Meta:
        name = "root"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
    idref_attr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Wrapper:
    class Meta:
        name = "wrapper"

    root: Optional[Root] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
