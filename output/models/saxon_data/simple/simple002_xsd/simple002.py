from dataclasses import dataclass, field
from typing import List, Type, Union

__NAMESPACE__ = "http://simple001.ly/"


@dataclass
class Chap:
    class Meta:
        name = "chap"

    section: List["Chap.Section"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://simple001.ly/",
            "min_occurs": 1,
        },
    )

    @dataclass
    class Section:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        nr: float = field(
            default=float("inf"),
            metadata={
                "type": "Attribute",
            },
        )
        ref: str = field(
            init=False,
            default="+INF",
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://simple001.ly/"

    chap_or_appx: List[Union["Doc.Chap", "Doc.Appx"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "chap",
                    "type": Type["Doc.Chap"],
                },
                {
                    "name": "appx",
                    "type": Type["Doc.Appx"],
                },
            ),
        },
    )

    @dataclass
    class Chap(Chap):
        pass

    @dataclass
    class Appx(Chap):
        pass
