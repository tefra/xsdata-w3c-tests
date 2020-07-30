from enum import Enum
from dataclasses import dataclass, field
from typing import Optional


class BuildNotation(Enum):
    """
    :cvar JPEG:
    :cvar MPEG:
    :cvar G:
    """
    JPEG = "jpeg"
    MPEG = "mpeg"
    G = "g"


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
        attr_test: Optional[BuildNotation] = field(
            default=None,
            metadata=dict(
                name="attrTest",
                type="Attribute",
                max_length=3
            )
        )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
