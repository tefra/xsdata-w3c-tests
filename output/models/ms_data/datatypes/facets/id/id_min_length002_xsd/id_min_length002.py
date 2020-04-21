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
        """
        value: Optional[str] = field(
            default=None,
        )
        attr_test: Optional[str] = field(
            default=None,
            metadata=dict(
                name="attrTest",
                type="Attribute",
                min_length=5.0
            )
        )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
