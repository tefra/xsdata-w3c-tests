from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://xstest-tns/ibms3_3_6_v04"


@dataclass
class Elem0:
    class Meta:
        name = "elem0"
        namespace = "http://xstest-tns/ibms3_3_6_v04"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Elem1:
    class Meta:
        name = "elem1"
        namespace = "http://xstest-tns/ibms3_3_6_v04"

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
        namespace = "http://xstest-tns/ibms3_3_6_v04"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Elem3:
    class Meta:
        name = "elem3"
        namespace = "http://xstest-tns/ibms3_3_6_v04"

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

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "elem3",
                    "type": str,
                    "namespace": "http://xstest-tns/ibms3_3_6_v04",
                },
                {
                    "name": "elem2",
                    "type": str,
                    "namespace": "http://xstest-tns/ibms3_3_6_v04",
                },
                {
                    "name": "elem0",
                    "type": str,
                    "namespace": "http://xstest-tns/ibms3_3_6_v04",
                },
                {
                    "name": "elem1",
                    "type": str,
                    "namespace": "http://xstest-tns/ibms3_3_6_v04",
                },
            ),
            "max_occurs": 6,
        }
    )


@dataclass
class Root(RootType):
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/ibms3_3_6_v04"
