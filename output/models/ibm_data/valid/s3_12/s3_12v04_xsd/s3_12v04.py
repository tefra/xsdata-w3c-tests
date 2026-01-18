from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://xstest-tns"


@dataclass(kw_only=True)
class AnySimpleType:
    class Meta:
        name = "anySimpleType"

    value: None | object = field(default=None)
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DoubleType(AnySimpleType):
    class Meta:
        name = "doubleType"

    value: float = field()


@dataclass(kw_only=True)
class FloatType(AnySimpleType):
    class Meta:
        name = "floatType"

    value: float = field()


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns"

    elem1: list[AnySimpleType | FloatType | DoubleType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 5,
        },
    )
