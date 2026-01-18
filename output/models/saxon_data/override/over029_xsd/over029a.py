from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://datypic.com/spc"


@dataclass(kw_only=True)
class GiftWrap:
    class Meta:
        name = "giftWrap"
        namespace = "http://datypic.com/spc"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
