from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    """
    :ivar e:
    :ivar f:
    """
    e: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://xsdtesting"
        )
    )
    f: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://xsdtesting"
        )
    )


@dataclass
class Base:
    """
    :ivar e:
    :ivar f:
    """
    class Meta:
        name = "base"

    e: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://xsdtesting"
        )
    )
    f: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://xsdtesting"
        )
    )


@dataclass
class Doc(Base):
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"



@dataclass
class Test(B):
    class Meta:
        name = "test"
