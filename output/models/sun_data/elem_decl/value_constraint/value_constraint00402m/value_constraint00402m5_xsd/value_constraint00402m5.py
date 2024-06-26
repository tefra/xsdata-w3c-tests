from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/valueConstraint"


@dataclass
class Answer:
    class Meta:
        name = "answer"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    certainty: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/valueConstraint"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class E(Answer):
    class Meta:
        namespace = "ElemDecl/valueConstraint"
