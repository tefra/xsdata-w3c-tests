from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ns-a"


@dataclass(kw_only=True)
class CtA:
    class Meta:
        name = "ct-A"

    a1: int = field(
        metadata={
            "type": "Element",
            "namespace": "ns-a",
            "required": True,
        }
    )
    a2: bool = field(
        metadata={
            "type": "Element",
            "namespace": "ns-a",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class CtB:
    class Meta:
        name = "ct-B"

    b1: bool = field(
        metadata={
            "type": "Element",
            "namespace": "ns-a",
            "required": True,
        }
    )
    b2: int = field(
        metadata={
            "type": "Element",
            "namespace": "ns-a",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class CtC:
    class Meta:
        name = "ct-C"

    c1: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    c2: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass(kw_only=True)
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


@dataclass(kw_only=True)
class AE2(CtB):
    class Meta:
        name = "a-e2"
        namespace = "ns-a"


@dataclass(kw_only=True)
class AE3(CtC):
    class Meta:
        name = "a-e3"
        namespace = "ns-a"


@dataclass(kw_only=True)
class BE1(CtA):
    class Meta:
        name = "b-e1"
        namespace = "ns-a"


@dataclass(kw_only=True)
class BE3(CtC):
    class Meta:
        name = "b-e3"
        namespace = "ns-a"


@dataclass(kw_only=True)
class CE1(CtA):
    class Meta:
        name = "c-e1"
        namespace = "ns-a"


@dataclass(kw_only=True)
class CE2(CtB):
    class Meta:
        name = "c-e2"
        namespace = "ns-a"


@dataclass(kw_only=True)
class E1(CtA):
    class Meta:
        name = "e1"
        namespace = "ns-a"


@dataclass(kw_only=True)
class E2(CtB):
    class Meta:
        name = "e2"
        namespace = "ns-a"


@dataclass(kw_only=True)
class E3(CtC):
    class Meta:
        name = "e3"
        namespace = "ns-a"
