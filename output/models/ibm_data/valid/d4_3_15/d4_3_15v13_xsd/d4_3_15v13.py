from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate


@dataclass(kw_only=True)
class RootType:
    class Meta:
        name = "rootType"

    date_ele: XmlDate = field(
        metadata={
            "name": "dateEle",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass(kw_only=True)
class Root(RootType):
    class Meta:
        name = "root"
