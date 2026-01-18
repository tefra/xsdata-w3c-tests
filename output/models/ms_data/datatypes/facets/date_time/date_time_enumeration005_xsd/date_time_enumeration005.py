from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDateTime


class Dttype(Enum):
    VALUE_2002_01_01_T12_01_01_00_00 = XmlDateTime(2002, 1, 1, 12, 1, 1, 0, 0)


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    value: Dttype = field(
        metadata={
            "required": True,
        }
    )
