from dataclasses import dataclass, field
from typing import Optional, Union

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Foo:
    class Meta:
        name = "foo"
        namespace = "http://xsdtesting"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Base:
    class Meta:
        name = "base"

    foo_or_bar: list[Union[Foo, object]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "foo",
                    "type": Foo,
                    "namespace": "http://xsdtesting",
                    "max_occurs": 4,
                },
                {
                    "name": "bar",
                    "type": object,
                    "namespace": "http://xsdtesting",
                },
            ),
            "max_occurs": 4,
        },
    )


@dataclass
class Doc(Base):
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"
