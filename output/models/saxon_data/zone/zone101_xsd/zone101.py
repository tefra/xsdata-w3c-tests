from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    value: XmlDateTime = field()
