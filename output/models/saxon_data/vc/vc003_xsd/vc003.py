from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate


@dataclass(kw_only=True)
class Temp:
    class Meta:
        name = "temp"

    value: XmlDate = field()
