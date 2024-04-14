from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional, Union

__NAMESPACE__ = "ElemDecl/identityConstraintDefs"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/identityConstraintDefs"

    element_or_element_ref_or_element_refs: List[
        Union["Root.Element", "Root.ElementRef", "Root.ElementRefs"]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Element",
                    "type": ForwardRef("Root.Element"),
                    "namespace": "",
                },
                {
                    "name": "ElementRef",
                    "type": ForwardRef("Root.ElementRef"),
                    "namespace": "",
                },
                {
                    "name": "ElementRefs",
                    "type": ForwardRef("Root.ElementRefs"),
                    "namespace": "",
                },
            ),
        },
    )

    @dataclass
    class Element:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class ElementRef:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class ElementRefs:
        value: List[str] = field(
            default_factory=list,
            metadata={
                "tokens": True,
            },
        )
