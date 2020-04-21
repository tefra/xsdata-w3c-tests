from decimal import Decimal
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ComplexfooType:
    """
    :ivar comp_foo:
    """
    class Meta:
        name = "complexfooType"

    comp_foo: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class SimpleTest:
    """
    :ivar value:
    """
    class Meta:
        name = "simpleTest"

    value: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            required=True
        )
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
