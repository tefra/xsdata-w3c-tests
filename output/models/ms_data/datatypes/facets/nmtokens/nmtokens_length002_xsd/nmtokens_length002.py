from dataclasses import dataclass, field
from typing import List, Optional


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
        attr_test: List[str] = field(
            default_factory=list,
            metadata=dict(
                name="attrTest",
                type="Attribute",
                length=2,
                tokens=True
            )
        )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
