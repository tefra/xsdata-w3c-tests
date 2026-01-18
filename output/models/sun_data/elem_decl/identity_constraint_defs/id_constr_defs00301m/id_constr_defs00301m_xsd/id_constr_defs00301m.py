from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

__NAMESPACE__ = "ElemDecl/identityConstraintDefs"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/identityConstraintDefs"

    element_or_element_ref_or_element_refs: list[
        Root.Element | Root.ElementRef | Root.ElementRefs
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

    @dataclass(kw_only=True)
    class Element:
        value: str = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ElementRef:
        value: str = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ElementRefs:
        value: list[str] = field(
            default_factory=list,
            metadata={
                "tokens": True,
            },
        )
