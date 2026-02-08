from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://xstest-tns/schema11_S3_4_6"


@dataclass(kw_only=True)
class CmplxBase:
    class Meta:
        name = "cmplxBase"

    element1: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    element2: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    element3: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    element4: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass(kw_only=True)
class Derived:
    class Meta:
        name = "derived"

    element4: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    element3: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    element2: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    element1: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass(kw_only=True)
class Root(Derived):
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_S3_4_6"
