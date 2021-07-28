from dataclasses import dataclass, field
from typing import List, Optional, Union

__NAMESPACE__ = "http://www.w3.org/XML/2008/xsdl-exx/ns1"


@dataclass
class E:
    class Meta:
        name = "e"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"

    value: Optional[str] = field(
        default=None,
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
            "required": True,
        }
    )


@dataclass
class T:
    e_or_e1: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "e",
                    "type": str,
                    "namespace": "http://www.w3.org/XML/2008/xsdl-exx/ns1",
                },
                {
                    "name": "e1",
                    "type": Union[str, E1],
                    "namespace": "http://www.w3.org/XML/2008/xsdl-exx/ns1",
                },
            ),
            "max_occurs": 2,
        }
    )


@dataclass
class Test(T):
    class Meta:
        name = "test"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"
