from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://datypic.com/spc"


@dataclass
class GiftWrap:
    """
    :ivar value:
    """
    class Meta:
        name = "giftWrap"
        namespace = "http://datypic.com/spc"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
