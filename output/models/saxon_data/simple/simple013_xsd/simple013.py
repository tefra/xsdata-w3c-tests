from dataclasses import dataclass, field
from datetime import datetime, time
from typing import List, Union

__NAMESPACE__ = "http://simple013.ly/"


@dataclass
class DocType:
    class Meta:
        name = "doc-type"

    chap: List[Union[str, datetime, time]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://simple013.ly/",
            "min_occurs": 1,
        }
    )


@dataclass
class SubDocType:
    class Meta:
        name = "sub-doc-type"

    chap: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://simple013.ly/",
            "min_occurs": 1,
        }
    )


@dataclass
class Doc(DocType):
    class Meta:
        name = "doc"
        namespace = "http://simple013.ly/"


@dataclass
class Subdoc(SubDocType):
    class Meta:
        name = "subdoc"
        namespace = "http://simple013.ly/"


@dataclass
class Book:
    class Meta:
        name = "book"
        namespace = "http://simple013.ly/"

    subdoc: List[Subdoc] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "sequential": True,
        }
    )
    doc: List[Doc] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "sequential": True,
        }
    )
