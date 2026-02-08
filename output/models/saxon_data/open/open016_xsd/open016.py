from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    value: XmlDate = field()
    evidence: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    open_com_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "http://open.com/",
        },
    )
