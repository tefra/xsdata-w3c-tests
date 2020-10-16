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
        metadata={
            "type": "Element",
        }
    )

    @dataclass
    class Elem:
        """
        :ivar att:
        """
        att: int = field(
            init=False,
            default=123,
            metadata={
                "type": "Attribute",
                "namespace": "http://xsdtesting",
            }
        )
