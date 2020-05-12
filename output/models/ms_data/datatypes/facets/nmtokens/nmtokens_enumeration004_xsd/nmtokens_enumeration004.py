from enum import Enum
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
        attr_test: Optional["FooType.Foo.AttrTest"] = field(
            default=None,
            metadata=dict(
                name="attrTest",
                type="Attribute"
            )
        )

        class AttrTest(Enum):
            """
            :cvar FOO:
            :cvar FOO123:
            :cvar FU1:
            :cvar FOO_FU1:
            """
            FOO = "foo"
            FOO123 = "foo123"
            FU1 = "fu1"
            FOO_FU1 = "foo fu1"


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
