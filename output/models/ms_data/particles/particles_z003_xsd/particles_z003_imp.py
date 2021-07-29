from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "importedXSD"


@dataclass
class Foo:
    class Meta:
        name = "foo"
        namespace = "importedXSD"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )
