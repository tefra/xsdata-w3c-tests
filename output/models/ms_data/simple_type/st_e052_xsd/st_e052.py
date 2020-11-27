from dataclasses import dataclass, field
from typing import Optional, Union


@dataclass
class Root:
    class Meta:
        name = "root"

    value: Optional[Union[bool, int, str]] = field(
        default=None,
    )
