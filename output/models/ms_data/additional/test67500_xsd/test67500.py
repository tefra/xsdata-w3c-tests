from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName


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
