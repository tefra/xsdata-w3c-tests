from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xstest-tns/ibms3_3_6_v01"


@dataclass
class Elem1:
    class Meta:
        name = "elem1"
        namespace = "http://xstest-tns/ibms3_3_6_v01"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Elem2:
    class Meta:
        name = "elem2"
        namespace = "http://xstest-tns/ibms3_3_6_v01"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class RootType:
    class Meta:
        name = "rootType"

    elem2_or_elem1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "elem2",
                    "type": str,
                    "namespace": "http://xstest-tns/ibms3_3_6_v01",
                },
                {
                    "name": "elem1",
                    "type": str,
                    "namespace": "http://xstest-tns/ibms3_3_6_v01",
                },
            ),
        }
    )


@dataclass
class Root(RootType):
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/ibms3_3_6_v01"
