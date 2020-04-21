from decimal import Decimal
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ComplexfooType:
    """
    :ivar comp_foo:
    """
    class Meta:
        name = "complexfooType"

    comp_foo: List[Decimal] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
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

    complex_test: List[ComplexTest] = field(
        default_factory=list,
        metadata=dict(
            name="complexTest",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    simple_test: List[SimpleTest] = field(
        default_factory=list,
        metadata=dict(
            name="simpleTest",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
