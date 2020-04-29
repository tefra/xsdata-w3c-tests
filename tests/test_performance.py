from pathlib import Path

from xsdata.formats.dataclass.parsers import XmlParser

from output.models.common import xsts_xsd


def test_xml_parser_performance(benchmark):

    def parse():
        root = Path(__file__).parent.parent
        xml_path = root.joinpath("w3c/nistMeta/NISTXMLSchemaDatatypes.testSet")

        XmlParser().from_path(xml_path, xsts_xsd.TestSet)

    result = benchmark(parse)
