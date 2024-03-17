from dataclasses import dataclass, field
from typing import Union

from output.models.ms_data.simple_type.test298668_a_xsd.test298668_b import (
    TPredefinedLnclassEnum,
)

__NAMESPACE__ = "a"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "a"

    value: Union[str, TPredefinedLnclassEnum] = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\p{Lu}+",
        },
    )
