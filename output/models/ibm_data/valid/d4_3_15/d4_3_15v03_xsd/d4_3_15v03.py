from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ParentType:
    child: Optional["ParentType.Child"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    grandchild: Optional["ParentType.Grandchild"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class Child:
        name: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )
        dob: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )

    @dataclass
    class Grandchild:
        name: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )
        dob: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )


@dataclass
class TimerType:
    time_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "time",
            "type": "Attribute",
        }
    )
    iterations: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Data:
    class Meta:
        name = "data"

    timer: List[TimerType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 3,
        }
    )
    parent: List[ParentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 5,
        }
    )
