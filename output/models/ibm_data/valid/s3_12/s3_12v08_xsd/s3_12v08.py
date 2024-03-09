from dataclasses import dataclass, field
from typing import Any, List, Optional, Union

__NAMESPACE__ = "tns"


@dataclass
class ChildType:
    class Meta:
        name = "childType"

    type1: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    type2: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class DerivedType1(ChildType):
    class Meta:
        name = "derivedType1"

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[bool] = field(default=None)


@dataclass
class DerivedType2(ChildType):
    class Meta:
        name = "derivedType2"

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[int] = field(default=None)


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "tns"

    child: List[Union[ChildType, DerivedType1, DerivedType2]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
