from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate


@dataclass(kw_only=True)
class RootType:
    class Meta:
        name = "rootType"

    ele: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    date: None | XmlDate = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Root(RootType):
    class Meta:
        name = "root"
