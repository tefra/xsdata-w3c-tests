from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Ct:
    """
    :ivar a:
    """
    class Meta:
        name = "ct"

    a: Optional["Ct.A"] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )

    @dataclass
    class A:
        """
        :ivar att1:
        :ivar att2:
        """
        att1: str = field(
            default="default",
            metadata=dict(
                type="Attribute"
            )
        )
        att2: str = field(
            init=False,
            default="fixed",
            metadata=dict(
                type="Attribute"
            )
        )


@dataclass
class Root(Ct):
    class Meta:
        name = "root"