from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "AGroupDef/annotation"


@dataclass(kw_only=True)
class A:
    c: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    date: None | XmlDate = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "AGroupDef/annotation"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
