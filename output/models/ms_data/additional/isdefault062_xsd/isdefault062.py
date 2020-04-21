from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "foo"


@dataclass
class Root:
    """
    :ivar elem:
    """
    class Meta:
        name = "root"
        namespace = "foo"

    elem: Optional["Root.Elem"] = field(
        default=None,
        metadata=dict(
            type="Element",
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
                type="Attribute",
                namespace="foo"
            )
        )
        attr2: str = field(
            init=False,
            default="abc",
            metadata=dict(
                type="Attribute",
                namespace="foo"
            )
        )
        attr3: bool = field(
            init=False,
            default=True,
            metadata=dict(
                type="Attribute",
                namespace="foo"
            )
        )
