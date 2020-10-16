from dataclasses import dataclass, field
from typing import List


@dataclass
class Root:
    """
    :ivar foo:
    :ivar sg:
    """
    class Meta:
        name = "root"

    foo: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    sg: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
