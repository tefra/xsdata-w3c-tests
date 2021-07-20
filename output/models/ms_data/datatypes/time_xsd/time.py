from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlTime


@dataclass
class ComplexfooType:
    class Meta:
        name = "complexfooType"

    comp_foo: Optional[XmlTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class SimpleTest:
    class Meta:
        name = "simpleTest"

    value: Optional[XmlTime] = field(
        default=None
    )


@dataclass
class ComplexTest(ComplexfooType):
    class Meta:
        name = "complexTest"


@dataclass
class Root:
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
    simple_test: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "simpleTest",
            "type": "Element",
        }
    )
