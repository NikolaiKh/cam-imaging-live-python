# cam-imaging-live-python
Live stream of a camera via pycromanager, show live background subtraction, save files.

Interface is made with QtDesigner and based on PyQt 5/6. Pyqtgraph is used to show 2d images, as it's faster then matplotlib: https://stackoverflow.com/questions/40126176/fast-live-plotting-in-matplotlib-pyplot?noredirect=1&lq=1

Multithreading is used also, according to: taken from https://www.pythonguis.com/tutorials/multithreading-pyqt-applications-qthreadpool/
