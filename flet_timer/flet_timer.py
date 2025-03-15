import threading
import flet as ft
from interval_timer import IntervalTimer
from flet.core.control import Control
from flet.core.ref import Ref
from typing import Any, Optional
from flet.core.types import OptionalControlEventCallable
from flet.core.control import OptionalNumber

class Timer(ft.Control):
    def __init__(
            self, 
            name: Optional[str] = None, 
            interval_s: OptionalNumber = None, 
            callback : OptionalControlEventCallable = None,
            #
            # Control
            #
            ref: Optional[Ref] = None,
            data: Any = None
            ):
    
        Control.__init__(
            self,
            ref=ref,
            data=data,
        )
        self.name = name
        self.interval_s = interval_s
        self.callback = callback
        self.active = False
        self.th = threading.Thread(target=self.tick, daemon=True)

        if callback is None:
            self.callback = lambda: print(f"Timer {self.name} ticked")

    # name
    @property
    def name(self) -> Optional[str]:
        return self._get_attr("name")

    @name.setter
    def name(self, value: Optional[str]):
        self._set_attr("name", value)

    # interval
    @property
    def interval_s(self) -> OptionalNumber:
        return self._get_attr("interval_s")

    @interval_s.setter
    def interval_s(self, value) -> OptionalNumber:
        self._set_attr("interval_s", value)

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

    def before_update(self):
        super().before_update()

    def _get_control_name(self):
        return "timer"