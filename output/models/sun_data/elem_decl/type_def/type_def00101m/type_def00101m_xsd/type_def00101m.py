from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/typeDef"


@dataclass
class Answer:
    class Meta:
        name = "answer"
        namespace = "ElemDecl/typeDef"

    value: Optional[bool] = field(
        default=None
    )
