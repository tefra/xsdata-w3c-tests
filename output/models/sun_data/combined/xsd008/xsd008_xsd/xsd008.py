from dataclasses import dataclass, field
from typing import List, Optional

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
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class IntType:
    class Meta:
        name = "int"
        namespace = "foo"

    annotation: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class LongType:
    class Meta:
        name = "longType"

    annotation: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "foo",
        }
    )
    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class YesNo:
    class Meta:
        name = "yesNo"
        namespace = "foo"

    annotation: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    value: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
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

    int_value: List[IntType] = field(
        default_factory=list,
        metadata={
            "name": "int",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    long: List[Long] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    yes_no: List[YesNo] = field(
        default_factory=list,
        metadata={
            "name": "yesNo",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    facet: List[Facet] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
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
        }
    )
    restricted: Optional["Root.Restricted"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )

    @dataclass
    class Restricted:
        int_value: List[IntType] = field(
            default_factory=list,
            metadata={
                "name": "int",
                "type": "Element",
                "min_occurs": 1,
            }
        )
        long: List[Long] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
            }
        )
