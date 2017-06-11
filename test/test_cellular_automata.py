# -*- coding: utf-8 -*-

import unittest
from src.cellular_automata import init_rule, next


class TestCellularAutomata(unittest.TestCase):

    def test_init_rule(self):
        self.assertEqual(
            init_rule(0),
            [False, False, False, False, False, False, False, False])
        self.assertEqual(
            init_rule(1),
            [True, False, False, False, False, False, False, False])
        self.assertEqual(
            init_rule(30),
            [False, True, True, True, True, False, False, False])
        self.assertEqual(
            init_rule(255),
            [True, True, True, True, True, True, True, True])
        with self.assertRaises(ValueError):
            init_rule(-1)
        with self.assertRaises(ValueError):
            init_rule(256)

    def test_next(self):
        rule = init_rule(30)
        self.assertEqual(next(rule, [True]),
                         [True, True, True])
