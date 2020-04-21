from dataclasses import dataclass, field
from typing import Optional


@dataclass
class TestV2:
    """
    :ivar value:
    :ivar v2:
    """
    class Meta:
        name = "TEST_V2"

    value: Optional[int] = field(
        default=None,
    )
    v2: Optional[bool] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Test:
    """
    :ivar value:
    """
    class Meta:
        name = "test"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
