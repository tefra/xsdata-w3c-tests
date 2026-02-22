from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from xml.etree.ElementTree import QName

from xsdata.models.datatype import XmlPeriod


class RestrictedNotation(Enum):
    JPEG = QName("jpeg")


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    value: XmlPeriod | Decimal | int | RestrictedNotation = field(
        init=False, default=25
    )
