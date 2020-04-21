from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Foo:
    """
    :ivar local_element:
    """
    class Meta:
        name = "foo"
        namespace = "http://xsdtesting"

    local_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##local",
            required=True
        )
    )
