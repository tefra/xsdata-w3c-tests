from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDateTime


class DocValue(Enum):
    VALUE_0000_09_20_T00_00_00_Z = XmlDateTime(0, 9, 20, 0, 0, 0, 0, 0)
    VALUE_0000_09_20_T12_00_00_Z = XmlDateTime(0, 9, 20, 12, 0, 0, 0, 0)


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    value: DocValue = field(
        metadata={
            "explicit_timezone": "required",
        }
    )
