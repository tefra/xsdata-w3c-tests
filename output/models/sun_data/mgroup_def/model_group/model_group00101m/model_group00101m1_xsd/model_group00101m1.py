from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "modelGroup"


@dataclass(kw_only=True)
class A1:
    class Meta:
        name = "A"

    c: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    date: XmlDate = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class A(A1):
    class Meta:
        name = "a"
        namespace = "modelGroup"
