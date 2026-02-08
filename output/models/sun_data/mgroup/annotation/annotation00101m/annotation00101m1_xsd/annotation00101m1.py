from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "MGroup/annotation"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "MGroup/annotation"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class TheType:
    class Meta:
        name = "theType"

    c: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    date: XmlDate = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
