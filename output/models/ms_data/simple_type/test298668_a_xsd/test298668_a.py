from dataclasses import dataclass, field
from typing import Optional, Union
from output.models.ms_data.simple_type.test298668_a_xsd.test298668_b import (
    TPredefinedLnclassEnum,
)

__NAMESPACE__ = "a"


@dataclass
class Root:
    """
    :ivar value:
    """
    class Meta:
        name = "root"
        namespace = "a"

    value: Optional[Union[str, TPredefinedLnclassEnum]] = field(
        default=None,
        metadata=dict(
            required=True,
            min_length=1.0,
            pattern=r"\p{Lu}+"
        )
    )