from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Base:
    """
    :ivar g1:
    :ivar g2:
    """
    class Meta:
        name = "base"

    g1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
        }
    )
    g2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
        }
    )


@dataclass
class Foo:
    """
    :ivar any_element:
    """
    class Meta:
        name = "foo"
        namespace = "http://xsdtesting"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class Doc(Base):
    """
    :ivar s1:
    :ivar s2:
    """
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    s1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    s2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
