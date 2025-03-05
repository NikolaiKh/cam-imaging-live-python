import sys
import os
# from pathlib import Path
try:
    from PyQt5.QtWidgets import QApplication, QWidget, QGraphicsScene, QFileDialog
    from PyQt5.QtCore import QObject, QThreadPool, QRunnable, pyqtSlot, pyqtSignal
except:
    from PyQt6.QtWidgets import QApplication, QWidget, QGraphicsScene, QFileDialog
    from PyQt6.QtCore import QObject, QThreadPool, QRunnable, pyqtSlot, pyqtSignal
    
import traceback
import tkinter
from tkinter import filedialog, messagebox
import numpy as np

from GUI.interface import Ui_Form
import pycromanager_class
# from AppData.EquipmentClasses.devClasses import Lockin_SR_devclass as Lockin_class
# from AppData.EquipmentClasses.devClasses import OxfordInst_ITC5023S_devclass as TempContrl_class
# from AppData.EquipmentClasses.devClasses import pycromanager_devclass as pycromanager_class
import time
from datetime import datetime, date, timedelta
# import json
import h5py


# 2 next classes for multithreading

class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    '''
    finished = pyqtSignal()
    progress = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)


class Worker(QRunnable):
    # used for LIA and XPS initialization
    '''
    Worker thread for any function
    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.
    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    taken from https://www.pythonguis.com/tutorials/multithreading-pyqt-applications-qthreadpool/
    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        self.kwargs['callback'] = self.signals.progress.emit

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(
                *self.args, **self.kwargs
            )
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        # set parameters of GUI
        self.setWindowTitle('Camera live imaging')
        # create an instance of Ui_Form
        self.ui = Ui_Form()
        # initialization of GUI
        self.ui.setupUi(self)
        self.scene = QGraphicsScene()
        # Find own location
        self.path = os.path.dirname(os.path.realpath(sys.argv[0]))
        self.ui.folder_edit.setText(self.path)

        # init camera
        self.Cam_setting = {}
        self.camera_init()
        self.set_camera_settings()
        self.take_images()
        self.Ref = np.zeros(self.img.shape).astype(np.int32)

        # set functions for buttons
        self.ui.folderButton.clicked.connect(self.show_folder_dialog)
        self.ui.StopButton.clicked.connect(self.stop_button_clicked)
        self.ui.StartButton.clicked.connect(self.start_button_press)
        self.ui.save_Button.clicked.connect(self.save_image)
        self.ui.Take_snap_button.clicked.connect(self.Snap_button_pressed)
        self.ui.SetCam_button.clicked.connect(self.set_camera_settings)
        self.ui.Set_Ref_button.clicked.connect(self.SetRef_button_pressed)
        self.ui.remove_ref_button.clicked.connect(self.DelRef_button_pressed)


        # set params of pyqtgraph widgets / does not work
        # hist = self.ui.Image_view.getHistogramWidget()
        # hist.orientation = 'horizontal'

        # show the form
        self.show()

        # folder and file names
        self.folder_path = self.ui.folder_edit.text()
        self.file_name = self.ui.FileName.text()
        # variable for stopping main loop
        self.isStop = True
        # value of min/max intensity lims
        self.ref_int_min = 0
        self.ref_int_max = 1
        self.diff_int_min = -1
        self.diff_int_max = 1

        # setup thread pool
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())
        self.update_frame()


    def camera_init(self):
        # camera connection
        self.camera = pycromanager_class.MMcamera()
        #set max sensetivity
        # self.camera.set_MaxSens()
        #get and set gains
        gain = self.camera.get_gain()
        print(f"Camera gain: {gain}")
        # self.ui.gain_spinBox.setValue(gain)
        #get and set PModes to combobox
        PModes = self.camera.get_allPModevalues()
        print(f"Camera avalible modes: {PModes}")
        # self.ui.pModeComboBox.addItems(PModes)
        # pmode = self.camera.get_PMode()
        # print(f"Camera current mode: {pmode}")
        # index = PModes.index(pmode)
        # if index >= 0:
        #     self.ui.pModeComboBox.setCurrentIndex(index)
        # get and set ROrates to combobox
        ROrates = self.camera.get_allReadoutRates()
        print(f"Camera readout rates: {ROrates}")
        # self.ui.ROrateComboBox.addItems(ROrates)
        # ROrate = self.camera.get_ReadoutRate()
        # print(f"Camera readout rate: {ROrate}")
        # index = ROrates.index(ROrate)
        # if index >= 0:
        #     self.ui.ROrateComboBox.setCurrentIndex(index)
        #get and set binnings to combobox
        binnings = self.camera.get_allBinningvalues()
        self.ui.binningComboBox.addItems(binnings)
        bin = self.camera.get_binning()
        index = binnings.index(bin)
        if index >= 0:
            self.ui.binningComboBox.setCurrentIndex(index)

    def take_images(self):
        self.img = self.camera.get_image().astype(np.int32).T # int32 to save integers => save hard drive space

    def set_camera_settings(self):
        exposure = int(self.ui.ExpTime.text())
        self.camera.set_exposure(exposure)
        binning = self.ui.binningComboBox.currentText()
        self.camera.set_binning(binning)
        # gain = int(self.ui.gain_spinBox.text())
        # self.camera.set_gain(gain)
        mode = self.ui.pModeComboBox.currentText()
        self.camera.set_PMode(mode) # Normal mode closes the program sometimes
        ReadoutRate = self.ui.ROrateComboBox.currentText()
        self.camera.set_ReadoutRate(ReadoutRate)
        self.Cam_setting['Exposure'] = exposure
        self.Cam_setting['Binning'] = binning
        # self.Cam_setting['Gain'] = gain
        self.Cam_setting['Mode'] = mode
        self.Cam_setting['ReadoutRate'] = ReadoutRate

    def update(self):
        self.update_frame()

    def update_frame(self):
        # update current image
        image_data = self.img
        widget = self.ui.Image_view
        # View image
        widget.setImage(image_data)
        if self.ui.refAutoLims_checkBox.isChecked():
            # Get the number of rows and columns
            num_rows, num_columns = image_data.shape
            # Get the central subarray
            central_subarray = image_data[num_rows//4: num_rows*3//4, num_columns//4: num_columns*3//4]
            # Compute the maximum and minimum values
            max_value = np.max(central_subarray)
            min_value = np.min(central_subarray)
            # update limits for future
            self.ref_int_min = min_value
            self.ref_int_max = max_value
            self.ui.refMinInt_spinBox.setValue(min_value)
            self.ui.refMaxInt_spinBox.setValue(max_value)
        else:
            min_value = self.ui.refMinInt_spinBox.value()
            max_value = self.ui.refMaxInt_spinBox.value()
        widget.setLevels(min_value, max_value)  # Set min_value and max_value according to your desired range
        widget.show()

        #update difference image
        if not self.img.shape == self.Ref.shape:
            self.Ref = np.zeros(self.img.shape).astype(np.int32)
        image_data = self.img - self.Ref
        widget = self.ui.Diff_view
        widget.setImage(image_data)
        if self.ui.diffAutoLims_checkBox.isChecked():
            # Get the number of rows and columns
            num_rows, num_columns = image_data.shape
            # Get the central subarray
            central_subarray = image_data[num_rows//4: num_rows*3//4, num_columns//4: num_columns*3//4]
            # Compute the maximum and minimum values
            max_value = np.max(central_subarray)
            min_value = np.min(central_subarray)
            # update limits for future
            self.diff_int_min = min_value
            self.diff_int_max = max_value
            self.ui.diffMinInt_spinBox.setValue(min_value)
            self.ui.diffMaxInt_spinBox.setValue(max_value)
        else:
            min_value = self.ui.diffMinInt_spinBox.value()
            max_value = self.ui.diffMaxInt_spinBox.value()
        # View difference image
        widget.setLevels(min_value, max_value)  # Set min_value and max_value according to your desired range
        widget.show()

    # def save_images(self):
        # saving runs in h5
        # fullname = os.path.join(folder, filename)
        # with h5py.File(self.fullpathname, 'a') as f:
        #     imagecount = '{:0>4}'.format(str(self.imagecount))
        #     Imagename = f"Image_{imagecount}"
        #     # Save the image data with compression
        #     Myimg = f.create_dataset(Imagename, data=self.img, dtype='uint32', compression='gzip')
        #
        #     # Add metadata as attributes
        #     Myimg.attrs['image_shape'] = self.img.shape
        #     Myimg.attrs['color_mode'] = 'grayscale'
        #     Myimg.attrs['Magnetic field'] = f"{self.mVoltage } (V), {self.mfield} mT"
        #     Myimg.attrs['Temp'] = self.Temp['current']
        #     Myimg.attrs['DateTime'] = datetime.now().replace(microsecond=0).isoformat()
        #     f.close()


    def save_image(self, format='%d'):
        # saving one image
        folder = self.ui.folder_edit.text()
        if not os.path.isdir(folder):
            messagebox.showerror("Error", "Folder does not exist!")
            return
        filename = self.ui.FileName.text()
        if not filename:
            messagebox.showerror("Error", "Please enter a file name")
            return
        fullname = os.path.join(folder, filename)
        if os.path.exists(fullname):
            overwrite = messagebox.askyesno('File already exists', 'File already exists. Overwrite?')
            if overwrite:
                with open(fullname, "w") as file:
                    np.savetxt(file, self.img, fmt='%d')
                    self.ui.Image_view.export(fullname + ".png")
                    # messagebox.showinfo("Save", "File saved successfully.")
            else:
                self.isStop = True
        else:
            dir_name = os.path.dirname(os.path.abspath(fullname))
            # Path(dir_name).mkdir(parents=True, exist_ok=True)
            with open(fullname, "w") as file:
                np.savetxt(file, self.img, fmt='%d')
                self.ui.Image_view.export(fullname + ".png")
                # messagebox.showinfo("Save", "File saved successfully.")
        return


    def save_snap(self, image, fullname, format='%d'):
        # saving one image
        folder = self.ui.folder_edit.text()
        if not os.path.isdir(folder):
            messagebox.showerror("Error", "Folder does not exist!")
            return
        filename = self.ui.FileName.text()
        if not filename:
            messagebox.showerror("Error", "Please enter a file name")
            return
        fullname = os.path.join(folder, filename)
        if os.path.exists(fullname):
            overwrite = messagebox.askyesno('File already exists', 'File already exists. Overwrite?')
            if overwrite:
                with open(fullname, "w") as file:
                    np.savetxt(file, image, fmt=format)
                    # messagebox.showinfo("Save", "File saved successfully.")
            else:
                self.isStop = True
        else:
            dir_name = os.path.dirname(os.path.abspath(fullname))
            # Path(dir_name).mkdir(parents=True, exist_ok=True)
            with open(fullname, "w") as file:
                np.savetxt(file, image, fmt=format)
                # messagebox.showinfo("Save", "File saved successfully.")
        return


    def show_folder_dialog(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.startpath = folder_path
        if self.startpath:
            if (self.startpath.find(str(date.today())) > 0):
                self.ui.folder_edit.setText(self.startpath + "/")
            else:
                self.ui.folder_edit.setText(self.startpath + "/" + str(date.today()) + "/")
            self.folder_path = self.ui.folder_edit.text()

    def stop_button_clicked(self):
        print("Stopped")
        self.isStop = True
        self.enableButtons(True)
        self.update_frame()
        
    def Snap_button_pressed(self):
        self.take_images()
        self.update_frame()

    def SetRef_button_pressed(self):
        if (self.Ref == self.img).all():
            return
        self.Ref = self.img.copy()
        self.update_frame()

    def DelRef_button_pressed(self):
        self.Ref = np.zeros(self.img.shape).astype(np.int32)
        self.ui.Diff_view.setImage(self.Ref)
        self.update_frame()

    def enableButtons(self, value):
        self.ui.StartButton.setEnabled(value)
        self.ui.Take_snap_button.setEnabled(value)
            
    def SnapLoop(self, callback):
        while not self.isStop:
            self.take_images()
            callback()
            time.sleep(0.025)

    def start_button_press(self):
        # start main measurements
        if not self.isStop:
            return
        # prepare measurements
        self.isStop = False
        self.enableButtons(False)
        self.Ref = np.zeros(self.img.shape).astype(np.int32)
        self.ui.Diff_view.setImage(self.Ref)
        self.set_camera_settings()

        base_folder = self.ui.folder_edit.text()
        folder = base_folder
        filename = self.ui.FileName.text()
        self.fullpathname = os.path.join(folder, filename + ".hdf5")

        Snapper = Worker(self.SnapLoop)
        Snapper.signals.progress.connect(self.update)
        Snapper.signals.finished.connect(self.finish)
        self.threadpool.start(Snapper)

    def finish(self):
        self.stop_button_clicked()

    def On_app_quit(self):
        self.stop_button_clicked()
        self.threadpool.waitForDone()
        quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    mainWindow = MainForm()
    app.aboutToQuit.connect(mainWindow.On_app_quit)
    sys.exit(app.exec())
