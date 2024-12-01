from dataclasses import dataclass, field
from typing import Any, ForwardRef, List, Optional, Union

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Base:
    class Meta:
        name = "base"

    foo_or_foo1: List[Union["Base.Foo", "Base.Foo1"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "foo",
                    "type": ForwardRef("Base.Foo"),
                    "namespace": "http://xsdtesting",
                    "max_occurs": 6,
                },
                {
                    "name": "foo1",
                    "type": ForwardRef("Base.Foo1"),
                    "namespace": "http://xsdtesting",
                    "max_occurs": 6,
                },
            ),
            "max_occurs": 6,
        },
    )

    @dataclass
    class Foo:
        value: Optional[bool] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class Foo1:
        value: Optional[bool] = field(
            default=None,
            metadata={
                "required": True,
            },
        )


@dataclass
class Doc(Base):
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    foo1: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
