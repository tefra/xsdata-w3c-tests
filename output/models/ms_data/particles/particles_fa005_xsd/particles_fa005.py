from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Base:
    """
    :ivar target_namespace_foo_element:
    """
    class Meta:
        name = "base"

    target_namespace_foo_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace foo",
            "max_occurs": 3,
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
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"
