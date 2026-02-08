from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://xstest-tns/ibms3_3_6_v02"


@dataclass(kw_only=True)
class Elem0:
    class Meta:
        name = "elem0"
        namespace = "http://xstest-tns/ibms3_3_6_v02"

    value: str = field(default="")


@dataclass(kw_only=True)
class Elem1:
    class Meta:
        name = "elem1"
        namespace = "http://xstest-tns/ibms3_3_6_v02"

    value: str = field(default="")


@dataclass(kw_only=True)
class Elem2:
    class Meta:
        name = "elem2"
        namespace = "http://xstest-tns/ibms3_3_6_v02"

    value: str = field(default="")


@dataclass(kw_only=True)
class RootType:
    class Meta:
        name = "rootType"

    elem2_or_elem0: list[Elem2 | Elem0] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "elem2",
                    "type": Elem2,
                    "namespace": "http://xstest-tns/ibms3_3_6_v02",
                    "max_occurs": 2,
                },
                {
                    "name": "elem0",
                    "type": Elem0,
                    "namespace": "http://xstest-tns/ibms3_3_6_v02",
                },
            ),
            "max_occurs": 2,
        },
    )
    elem1: None | Elem1 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xstest-tns/ibms3_3_6_v02",
        },
    )


@dataclass(kw_only=True)
class Root(RootType):
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/ibms3_3_6_v02"
