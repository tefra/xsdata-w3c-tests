from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


class MySimpleType(Enum):
    """
    :cvar VALUE_1:
    :cvar VALUE_2:
    :cvar VALUE_3:
    """
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


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
        att: MySimpleType = field(
            init=False,
            default=MySimpleType.VALUE_1,
            metadata=dict(
                type="Attribute",
                namespace="http://xsdtesting"
            )
        )
