from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    """
    :ivar value:
    """
    class Meta:
        name = "b"
        namespace = "http://xsdtesting"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Foo:
    """
    :ivar www_w3_org_1999_xhtml_element:
    """
    class Meta:
        name = "foo"
        namespace = "http://xsdtesting"

    www_w3_org_1999_xhtml_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##local http://www.w3.org/1999/xhtml",
            min_occurs=1,
            max_occurs=10
        )
    )
