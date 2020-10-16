from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://xsdtesting"


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
class Base:
    """
    :ivar foo:
    :ivar bar:
    """
    class Meta:
        name = "base"

    foo: List[Foo] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
            "max_occurs": 4,
        }
    )
    bar: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
        }
    )


@dataclass
class Doc:
    """
    :ivar foo:
    :ivar bar:
    """
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    foo: List[Foo] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 3,
        }
    )
    bar: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
