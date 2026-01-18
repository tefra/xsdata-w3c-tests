from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    value: XmlPeriod | str = field(init=False, default="ENU ")
