import threading

import flet as ft
from interval_timer import IntervalTimer


class Timer(ft.UserControl):
    def __init__(self, name="Timer", interval_s=1, callback=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.interval_s = interval_s
        self.callback = callback
        self.active = False
        self.th = threading.Thread(target=self.tick, daemon=True)
        if callback is None:
            self.callback = lambda: print(f"Timer {self.name} ticked")

    def did_mount(self):
        self.start()
        self.th.start()

    def start(self):
        self.active = True

    def stop(self):
        self.active = False

    def tick(self):
        for _ in IntervalTimer(self.interval_s):
            if not self.active:
                break
            try:
                self.callback()
            except Exception as e:
                print(e)

    def build(self):
        return ft.Container(padding=0, margin=0)

    def will_unmount(self):
        self.stop()
        super().will_unmount()
