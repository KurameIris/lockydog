import ui
import wx
import json
import requests
import datetime
import os.path
import random
import logging
import traceback
from PIL import Image
from wx.dataview import DataViewIconText
from bilibili_api import dynamic, sync, Credential, user

logger = logging.getLogger()


async def main(dym_id):
    # 初始化
    dy = dynamic.Dynamic(dym_id)
    # 存储所有转发信息
    reposters = []
    # 存储下一页起始位置
    offset = "0"
    while True:
        # 循环拉取动态
        r = await dy.get_reposts(offset)
        # 存入
        logger.info(f"拉到了信息：{r}")
        reposters.extend(r['items'])
        logger.info(f'拉取转发信息中 {len(reposters)} / {r["total"]}')

        if r['has_more'] != 1:
            # 无更多，退出循环
            break

        # 设置下一页起始位置
        offset = r['offset']

    return reposters


class WindowsMixin(ui.MyFrame2):
    DymInfo = []
    Session = requests.Session()
    CacheDir = "cache"
    BattleField = []
    PlayGround = []
    Winner = []

    async def load_dym(self, dym_id):
        # 初始化
        dy = dynamic.Dynamic(dym_id)
        # 存储所有转发信息
        reposters = []
        # 存储下一页起始位置
        offset = "0"

        while True:
            # 循环拉取动态
            r = await dy.get_reposts(offset)
            # 存入
            logger.info(f"拉到了信息：{r}")
            reposters.extend(r['items'])
            logger.info(f'拉取转发信息中 {len(reposters)} / {r["total"]}')
            self.battle_field_title.SetLabelText(f'BattleField ({len(reposters)} / {r["total"]})')

            if r['has_more'] != 1:
                # 无更多，退出循环
                break

            # 设置下一页起始位置
            offset = r['offset']

        return reposters

    def get_ico(self, url: str, name: str):
        img_format = url[url.rfind(".") + 1:]
        f_name = f"{name}.{img_format}"
        fp = os.path.join(self.CacheDir, f_name)
        if os.path.exists(fp):
            return fp
        try:
            # 保存头像
            resp = self.Session.get(url)
            if resp.status_code == 200:
                with open(fp, "wb+") as f:
                    f.write(resp.content)
                # 缩放
                Image.open(fp).resize((25, 25)).save(fp)
            return fp
        except Exception as e:
            logger.error(f"get ico ex: {e}")
            logger.error(traceback.format_exc(5))
            return None

    def check_for_data(self):
        if self.BattleField:
            return True
        else:
            return False

    def refresh_title(self):
        self.battle_field_title.SetLabelText(f"BattleField ({len(self.PlayGround)}/{len(self.BattleField)})")

    def draw(self):
        self.battle_field.DeleteAllItems()
        for ico, _uid, _uname, _timestamp, _content, _format_timestamp in self.PlayGround:
            self.battle_field.AppendItem([ico, str(_uid), _uname, _format_timestamp, _content])
        self.refresh_title()

    def win(self, name=""):
        data = self.PlayGround.pop(random.choice(range(len(self.PlayGround))))
        ico, _uid, _uname, _timestamp, _content, _format_timestamp = data
        self.winner.AppendItem([ico, str(_uid), _uname, _format_timestamp, name])

    def start_buttonOnButtonClick(self, event):
        """
        拉取动态
        :param event:
        :return:
        """
        try:
            if not os.path.exists(self.CacheDir):
                os.mkdir(self.CacheDir)

            self.BattleField = []
            self.PlayGround = []
            self.Winner = []

            self.dym_id.GetValue()

            self.DymInfo = sync(self.load_dym(int(self.dym_id.GetValue())))

            _card = ""
            for _d in self.DymInfo:
                try:

                    _desc = _d["desc"]

                    _card = json.loads(_d["card"])

                    _user = _card["user"]
                    _uid = _user["uid"]
                    _uname = _user["uname"]
                    _url = _user["face"]

                    _item = _card["item"]
                    _content = _item["content"]
                    _timestamp = datetime.datetime.fromtimestamp(int(_desc.get("timestamp")))
                    _format_timestamp = datetime.datetime.strftime(_timestamp, "%Y-%m-%d %H:%M:%S")

                    ico_path = self.get_ico(_url, _uid)
                    if ico_path:
                        ioc_obj = wx.Icon(ico_path, desiredWidth=25, desiredHeight=25)
                        ico = DataViewIconText(text="", icon=ioc_obj)
                    else:
                        ico = None
                    self.BattleField.append([ico, _uid, _uname, _timestamp, _content, _format_timestamp])
                    self.PlayGround.append([ico, _uid, _uname, _timestamp, _content, _format_timestamp])
                except Exception as e:
                    logger.info(e, _card)
                    logger.error(traceback.format_exc(5))
        except Exception as e:
            logger.error(e)
            logger.error(traceback.format_exc(5))
        else:
            self.draw()

    def everyone_keep_oneOnButtonClick(self, event):
        """
        每个id保留第一条
        :param event:
        :return:
        """
        if not self.check_for_data():
            return event.Skip()
        cache = dict()
        for ico, _uid, _uname, _timestamp, _content, _format_timestamp in self.PlayGround:
            if _uid in cache:
                cache[_uid].append([ico, _uid, _uname, _timestamp, _content, _format_timestamp])
            else:
                cache.update({_uid: [
                    [ico, _uid, _uname, _timestamp, _content, _format_timestamp]
                ]})
        self.PlayGround.clear()
        for player, message in cache.items():
            message.sort(key=lambda x: x[3])
            self.PlayGround.append(message[0])
            self.draw()

    def remove_halfOnButtonClick(self, event):
        """
        去掉一半
        :param event:
        :return:
        """
        if not self.check_for_data():
            return event.Skip()
        if len(self.PlayGround) > 1:
            for _ in range(int(len(self.PlayGround) / 2)):
                loser = random.choice(range(len(self.PlayGround)))
                self.PlayGround.pop(loser)
        self.draw()

    def remove_oneOnButtonClick(self, event):
        """
        去掉一个
        :param event:
        :return:
        """
        if not self.check_for_data():
            return event.Skip()
        if len(self.PlayGround) > 1:
            loser = random.choice(range(len(self.PlayGround)))
            while self.Safe == str(self.PlayGround[loser][1]):
                loser = random.choice(range(len(self.PlayGround)))
            self.PlayGround.pop(loser)
        self.draw()

    def remove_lateOnButtonClick(self, event):
        """
        去掉来晚的人
        :param event:
        :return:
        """
        if not self.check_for_data():
            return event.Skip()

        _date = self.end_date.GetValue()
        logger.info(_date)
        _time = self.end_time.GetValue()
        _target_time = datetime.datetime(
            _date.year, _date.month + 1, _date.day, _time.hour, _time.minute, _time.second
        )
        logger.info(f"去掉这个时间后的: {datetime.datetime.strftime(_target_time, '%Y-%m-%d %H:%M:%S')}")

        def _filter(data):
            return _target_time >= data[3]

        tmp = list(filter(_filter, self.PlayGround))
        self.PlayGround = tmp
        self.draw()

    def keep_lateOnButtonClick(self, event):
        """
        只保留来晚的人
        :param event:
        :return:
        """
        if not self.check_for_data():
            return event.Skip()

        _date = self.end_date.GetValue()
        _time = self.end_time.GetValue()

        _target_time = datetime.datetime(
            _date.year, _date.month + 1, _date.day, _time.hour, _time.minute, _time.second
        )
        logger.info(f"保留这个时间之后的: {datetime.datetime.strftime(_target_time, '%Y-%m-%d %H:%M:%S')}")

        def _filter(data):
            return _target_time <= data[3]

        tmp = list(filter(_filter, self.PlayGround))
        self.PlayGround = tmp
        self.draw()

    def choose_oneOnButtonClick(self, event):
        if not self.check_for_data():
            return event.Skip()
        obj = wx.TextEntryDialog(self, "输入奖品名称：")
        if obj.ShowModal() == wx.ID_OK:
            obj_name = obj.GetValue()
            self.win(obj_name)

    def restartOnButtonClick(self, event):
        if not self.check_for_data():
            return event.Skip()
        self.PlayGround = [*self.BattleField]
        self.Winner = []
        self.draw()
