# Python-Spinner
Python-Spinner for Terminal Output

## Example
With `python spinner.py` (on Linux) you can see some examples.

## USING
You can use a loading/spinner animation like `time.sleep(interval_time)`
Optional with a countdown.
```python
import spinner
spinner.sleep(interval_time, countdown=True|False|None)
```
You can use a loading/spinner animation while a callable function returns True
```python
import spinner
spinner.sleep(callback=callable_function)
```
You can use a loading/spinner animation while a callable function returns False
```python
import spinner
spinner.sleep(callback=callable_function, negative=True)
```
You can use a different loading/spinner animation
```python
import spinner
spinner.sleep(interval_time=interval_time, loading_anim=[".  ",".. ","..."])
```
