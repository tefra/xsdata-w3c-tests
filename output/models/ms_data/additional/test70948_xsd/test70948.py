from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xsdtesting"

    value: Optional[int] = field(
        default=None
    )
