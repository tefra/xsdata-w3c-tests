from dataclasses import dataclass, field
from typing import Optional


@dataclass
class One:
    elem1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    elem2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    att1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    att2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Two(One):
    pass


@dataclass
class Three(Two):
    pass


@dataclass
class Doc:
    class Meta:
        name = "doc"

    e1: Optional[One] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    e2: Optional[Two] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    e3: Optional[Three] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
