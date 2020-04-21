from enum import Enum
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ComplexfooType:
    """
    :ivar comp_foo:
    """
    class Meta:
        name = "complexfooType"

    comp_foo: Optional["ComplexfooType.CompFoo"] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )

    class CompFoo(Enum):
        """
        :cvar VALUE_0:
        :cvar VALUE_1:
        """
        VALUE_0 = "0"
        VALUE_1 = "1"


class SimplefooType(Enum):
    """
    :cvar FALSE_VALUE:
    :cvar TRUE_VALUE:
    """
    FALSE_VALUE = "false"
    TRUE_VALUE = "true"


@dataclass
class ComplexTest(ComplexfooType):
    class Meta:
        name = "complexTest"


@dataclass
class SimpleTest:
    """
    :ivar value:
    """
    class Meta:
        name = "simpleTest"

    value: Optional[SimplefooType] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Root:
    """
    :ivar complex_test:
    :ivar simple_test:
    """
    class Meta:
        name = "root"

    complex_test: Optional[ComplexTest] = field(
        default=None,
        metadata=dict(
            name="complexTest",
            type="Element",
            required=True
        )
    )
    simple_test: Optional[SimpleTest] = field(
        default=None,
        metadata=dict(
            name="simpleTest",
            type="Element",
            required=True
        )
    )
