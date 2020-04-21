from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Doc:
    """
    :ivar elem:
    """
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: Optional["Doc.Elem"] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )

    @dataclass
    class Elem:
        """
        :ivar att:
        """
        att: str = field(
            init=False,
            default="A B",
            metadata=dict(
                type="Attribute",
                namespace="http://xsdtesting"
            )
        )
