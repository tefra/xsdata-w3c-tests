from dataclasses import dataclass, field
from typing import List, Optional, Union

__NAMESPACE__ = "http://xstest-tns"


@dataclass
class AnySimpleType:
    class Meta:
        name = "anySimpleType"

    value: Optional[object] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DoubleType:
    class Meta:
        name = "doubleType"

    value: Optional[float] = field(
        default=None
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class FloatType:
    class Meta:
        name = "floatType"

    value: Optional[float] = field(
        default=None
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns"

    elem1: List[Union[AnySimpleType, FloatType, DoubleType]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 5,
        }
    )
