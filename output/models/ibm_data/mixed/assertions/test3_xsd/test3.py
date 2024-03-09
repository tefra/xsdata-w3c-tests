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

    timer: Optional[TimerType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    parent: Optional[ParentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
