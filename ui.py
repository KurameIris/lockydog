# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv
import wx.dataview


###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Yuano的动态抽奖姬", pos=wx.DefaultPosition,
                          size=wx.Size(800, 521), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(-1, 540), wx.Size(-1, 900))

        bSizer44 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel31 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 40), wx.TAB_TRAVERSAL)
        self.m_panel31.SetMinSize(wx.Size(-1, 40))
        self.m_panel31.SetMaxSize(wx.Size(-1, 40))

        bSizer45 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText25 = wx.StaticText(self.m_panel31, wx.ID_ANY, u"动态ID", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText25.Wrap(-1)

        bSizer45.Add(self.m_staticText25, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.dym_id = wx.TextCtrl(self.m_panel31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer45.Add(self.dym_id, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.start_button = wx.Button(self.m_panel31, wx.ID_ANY, u"开始", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer45.Add(self.start_button, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText26 = wx.StaticText(self.m_panel31, wx.ID_ANY, u"截止日", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText26.Wrap(-1)

        bSizer45.Add(self.m_staticText26, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.end_date = wx.adv.DatePickerCtrl(self.m_panel31, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                              wx.DefaultSize, wx.adv.DP_DROPDOWN)
        bSizer45.Add(self.end_date, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText27 = wx.StaticText(self.m_panel31, wx.ID_ANY, u"截止时间", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText27.Wrap(-1)

        bSizer45.Add(self.m_staticText27, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.end_time = wx.adv.TimePickerCtrl(self.m_panel31, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                              wx.DefaultSize, wx.adv.TP_DEFAULT)
        bSizer45.Add(self.end_time, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_panel31.SetSizer(bSizer45)
        self.m_panel31.Layout()
        bSizer44.Add(self.m_panel31, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel32 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer46 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer48 = wx.BoxSizer(wx.VERTICAL)

        self.battle_field_title = wx.StaticText(self.m_panel32, wx.ID_ANY, u"BattleField", wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.battle_field_title.Wrap(-1)

        bSizer48.Add(self.battle_field_title, 0, wx.ALL, 5)

        self.battle_field = wx.dataview.DataViewListCtrl(self.m_panel32, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                         0)
        self.bf_ico = self.battle_field.AppendIconTextColumn(u"ico", wx.dataview.DATAVIEW_CELL_INERT, 30, wx.ALIGN_LEFT,
                                                             wx.dataview.DATAVIEW_COL_RESIZABLE)
        self.bf_uid = self.battle_field.AppendTextColumn(u"uid", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT,
                                                         wx.dataview.DATAVIEW_COL_RESIZABLE | wx.dataview.DATAVIEW_COL_SORTABLE)
        self.bf_name = self.battle_field.AppendTextColumn(u"名字", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT,
                                                          wx.dataview.DATAVIEW_COL_RESIZABLE | wx.dataview.DATAVIEW_COL_SORTABLE)
        self.bf_time = self.battle_field.AppendTextColumn(u"转发时间", wx.dataview.DATAVIEW_CELL_INERT, 180, wx.ALIGN_LEFT,
                                                          wx.dataview.DATAVIEW_COL_RESIZABLE | wx.dataview.DATAVIEW_COL_SORTABLE)
        self.bf_context = self.battle_field.AppendTextColumn(u"评论", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT,
                                                             wx.dataview.DATAVIEW_COL_RESIZABLE | wx.dataview.DATAVIEW_COL_SORTABLE)
        bSizer48.Add(self.battle_field, 1, wx.ALL | wx.EXPAND, 5)

        self.m_staticText29 = wx.StaticText(self.m_panel32, wx.ID_ANY, u"Winner", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText29.Wrap(-1)

        bSizer48.Add(self.m_staticText29, 0, wx.ALL, 5)

        self.winner = wx.dataview.DataViewListCtrl(self.m_panel32, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.win_ico = self.winner.AppendIconTextColumn(u"ico", wx.dataview.DATAVIEW_CELL_INERT, 30, wx.ALIGN_LEFT,
                                                        wx.dataview.DATAVIEW_COL_RESIZABLE)
        self.win_uid = self.winner.AppendTextColumn(u"uid", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT,
                                                    wx.dataview.DATAVIEW_COL_RESIZABLE)
        self.win_name = self.winner.AppendTextColumn(u"名字", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT,
                                                     wx.dataview.DATAVIEW_COL_RESIZABLE)
        self.win_time = self.winner.AppendTextColumn(u"转发时间", wx.dataview.DATAVIEW_CELL_INERT, 180, wx.ALIGN_LEFT,
                                                     wx.dataview.DATAVIEW_COL_RESIZABLE)
        self.win_obj = self.winner.AppendTextColumn(u"奖品", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT,
                                                    wx.dataview.DATAVIEW_COL_RESIZABLE)
        bSizer48.Add(self.winner, 1, wx.ALL | wx.EXPAND, 5)

        bSizer46.Add(bSizer48, 1, wx.EXPAND, 5)

        self.m_panel33 = wx.Panel(self.m_panel32, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel33.SetMinSize(wx.Size(200, -1))
        self.m_panel33.SetMaxSize(wx.Size(200, -1))

        bSizer47 = wx.BoxSizer(wx.VERTICAL)

        self.everyone_keep_one = wx.Button(self.m_panel33, wx.ID_ANY, u"每个账号只保留第一条", wx.DefaultPosition, wx.DefaultSize,
                                           0)
        bSizer47.Add(self.everyone_keep_one, 0, wx.ALL | wx.EXPAND, 5)

        self.remove_half = wx.Button(self.m_panel33, wx.ID_ANY, u"去掉一半", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer47.Add(self.remove_half, 0, wx.ALL | wx.EXPAND, 5)

        self.remove_one = wx.Button(self.m_panel33, wx.ID_ANY, u"去掉一个", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer47.Add(self.remove_one, 0, wx.ALL | wx.EXPAND, 5)

        self.remove_late = wx.Button(self.m_panel33, wx.ID_ANY, u"去掉来晚的", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer47.Add(self.remove_late, 0, wx.ALL | wx.EXPAND, 5)

        self.keep_late = wx.Button(self.m_panel33, wx.ID_ANY, u"只保留来晚的", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer47.Add(self.keep_late, 0, wx.ALL | wx.EXPAND, 5)

        self.choose_one = wx.Button(self.m_panel33, wx.ID_ANY, u"抽取一人中奖", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer47.Add(self.choose_one, 0, wx.ALL | wx.EXPAND, 5)

        self.restart = wx.Button(self.m_panel33, wx.ID_ANY, u"重新开始", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer47.Add(self.restart, 0, wx.ALL | wx.EXPAND, 5)

        bSizer47.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_bitmap1 = wx.StaticBitmap(self.m_panel33, wx.ID_ANY,
                                         wx.Bitmap(u"lockydog/res/yuaaaa.png", wx.BITMAP_TYPE_ANY), wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        bSizer47.Add(self.m_bitmap1, 1, wx.ALL | wx.EXPAND, 5)

        self.m_panel33.SetSizer(bSizer47)
        self.m_panel33.Layout()
        bSizer47.Fit(self.m_panel33)
        bSizer46.Add(self.m_panel33, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel32.SetSizer(bSizer46)
        self.m_panel32.Layout()
        bSizer46.Fit(self.m_panel32)
        bSizer44.Add(self.m_panel32, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer44)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.start_button.Bind(wx.EVT_BUTTON, self.start_buttonOnButtonClick)
        self.everyone_keep_one.Bind(wx.EVT_BUTTON, self.everyone_keep_oneOnButtonClick)
        self.remove_half.Bind(wx.EVT_BUTTON, self.remove_halfOnButtonClick)
        self.remove_one.Bind(wx.EVT_BUTTON, self.remove_oneOnButtonClick)
        self.remove_late.Bind(wx.EVT_BUTTON, self.remove_lateOnButtonClick)
        self.keep_late.Bind(wx.EVT_BUTTON, self.keep_lateOnButtonClick)
        self.choose_one.Bind(wx.EVT_BUTTON, self.choose_oneOnButtonClick)
        self.restart.Bind(wx.EVT_BUTTON, self.restartOnButtonClick)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def start_buttonOnButtonClick(self, event):
        event.Skip()

    def everyone_keep_oneOnButtonClick(self, event):
        event.Skip()

    def remove_halfOnButtonClick(self, event):
        event.Skip()

    def remove_oneOnButtonClick(self, event):
        event.Skip()

    def remove_lateOnButtonClick(self, event):
        event.Skip()

    def keep_lateOnButtonClick(self, event):
        event.Skip()

    def choose_oneOnButtonClick(self, event):
        event.Skip()

    def restartOnButtonClick(self, event):
        event.Skip()
