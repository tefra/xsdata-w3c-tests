from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "http://www.tempuri.org"


@dataclass(kw_only=True)
class TestElement:
    class Meta:
        name = "testElement"
        namespace = "http://www.tempuri.org"

    value: XmlPeriod = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RootType:
    class Meta:
        name = "rootType"

    test_element: TestElement = field(
        metadata={
            "name": "testElement",
            "type": "Element",
            "namespace": "http://www.tempuri.org",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Root(RootType):
    class Meta:
        name = "root"
        namespace = "http://www.tempuri.org"
