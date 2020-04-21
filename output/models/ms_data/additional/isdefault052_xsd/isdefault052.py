from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Root:
    """
    :ivar elem:
    """
    class Meta:
        name = "root"

    elem: Optional["Root.Elem"] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )

    @dataclass
    class Elem:
        """
        :ivar attr1:
        :ivar attr2:
        :ivar attr3:
        """
        attr1: int = field(
            init=False,
            default=123,
            metadata=dict(
                type="Attribute"
            )
        )
        attr2: str = field(
            init=False,
            default="abc",
            metadata=dict(
                type="Attribute"
            )
        )
        attr3: bool = field(
            init=False,
            default=True,
            metadata=dict(
                type="Attribute"
            )
        )
