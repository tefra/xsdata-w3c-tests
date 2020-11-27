from dataclasses import dataclass, field
from typing import Optional, Union


@dataclass
class Example:
    value: Optional[Union[int, str]] = field(
        default=None,
    )
