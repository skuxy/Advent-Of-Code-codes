#!/usr/bin/env python
# -*- coding: utf-8 -*-
from day2 import OPCODE_MAP, ShipComputer


def set_value(comp, address, value):
    comp.intcode[address] = value


def output_value(comp, address):
    return comp.intcode[address]


OPCODE_MAP[3] = set_value
OPCODE_MAP[4] = output_value


class UpgradedShipComputer(ShipComputer):
    def __init__(self, intcode):
        super().__init__(intcode)
        self.mode = 0

    def parse_opcode(self, opcode):
        operation = opcode[-2:]
        first_operator_mode = opcode[-3]
        second_operator_mode = opcode[-4]
        third_operator = None
        
        if len(opcode) > 4:
            third_operator = opcode[-5]

    def _fetch_parameter(self, mode, value):
        if mode == 1:
            return value
        else:
            return self.intcode[value]

    def forward(self, mode):
        mode_step = {
        }
