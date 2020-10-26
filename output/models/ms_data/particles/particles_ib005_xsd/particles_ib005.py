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
    :ivar foo_or_bar:
    """
    class Meta:
        name = "base"

    foo_or_bar: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "foo",
                    "type": Foo,
                    "namespace": "http://xsdtesting",
                },
                {
                    "name": "bar",
                    "type": object,
                    "namespace": "http://xsdtesting",
                },
            ),
            "max_occurs": 4,
        }
    )


@dataclass
class Doc(Base):
    """
    :ivar foo_or_bar:
    """
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    foo_or_bar: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "foo",
                    "type": Foo,
                },
                {
                    "name": "bar",
                    "type": object,
                },
            ),
            "max_occurs": 3,
        }
    )
