from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum


class AttRefAtt1(StrEnum):
    AK = "AK"
    AL = "AL"
    AR = "AR"


@dataclass(kw_only=True)
class AttRef:
    class Meta:
        name = "attRef"

    att1: None | AttRefAtt1 = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    att2: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    elem: None | AttRef = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
