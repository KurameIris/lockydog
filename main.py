import os
import wx
import dym
import logging

logger = logging.getLogger()


def start():
    app = wx.App(False)
    frame = dym.WindowsMixin(None)
    here = os.path.abspath(".")
    ico = wx.Icon(os.path.join(here, "lockydog", "res", "yuaaaa_small.BMP"), wx.BITMAP_TYPE_ANY)
    frame.SetIcon(ico)

    frame.Show(True)
    app.MainLoop()


if __name__ == '__main__':
    # 解决打包文件与multiprocessing冲突的问题
    # multiprocessing.freeze_support()

    try:
        start()
    except Exception as e:
        logger.error(f"Unknown Error: {e}")
