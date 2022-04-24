from dataclasses import dataclass, field
from typing import List, Union
from output.models.ms_data.simple_type.st_z074_a_xsd.st_z074_b import List2

__NAMESPACE__ = "a"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "a"

    value: List[Union[str, List2]] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
