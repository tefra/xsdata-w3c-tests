from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ComplexfooType:
    """
    :ivar comp_foo:
    """
    class Meta:
        name = "complexfooType"

    comp_foo: List[float] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            required=True,
            tokens=True
        )
    )


@dataclass
class SimpleTest:
    """
    :ivar value:
    """
    class Meta:
        name = "simpleTest"

    value: List[float] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            tokens=True
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
