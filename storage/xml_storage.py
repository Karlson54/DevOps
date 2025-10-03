import os
import xml.etree.ElementTree as ET
from .base import DataStorage

class XMLStorage(DataStorage):
    """Зберігання даних у форматі XML."""
    def save(self, students_data, filename: str) -> str:
        if not filename.endswith(".xml"):
            filename += ".xml"
        root = ET.Element("students")
        for sd in students_data:
            stu_el = ET.SubElement(root, "student")
            for key, val in sd.items():
                sub = ET.SubElement(stu_el, key)
                sub.text = str(val)
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
        return os.path.abspath(filename)
