from dataclasses import dataclass, field
from typing import Optional, Union


@dataclass
class Root:
    class Meta:
        name = "root"

    value: Optional[Union[str, int]] = field(
        default=None,
    )
