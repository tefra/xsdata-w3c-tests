from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from xml.etree.ElementTree import QName

from xsdata.models.datatype import XmlPeriod


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    value: XmlPeriod | Decimal | int | QName = field(init=False, default=25)
