from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://simple010.ly/"


@dataclass
class DocType:
    """
    :ivar chap:
    """
    class Meta:
        name = "doc-type"

    chap: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://simple010.ly/",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class SubDocType:
    """
    :ivar chap:
    """
    class Meta:
        name = "sub-doc-type"

    chap: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://simple010.ly/",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Doc(DocType):
    class Meta:
        name = "doc"
        namespace = "http://simple010.ly/"



@dataclass
class Subdoc(SubDocType):
    class Meta:
        name = "subdoc"
        namespace = "http://simple010.ly/"



@dataclass
class Book:
    """
    :ivar subdoc:
    :ivar doc:
    """
    class Meta:
        name = "book"
        namespace = "http://simple010.ly/"

    subdoc: List[Subdoc] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    doc: List[Doc] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
