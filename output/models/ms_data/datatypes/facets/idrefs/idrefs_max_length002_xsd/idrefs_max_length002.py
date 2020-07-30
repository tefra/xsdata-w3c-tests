from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Foo:
    """
    :ivar idrefs_attr:
    :ivar id1_attr:
    """
    class Meta:
        name = "foo"

    idrefs_attr: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            max_length=1
        )
    )
    id1_attr: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class FooType:
    """
    :ivar foo:
    :ivar id2_attr:
    """
    class Meta:
        name = "fooType"

    foo: Optional[Foo] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
    id2_attr: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
