from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ns-a"


@dataclass
class CtA:
    class Meta:
        name = "ct-A"

    a1: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "ns-a",
            "required": True,
        },
    )
    a2: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "ns-a",
            "required": True,
        },
    )


@dataclass
class CtB:
    class Meta:
        name = "ct-B"

    b1: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "ns-a",
            "required": True,
        },
    )
    b2: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "ns-a",
            "required": True,
        },
    )


@dataclass
class CtC:
    class Meta:
        name = "ct-C"

    c1: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    c2: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ns-a"

    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AE2(CtB):
    class Meta:
        name = "a-e2"
        namespace = "ns-a"


@dataclass
class AE3(CtC):
    class Meta:
        name = "a-e3"
        namespace = "ns-a"


@dataclass
class BE1(CtA):
    class Meta:
        name = "b-e1"
        namespace = "ns-a"


@dataclass
class BE3(CtC):
    class Meta:
        name = "b-e3"
        namespace = "ns-a"


@dataclass
class CE1(CtA):
    class Meta:
        name = "c-e1"
        namespace = "ns-a"


@dataclass
class CE2(CtB):
    class Meta:
        name = "c-e2"
        namespace = "ns-a"


@dataclass
class E1(CtA):
    class Meta:
        name = "e1"
        namespace = "ns-a"


@dataclass
class E2(CtB):
    class Meta:
        name = "e2"
        namespace = "ns-a"


@dataclass
class E3(CtC):
    class Meta:
        name = "e3"
        namespace = "ns-a"
