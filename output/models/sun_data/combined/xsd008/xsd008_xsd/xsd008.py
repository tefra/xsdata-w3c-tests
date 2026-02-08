from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "foo"


@dataclass(kw_only=True)
class Facet:
    class Meta:
        name = "facet"
        namespace = "foo"

    annotation: None | object = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    value: object = field(
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class LongType(Facet):
    class Meta:
        name = "longType"

    value: int = field(
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class YesNo(Facet):
    class Meta:
        name = "yesNo"
        namespace = "foo"

    value: bool = field(
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class Int(LongType):
    class Meta:
        name = "int"
        namespace = "foo"


@dataclass(kw_only=True)
class Long(LongType):
    class Meta:
        name = "long"
        namespace = "foo"


@dataclass(kw_only=True)
class Generic:
    class Meta:
        name = "generic"
        namespace = "foo"

    choice: list[Int | Long | YesNo | Facet] = field(
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


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "foo"

    generic: None | Generic = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    restricted: None | Root.Restricted = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass(kw_only=True)
    class Restricted:
        int_or_long: list[Int | Long] = field(
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
