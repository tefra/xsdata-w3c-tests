from enum import Enum
from dataclasses import dataclass, field
from typing import Optional


class BuildNotation(Enum):
    """
    :cvar G:
    :cvar JPEG:
    :cvar MPEG:
    """
    G = "g"
    JPEG = "jpeg"
    MPEG = "mpeg"


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
        attr_test: Optional["FooType.Foo.AttrTest"] = field(
            default=None,
            metadata=dict(
                name="attrTest",
                type="Attribute"
            )
        )

        class AttrTest(Enum):
            """
            :cvar G:
            :cvar JPEG:
            :cvar MPEG:
            """
            G = "g"
            JPEG = "jpeg"
            MPEG = "mpeg"


@dataclass
class Test(FooType):
    class Meta:
        name = "test"