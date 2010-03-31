# -*- coding: utf-8 -*-
### BEGIN LICENSE
# Copyright (C) 2010 Benjamin Elbers <elbersb@gmail.com>
#This program is free software: you can redistribute it and/or modify it 
#under the terms of the GNU General Public License version 3, as published 
#by the Free Software Foundation.
#
#This program is distributed in the hope that it will be useful, but 
#WITHOUT ANY WARRANTY; without even the implied warranties of 
#MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR 
#PURPOSE.  See the GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License along 
#with this program.  If not, see <http://www.gnu.org/licenses/>.
### END LICENSE

import gtk
from otrverwaltung.gui import AddDownloadDialog

from otrverwaltung.actions.baseaction import BaseAction

class Add(BaseAction):
    def __init__(self, app, gui):
        self.update_list = False
        self.__gui = gui

    def do(self):
        dialog = AddDownloadDialog.NewAddDownloadDialog()
        if dialog.run() == gtk.RESPONSE_OK:
            dialog.destroy()
        else:
            dialog.destroy()
            return
            
                

