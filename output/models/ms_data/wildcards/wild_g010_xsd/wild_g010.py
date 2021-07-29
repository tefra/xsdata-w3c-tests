from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    class Meta:
        name = "b"
        namespace = "http://xsdtesting"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Foo:
    class Meta:
        name = "foo"
        namespace = "http://xsdtesting"

    local_w3_org_1999_xhtml_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##local http://www.w3.org/1999/xhtml",
            "max_occurs": 10,
        }
    )
