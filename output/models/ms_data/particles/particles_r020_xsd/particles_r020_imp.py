from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://importedXSD"


@dataclass
class ImpElem1:
    class Meta:
        name = "impElem1"
        namespace = "http://importedXSD"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class ImpElem2:
    class Meta:
        name = "impElem2"
        namespace = "http://importedXSD"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )
