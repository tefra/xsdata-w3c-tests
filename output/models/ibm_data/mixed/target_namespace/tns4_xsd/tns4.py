from dataclasses import dataclass, field
from typing import List

from output.models.ibm_data.mixed.target_namespace.tns4_xsd.tns4_imp import A

__NAMESPACE__ = "http://test1"


@dataclass
class X:
    class Meta:
        name = "x"
        namespace = "http://test1"

    a: List[A] = field(
        default_factory=list,
        metadata={
            "wrapper": "y",
            "type": "Element",
            "namespace": "http://test2",
            "min_occurs": 1,
        },
    )
