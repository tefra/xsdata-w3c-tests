from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Test:
    """
    :ivar global_att:
    """
    class Meta:
        name = "test"

    global_att: Optional[int] = field(
        default=None,
        metadata=dict(
            name="globalAtt",
            type="Attribute"
        )
    )
