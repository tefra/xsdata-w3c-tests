from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlTime

__NAMESPACE__ = "compositor"


@dataclass(kw_only=True)
class A:
    class Meta:
        name = "a"
        namespace = "compositor"

    date: XmlDate = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    time: XmlTime = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
