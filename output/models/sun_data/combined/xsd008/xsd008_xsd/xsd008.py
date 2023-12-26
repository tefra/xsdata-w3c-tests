from dataclasses import dataclass, field
from typing import List, Optional, Union

__NAMESPACE__ = "foo"


@dataclass
class Facet:
    class Meta:
        name = "facet"
        namespace = "foo"

    annotation: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    value: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class LongType(Facet):
    class Meta:
        name = "longType"

    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class YesNo(Facet):
    class Meta:
        name = "yesNo"
        namespace = "foo"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Int(LongType):
    class Meta:
        name = "int"
        namespace = "foo"

    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Long(LongType):
    class Meta:
        name = "long"
        namespace = "foo"


@dataclass
class Generic:
    class Meta:
        name = "generic"
        namespace = "foo"

    choice: List[Union[Int, Long, YesNo, Facet]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "int",
                    "type": Int,
                },
                {
                    "name": "long",
                    "type": Long,
                },
                {
                    "name": "yesNo",
                    "type": YesNo,
                },
                {
                    "name": "facet",
                    "type": Facet,
                },
            ),
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "foo"

    generic: Optional[Generic] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    restricted: Optional["Root.Restricted"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Restricted:
        int_or_long: List[Union[Int, Long]] = field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "int",
                        "type": Int,
                    },
                    {
                        "name": "long",
                        "type": Long,
                    },
                ),
            },
        )
