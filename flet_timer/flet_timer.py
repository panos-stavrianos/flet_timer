import threading
import flet as ft
from interval_timer import IntervalTimer
from flet.core.ref import Ref
from typing import Any, Optional
from flet.core.types import OptionalControlEventCallable
from flet.core.control import OptionalNumber
class Timer(ft.Container):
    def __init__(
            self, 
            name: Optional[str] = None, 
            interval_s: OptionalNumber = None, 
            callback : OptionalControlEventCallable = None,
            #
            # Container
            #
            *args,
             **kwargs
            ):
    
        ft.Container.__init__(
            self,
            width=0,
            height=0,
            visible=False,
            *args,
            **kwargs
        )
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
        pass

    def will_unmount(self):
        self.stop()
        super().will_unmount()

    def before_update(self):
        super().before_update()