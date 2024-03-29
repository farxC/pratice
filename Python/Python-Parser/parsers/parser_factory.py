from .xml_parser import XMLParser
from .csv_parser import CSVParser
from .utils import get_file_name_from_path
import xml.etree.ElementTree as ET
import csv
import sys

def convert_to_json_factory(format,file):
    # Precondition: file already existis, file in is the given format
    # Instanciate the correct parser
    if format == "xml":
        file_name = get_file_name_from_path(file)
        try:
            menu = ET.parse(file).getroot()
        except(ET.ParseError):
            raise ValueError(
                f"error: The file {file_name} is not correctly-formatted")
        return XMLParser(root, file_name)
    
    if format == "csv":
        csv_data = open(file)
        return CSVParser(csv.DictReader(csv_data),
                         get_file_name_from_path(file))