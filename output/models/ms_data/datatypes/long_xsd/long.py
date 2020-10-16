from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ComplexfooType:
    """
    :ivar comp_foo:
    """
    class Meta:
        name = "complexfooType"

    comp_foo: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class SimpleTest:
    """
    :ivar value:
    """
    class Meta:
        name = "simpleTest"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ComplexTest(ComplexfooType):
    class Meta:
        name = "complexTest"


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
    simple_test: Optional[int] = field(
        default=None,
        metadata={
            "name": "simpleTest",
            "type": "Element",
            "required": True,
        }
    )
