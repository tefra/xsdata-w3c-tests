from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "pSubstitutions"


@dataclass(kw_only=True)
class A:
    c: list[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 3,
        },
    )


@dataclass(kw_only=True)
class B(A):
    d: XmlDate = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass(kw_only=True)
class C(A):
    pass


@dataclass(kw_only=True)
class E(A):
    class Meta:
        name = "e"
        namespace = "pSubstitutions"
