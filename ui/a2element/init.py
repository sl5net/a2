# -*- coding: utf-8 -*-
"""
@created: 2016 11 11
@author: Eric Werner
"""
import a2ctrl
from PySide import QtGui
from a2element import EditCtrl
from a2widget import a2CodeField


class Edit(EditCtrl):
    """
    The background widget that sets up how the user can edit the element,
    visible when editing the module.
    """
    def __init__(self, cfg, main, parentCfg):
        super(Edit, self).__init__(cfg, main, parentCfg)

        self.mainLayout.addWidget(QtGui.QLabel('Some code to be executed on a2 runtime start:'))
        self.text_field = a2CodeField()
        self.mainLayout.addWidget(self.text_field)
        a2ctrl.connect.control(self.text_field, 'code', self.cfg)

    @staticmethod
    def element_name():
        """The elements display name shown in UI"""
        return 'Init Call'

    @staticmethod
    def element_icon():
        return a2ctrl.Icons.inst().code


def get_settings(module_key, cfg, db_dict, user_cfg):
    db_dict.setdefault('init_calls', []).append(cfg['code'])
