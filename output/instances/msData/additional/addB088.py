from output.models.ms_data.additional.add_b088_xsd.add_b088 import Any
from output.models.ms_data.additional.add_b088_xsd.add_b088 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=[
        Any(
            target_namespace_imported_xsd_element=AnyElement(
                qname="{http://importedXSD}doc1",
                text="",
                tail=None,
                children=[
                    AnyElement(
                        qname="{http://importedXSD}elem1",
                        text="",
                        tail=None,
                        children=[
                            AnyElement(
                                qname="{http://importedXSD}bbb",
                                text="",
                                tail=None,
                                children=[],
                                attributes={}
                            ),
                        ],
                        attributes={}
                    ),
                    AnyElement(
                        qname="{http://importedXSD}elem2",
                        text="",
                        tail=None,
                        children=[
                            AnyElement(
                                qname="{http://importedXSD}bbb",
                                text="",
                                tail=None,
                                children=[],
                                attributes={}
                            ),
                        ],
                        attributes={}
                    ),
                ],
                attributes={}
            )
        ),
    ]
)
