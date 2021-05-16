import sys
import os
import time
import timeit
import itertools
import unittest
from pathlib import Path
from loguru import logger


current_folder = Path(__file__).absolute().parent
father_folder = str(current_folder.parent)
sys.path.append(father_folder)

from directedgraph.dgutils import FileManager


logger.add(
    "logs/test_dgutils.py.log",
    level="DEBUG",
    format="{time:YYYY-MM-DD :mm:ss} - {level} - {file} - {line} - {message}",
    rotation="10 MB",
)
logger.info("Start Log")


class TestFileManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.path = Path(os.path.dirname(__file__)).joinpath("test.xml")

    def tearDown(self):
        pass

    @logger.catch
    def test_read_graph(self):
        filemanager1 = FileManager()
        data1 = filemanager1.read_graph(str(self.path))
        list1 = [{"name": "My Graph"}]
        list2 = [
            {
                "type": "Node",
                "uid": "1f9cb9",
                "name": "N1",
                "colour": "#FF0000",
                "position_x": "0",
                "position_y": "0",
            },
            {
                "type": "Node",
                "uid": "9cf405",
                "name": "N2",
                "colour": "#FF0000",
                "position_x": "10",
                "position_y": "10",
            },
            {
                "type": "Node",
                "uid": "a129a9",
                "name": "N3",
                "colour": "#FF0000",
                "position_x": "20",
                "position_y": "20",
            },
            {
                "type": "Node",
                "uid": "59d632",
                "name": "N4",
                "colour": "#FF0000",
                "position_x": "30",
                "position_y": "30",
            },
            {
                "type": "Node",
                "uid": "8ad505",
                "name": "N5",
                "colour": "#FF0000",
                "position_x": "40",
                "position_y": "40",
            },
            {
                "type": "Node",
                "uid": "1d2386",
                "name": "N6",
                "colour": "#FF0000",
                "position_x": "50",
                "position_y": "50",
            },
            {
                "type": "Node",
                "uid": "567071",
                "name": "N7",
                "colour": "#FF0000",
                "position_x": "60",
                "position_y": "60",
            },
            {
                "type": "SourceNode",
                "uid": "14123f",
                "name": "S1",
                "colour": "#00FF00",
                "position_x": "100",
                "position_y": "100",
                "user_defined_attribute": "5",
            },
            {
                "type": "GroundNode",
                "uid": "365bb9",
                "name": "G1",
                "colour": "#FFFF00",
                "position_x": "200",
                "position_y": "200",
            },
            {
                "type": "Arc",
                "uid": "8665f0",
                "name": "A1",
                "colour": "#FFFFFF",
                "node1_uid": "14123f",
                "node2_uid": "1f9cb9",
                "user_define_arc_type": "None",
            },
            {
                "type": "Arc",
                "uid": "174404",
                "name": "C1",
                "colour": "#FFFFFF",
                "node1_uid": "59d632",
                "node2_uid": "1d2386",
                "user_define_arc_type": "Capacitor",
            },
            {
                "type": "Arc",
                "uid": "1c7ad3",
                "name": "C2",
                "colour": "#FFFFFF",
                "node1_uid": "1d2386",
                "node2_uid": "567071",
                "user_define_arc_type": "Capacitor",
            },
            {
                "type": "Arc",
                "uid": "2201bd",
                "name": "R1",
                "colour": "#FFFFFF",
                "node1_uid": "1f9cb9",
                "node2_uid": "9cf405",
                "user_define_arc_type": "Resistor",
            },
            {
                "type": "Arc",
                "uid": "bd6295",
                "name": "R2",
                "colour": "#FFFFFF",
                "node1_uid": "9cf405",
                "node2_uid": "a129a9",
                "user_define_arc_type": "Resistor",
            },
            {
                "type": "Arc",
                "uid": "a88df3",
                "name": "R3",
                "colour": "#FFFFFF",
                "node1_uid": "9cf405",
                "node2_uid": "a129a9",
                "user_define_arc_type": "Resistor",
            },
            {
                "type": "Arc",
                "uid": "b081b6",
                "name": "R4",
                "colour": "#FFFFFF",
                "node1_uid": "a129a9",
                "node2_uid": "59d632",
                "user_define_arc_type": "Resistor",
            },
            {
                "type": "Arc",
                "uid": "2f7002",
                "name": "R5",
                "colour": "#FFFFFF",
                "node1_uid": "a129a9",
                "node2_uid": "59d632",
                "user_define_arc_type": "Resistor",
            },
            {
                "type": "Arc",
                "uid": "0dcb2f",
                "name": "R6",
                "colour": "#FFFFFF",
                "node1_uid": "a129a9",
                "node2_uid": "59d632",
                "user_define_arc_type": "Resistor",
            },
            {
                "type": "Arc",
                "uid": "33ae52",
                "name": "R7",
                "colour": "#FFFFFF",
                "node1_uid": "59d632",
                "node2_uid": "8ad505",
                "user_define_arc_type": "Resistor",
            },
            {
                "type": "Arc",
                "uid": "6bf56b",
                "name": "R8",
                "colour": "#FFFFFF",
                "node1_uid": "8ad505",
                "node2_uid": "567071",
                "user_define_arc_type": "Resistor",
            },
            {
                "type": "Arc",
                "uid": "ea40e5",
                "name": "R9",
                "colour": "#FFFFFF",
                "node1_uid": "567071",
                "node2_uid": "365bb9",
                "user_define_arc_type": "Resistor",
            },
        ]
        self.assertEqual(data1[0], list1)
        self.assertEqual(data1[1], list2)


if __name__ == "__main__":
    unittest.main()
