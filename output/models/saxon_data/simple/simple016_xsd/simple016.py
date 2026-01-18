from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlTime

__NAMESPACE__ = "http://simple016.ly/"


@dataclass(kw_only=True)
class DocType:
    class Meta:
        name = "doc-type"

    chap: list[XmlDate | XmlDateTime | XmlTime] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://simple016.ly/",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class Doc(DocType):
    class Meta:
        name = "doc"
        namespace = "http://simple016.ly/"


@dataclass(kw_only=True)
class Book:
    class Meta:
        name = "book"
        namespace = "http://simple016.ly/"

    doc: list[Doc] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
