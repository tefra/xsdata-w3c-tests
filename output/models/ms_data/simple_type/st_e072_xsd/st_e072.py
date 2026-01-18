from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    value: XmlPeriod | str | int = field(init=False, default="a")


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    root: Root = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
