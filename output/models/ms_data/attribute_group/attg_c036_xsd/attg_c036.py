from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Test:
    """
    :ivar att3:
    :ivar att4:
    :ivar att5:
    """
    class Meta:
        name = "test"

    att3: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    att4: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    att5: Optional[bool] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Doc(Test):
    class Meta:
        name = "doc"
