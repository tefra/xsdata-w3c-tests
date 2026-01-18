from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate


@dataclass(kw_only=True)
class ParentType:
    child: None | ParentType.Child = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    grandchild: None | ParentType.Grandchild = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )

    @dataclass(kw_only=True)
    class Child:
        name: None | str = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        dob: None | XmlDate = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass(kw_only=True)
    class Grandchild:
        name: None | str = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        dob: None | XmlDate = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass(kw_only=True)
class TimerType:
    time: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    iterations: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
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
