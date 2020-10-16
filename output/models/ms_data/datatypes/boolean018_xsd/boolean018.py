from dataclasses import dataclass, field
from enum import Enum
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
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
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
    :cvar TRUE_VALUE:
    :cvar FALSE_VALUE:
    """
    TRUE_VALUE = "true"
    FALSE_VALUE = "false"


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
        metadata={
            "required": True,
        }
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
        metadata={
            "name": "complexTest",
            "type": "Element",
            "required": True,
        }
    )
    simple_test: Optional[SimplefooType] = field(
        default=None,
        metadata={
            "name": "simpleTest",
            "type": "Element",
            "required": True,
        }
    )
