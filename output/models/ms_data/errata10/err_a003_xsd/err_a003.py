from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "http://www.tempuri.org"


@dataclass
class TestElement:
    class Meta:
        name = "testElement"
        namespace = "http://www.tempuri.org"

    value: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class RootType:
    class Meta:
        name = "rootType"

    test_element: Optional[TestElement] = field(
        default=None,
        metadata={
            "name": "testElement",
            "type": "Element",
            "namespace": "http://www.tempuri.org",
            "required": True,
        },
    )


@dataclass
class Root(RootType):
    class Meta:
        name = "root"
        namespace = "http://www.tempuri.org"
