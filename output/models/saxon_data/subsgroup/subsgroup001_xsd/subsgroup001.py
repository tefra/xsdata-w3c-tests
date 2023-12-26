from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Back:
    class Meta:
        name = "back"

    para: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Body:
    class Meta:
        name = "body"

    para: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Para:
    class Meta:
        name = "para"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"

    body: Optional[Body] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    back: Optional[Back] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
