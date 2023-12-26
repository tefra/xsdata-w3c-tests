from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://xstest-tns/ibms3_3_6_v02"


@dataclass
class Elem0:
    class Meta:
        name = "elem0"
        namespace = "http://xstest-tns/ibms3_3_6_v02"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Elem1:
    class Meta:
        name = "elem1"
        namespace = "http://xstest-tns/ibms3_3_6_v02"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Elem2:
    class Meta:
        name = "elem2"
        namespace = "http://xstest-tns/ibms3_3_6_v02"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class RootType:
    class Meta:
        name = "rootType"

    elem2_or_elem0: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "elem2",
                    "type": str,
                    "namespace": "http://xstest-tns/ibms3_3_6_v02",
                },
                {
                    "name": "elem0",
                    "type": str,
                    "namespace": "http://xstest-tns/ibms3_3_6_v02",
                },
            ),
            "max_occurs": 2,
        },
    )
    elem1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xstest-tns/ibms3_3_6_v02",
        },
    )


@dataclass
class Root(RootType):
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/ibms3_3_6_v02"
