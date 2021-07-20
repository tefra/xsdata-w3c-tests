from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    class Meta:
        name = "b"
        namespace = "http://xsdtesting"

    value: Optional[str] = field(
        default=None
    )


@dataclass
class Foo:
    class Meta:
        name = "foo"
        namespace = "http://xsdtesting"

    target_namespace_w3_org_1999_xhtml_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace http://www.w3.org/1999/xhtml",
            "min_occurs": 1,
        }
    )
