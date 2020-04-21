from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Test:
    """
    :ivar complex_att:
    :ivar global_att:
    :ivar item1:
    :ivar item2:
    """
    class Meta:
        name = "test"

    complex_att: Optional[str] = field(
        default=None,
        metadata=dict(
            name="complexAtt",
            type="Attribute"
        )
    )
    global_att: Optional[int] = field(
        default=None,
        metadata=dict(
            name="globalAtt",
            type="Attribute"
        )
    )
    item1: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    item2: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
