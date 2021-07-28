from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime


@dataclass
class ComplexfooType:
    class Meta:
        name = "complexfooType"

    comp_foo: Optional[XmlDateTime] = field(
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

    value: Optional[XmlDateTime] = field(
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
    simple_test: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "simpleTest",
            "type": "Element",
            "required": True,
        }
    )
