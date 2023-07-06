# Flet Timer

The Flet Timer is a simple timer component for the [Flet framework](https://flet.dev/). It allows you to create timers that execute a callback function at a specified interval.

## Installation

To use the Flet Timer, you can install it using pip:

```
pip install flet-timer
```

## Usage

Here's an example that demonstrates how to use the Flet Timer.

First, let's define a callback function that will execute at a specified interval:

```python
def refresh():
    txt_time.value = datetime.now().strftime("%H:%M:%S")
    page.update()
```

Next, create the Timer object with the desired interval in seconds, a name, and the callback:

```python
timer = Timer(name="timer", interval_s=1, callback=refresh)
```

Finally, add the Timer component to the page:

```python
page.add(timer)
```

The complete example code would look like this:

```python
from datetime import datetime
import flet as ft
from flet_timer.flet_timer import Timer


def main(page: ft.Page):
    page.title = "Flet Timer example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    txt_time = ft.Text(value="None")

    def refresh():
        txt_time.value = datetime.now().strftime("%H:%M:%S")
        page.update()

    timer = Timer(name="timer", interval_s=1, callback=refresh)

    page.add(
        timer,
        txt_time
    )


ft.app(main)
```

In this example, we create a Flet application that displays the current time using the `Text` component. We define a `refresh()` function that updates the `txt_time` value with the current time and triggers a page update. We instantiate a `Timer` with a 1-second interval and the `refresh()` function as the callback. The timer continuously calls the callback, updating the UI with the current time.

## Contributing

Contributions to the Flet Timer project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the [GitHub repository](https://github.com/example/flet-timer).

## License

The Flet Timer is open-source software released under the [MIT License](https://opensource.org/licenses/MIT). See the [LICENSE](https://github.com/example/flet-timer/blob/main/LICENSE) file for more information.