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
            "required": True,
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
            "required": True,
        }
    )
    element4: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
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
            "required": True,
        }
    )
    element3: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    element2: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    element1: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Root(Derived):
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_S3_4_6"
