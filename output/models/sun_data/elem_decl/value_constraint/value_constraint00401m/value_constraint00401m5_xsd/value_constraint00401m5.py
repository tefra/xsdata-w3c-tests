from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/valueConstraint"


@dataclass
class Answer:
    """
    :ivar value:
    :ivar certainty:
    """
    class Meta:
        name = "answer"

    value: Optional[bool] = field(
        default=None,
    )
    certainty: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Root:
    """
    :ivar any_element:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/valueConstraint"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class E(Answer):
    class Meta:
        namespace = "ElemDecl/valueConstraint"
