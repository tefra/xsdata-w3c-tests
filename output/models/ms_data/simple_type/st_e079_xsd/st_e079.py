from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from xsdata.models.datatype import XmlPeriod


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    value: XmlPeriod | QName | int = field(init=False, default=QName("{a}b"))
