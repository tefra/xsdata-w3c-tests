from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooType:
    """
    :ivar foo:
    """
    class Meta:
        name = "fooType"

    foo: Optional["FooType.Foo"] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )

    @dataclass
    class Foo:
        """
        :ivar value:
        :ivar attr_test:
        :ivar id_attr:
        """
        value: Optional[str] = field(
            default=None,
        )
        attr_test: Optional[str] = field(
            default=None,
            metadata=dict(
                name="attrTest",
                type="Attribute",
                min_length=4,
                max_length=6
            )
        )
        id_attr: Optional[str] = field(
            default=None,
            metadata=dict(
                type="Attribute"
            )
        )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
