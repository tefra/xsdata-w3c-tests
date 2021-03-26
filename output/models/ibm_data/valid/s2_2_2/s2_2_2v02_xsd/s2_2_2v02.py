from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://xstest-tns/ibms3_3_6_v02"


@dataclass
class Elem0:
    class Meta:
        name = "elem0"
        namespace = "http://xstest-tns/ibms3_3_6_v02"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Elem1:
    class Meta:
        name = "elem1"
        namespace = "http://xstest-tns/ibms3_3_6_v02"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Elem2:
    class Meta:
        name = "elem2"
        namespace = "http://xstest-tns/ibms3_3_6_v02"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class RootType:
    class Meta:
        name = "rootType"

    elem2_or_elem0_or_elem1: List[object] = field(
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
                {
                    "name": "elem1",
                    "type": str,
                    "namespace": "http://xstest-tns/ibms3_3_6_v02",
                },
            ),
            "min_occurs": 3,
            "max_occurs": 4,
        }
    )


@dataclass
class Root(RootType):
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/ibms3_3_6_v02"
