from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate


@dataclass
class ParentType:
    child: Optional["ParentType.Child"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    grandchild: Optional["ParentType.Grandchild"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )

    @dataclass
    class Child:
        name: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        dob: Optional[XmlDate] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Grandchild:
        name: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        dob: Optional[XmlDate] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class TimerType:
    time: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    iterations: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Data:
    class Meta:
        name = "data"

    timer: list[TimerType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 3,
        },
    )
    parent: list[ParentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 5,
        },
    )
