from dataclasses import dataclass, field
from typing import List, Optional, Union

__NAMESPACE__ = "http://www.w3.org/XML/2008/xsdl-exx/ns1"


@dataclass
class E:
    class Meta:
        name = "e"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class E1:
    class Meta:
        name = "e1"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class T:
    e: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/XML/2008/xsdl-exx/ns1",
        }
    )
    e1: List[Union[int, E1]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/XML/2008/xsdl-exx/ns1",
            "max_occurs": 2,
        }
    )


@dataclass
class Test(T):
    class Meta:
        name = "test"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"
