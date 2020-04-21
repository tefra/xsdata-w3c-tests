from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Optional


@dataclass
class MyType:
    """
    :ivar att:
    """
    class Meta:
        name = "myType"

    att: Optional[QName] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Root(MyType):
    class Meta:
        name = "root"
