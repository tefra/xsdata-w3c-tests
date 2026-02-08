from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlTime


@dataclass(kw_only=True)
class E:
    class Meta:
        name = "e"

    value: XmlDate = field()


@dataclass(kw_only=True)
class Zing:
    class Meta:
        name = "zing"

    e: XmlDate | XmlTime = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    f: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    local_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##local",
        },
    )


@dataclass(kw_only=True)
class Doc(Zing):
    class Meta:
        name = "doc"
