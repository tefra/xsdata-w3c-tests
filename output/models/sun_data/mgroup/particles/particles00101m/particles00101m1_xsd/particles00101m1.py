from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "particles"


@dataclass(kw_only=True)
class A:
    class Meta:
        name = "a"
        namespace = "particles"

    date: XmlDate = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
