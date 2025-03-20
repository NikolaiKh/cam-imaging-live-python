import sys
import os
import glob
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
import time
from datetime import datetime, date, timedelta
import h5py


# 2 next classes are for multithreading

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
        self.camera_init()
        self.set_camera_settings()
        self.take_images()
        self.Ref = np.zeros(self.img.shape).astype(np.int32)
        self.Diff = self.Ref
        self.image_count = 0

        # set functions for buttons
        self.ui.folderButton.clicked.connect(self.show_folder_dialog)
        self.ui.StopButton.clicked.connect(self.stop_button_clicked)
        self.ui.StartButton.clicked.connect(self.start_button_press)
        self.ui.save_Button.clicked.connect(self.save_images)
        self.ui.Take_snap_button.clicked.connect(self.snap_button_pressed)
        self.ui.SetCam_button.clicked.connect(self.set_camera_settings)
        self.ui.Set_Ref_button.clicked.connect(self.set_ref_button_pressed)
        self.ui.remove_ref_button.clicked.connect(self.del_ref_button_pressed)
        self.ui.SaveSettings_button.clicked.connect(self.save_settings)
        self.ui.LoadSettings_button.clicked.connect(self.load_settings)

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

    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_line = f'{timestamp}  {message}'
        self.ui.status_memo_PlainTextEdit.appendPlainText(new_line)
        print(new_line)

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


    def save_settings(self):
        # Save camera.params as np dictinary
        dictionary = self.camera.params
        dictionary["Folder"] = self.ui.folder_edit.text()
        dictionary["FileName"] = self.ui.FileName.text()
        np.save('cam_settings.npy', dictionary)
        self.log("Settings saved")

    def load_settings(self):
        # Load camera.params as np dictionary
        settings_file = 'cam_settings.npy'
        if os.path.exists(settings_file):
            dictionary = np.load(settings_file, allow_pickle='TRUE').item()
            if dictionary["Description"] == self.camera.get_camera_name():
                for key in dictionary.keys():
                    self.camera.set_property(key, dictionary[key])
                    self.log(f"{key} set to {dictionary[key]}")
            self.ui.gain_spinBox.setValue(int(dictionary["Gain"]))
            self.ui.ExpTime.setValue(float(dictionary["Exposure"]))
            self.set_camera_settings()
            # update folder and file_name
            self.ui.folder_edit.setText(dictionary["Folder"])
            self.ui.FileName.setText(dictionary["FileName"])
            self.log("Settings loaded")
        else:
            self.log("No saved setting. Use default settings")
        self.show_cam_parameters()


    def take_images(self):
        # self.log("Camera busy")
        # self.ui.status_memo_PlainTextEdit.update()
        self.img = self.camera.get_image().astype(np.int32).T   # int32 to save integers => save hard drive space
        # self.log("Camera ready")

    def set_camera_settings(self):
        exposure = self.ui.ExpTime.value()
        self.camera.set_exposure(exposure)
        binning = self.ui.binningComboBox.currentText()
        self.camera.set_binning(binning)
        gain = int(self.ui.gain_spinBox.value())
        self.camera.set_gain(gain)
        # mode = self.ui.pModeComboBox.currentText()
        # self.camera.set_PMode(mode)   # Normal mode closes the program sometimes
        # ReadoutRate = self.ui.ROrateComboBox.currentText()
        # self.camera.set_ReadoutRate(ReadoutRate)
        # show camera parameters
        self.show_cam_parameters()

    def show_cam_parameters(self):
        cam_params = self.camera.params
        # show camera parameters
        self.ui.cam_params_plainTextEdit.clear()
        for key, value in cam_params.items():
            self.ui.cam_params_plainTextEdit.appendPlainText(f"{key}: {value}")
        scrollbar = self.ui.cam_params_plainTextEdit.verticalScrollBar()
        scrollbar.setSliderPosition(0)

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
        self.Diff = image_data
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


    def file_exists_with_any_extension(self, directory, filename):
        # Use glob to find files with the given filename and any extension
        files = glob.glob(os.path.join(directory, f"{filename}.*"))
        return len(files) > 0

    def save_images(self):
        self.image_count += 1   # count saved images
        # save .dat files
        if self.ui.save_datFiles_checkBox.isChecked():
            if self.ui.saveRef_checkBox.isChecked():
                self.save_image2dat(widget=self.ui.Image_view)
            if self.ui.saveDiff_checkBox.isChecked():
                self.save_image2dat(widget=self.ui.Diff_view)

        # save in .h5 files
        if self.ui.save_h5Files_checkBox.isChecked():
            if self.ui.saveRef_checkBox.isChecked():
                return
                # self.save_image2h5(widget=self.ui.Image_view)
            if self.ui.saveDiff_checkBox.isChecked():
                return
                # self.save_image2h5(widget=self.ui.Diff_view)


    def get_minimum_dtype(self, min_value, max_value):
        if min_value >= 0:
            if max_value <= np.iinfo(np.uint8).max:
                return np.uint8
            elif max_value <= np.iinfo(np.uint16).max:
                return np.uint16
            elif max_value <= np.iinfo(np.uint32).max:
                return np.uint32
            else:
                return np.uint64
        else:
            if min_value >= np.iinfo(np.int8).min and max_value <= np.iinfo(np.int8).max:
                return np.int8
            elif min_value >= np.iinfo(np.int16).min and max_value <= np.iinfo(np.int16).max:
                return np.int16
            elif min_value >= np.iinfo(np.int32).min and max_value <= np.iinfo(np.int32).max:
                return np.int32
            else:
                return np.int64

    def save_image2h5(self, widget=None):
        if not widget:
            widget = self.ui.Image_view
            # saving one image from a widget
        folder = self.ui.folder_edit.text()
        if not os.path.isdir(folder):
            messagebox.showerror("Error", "Folder does not exist!")
            return
        filename = self.ui.FileName.text()
        # choose the options based on Ref / Diff input
        if widget == self.ui.Image_view:
            filename = "Ref_" + filename
            data2save = self.img
        else:
            filename = "Diff_" + filename
            data2save = self.Diff
        #   prepare the data
        new_dtype = self.get_minimum_dtype(np.min(data2save), np.max(data2save))
        data2save = data2save.astype(new_dtype)

        #   save the data
        fullname = os.path.join(folder, filename)
        with h5py.File(fullname+".h5", 'a') as f:
            image_count = '{:0>4}'.format(str(self.image_count))
            image_name = f"Image_{image_count}"
            # Save the image data with compression
            my_img = f.create_dataset(image_name, data=data2save, dtype=new_dtype, compression='gzip')

            # Add metadata as attributes
            # my_img.attrs['MetaData'] = self.camera.img_metadata
            # my_img.attrs = self.camera.params
            my_img.attrs['DateTime'] = datetime.now().replace(microsecond=0).isoformat()
            f.close()
        self.log(f".h5 updated successfully: {fullname}")


    def save_image2dat(self, widget=None):
        if not widget:
            widget = self.ui.Image_view
        # saving one image from a widget
        folder = self.ui.folder_edit.text()
        if not os.path.isdir(folder):
            messagebox.showerror("Error", "Folder does not exist!")
            return
        filename = self.ui.FileName.text()
        # choose the options based on Ref / Diff input
        if widget == self.ui.Image_view:
            filename = "Ref_" + filename
            data2save = self.img
        else:
            filename = "Diff_" + filename
            data2save = self.Diff
        new_dtype = self.get_minimum_dtype(np.min(data2save), np.max(data2save))
        data2save = data2save.astype(new_dtype)

        # save .dat and .png files
        if not filename:
            messagebox.showerror("Error", "Please enter a file name")
            return
        fullname = os.path.join(folder, filename)
        if self.file_exists_with_any_extension(folder, filename):
            overwrite = messagebox.askyesno('File already exists', f'File {filename} already exists. Overwrite?')
            if overwrite:
                # save image raw data to file
                np.savetxt(fullname + ".dat", data2save, fmt='%d')
                # save snapshot
                widget.export(fullname + ".png")
                # save cam_params and image metadata
                with open(fullname + ".meta", 'w') as file:
                    file.write("comments = { \n")
                    file.write(self.ui.comments_memo_PlainTextEdit.toPlainText())
                    file.write("} \n\n")
                    file.write("cam_params = {")
                    for k in sorted(self.camera.params.keys()):
                        file.write("'%s':'%s', \n" % (k, self.camera.params[k]))
                    file.write("} \n\n")
                    file.write("img_metadata = {")
                    for k in sorted(self.camera.img_metadata.keys()):
                        file.write("'%s':'%s', \n" % (k, self.camera.img_metadata[k]))
                self.log(f".dat overwrite successfully: {fullname}")
            else:
                self.isStop = True
        else:
            np.savetxt(fullname + ".dat", data2save, fmt='%d')
            widget.export(fullname + ".png")
            # save cam_params and image metadata
            with open(fullname + ".meta", 'w') as file:
                file.write("comments = { \n")
                file.write(self.ui.comments_memo_PlainTextEdit.toPlainText())
                file.write("} \n\n")
                file.write("cam_params = {")
                for k in sorted(self.camera.params.keys()):
                    file.write("'%s':'%s', \n" % (k, self.camera.params[k]))
                file.write("} \n\n")
                file.write("img_metadata = {")
                for k in sorted(self.camera.img_metadata.keys()):
                    file.write("'%s':'%s', \n" % (k, self.camera.img_metadata[k]))
                file.write("}")
            self.log(f".dat saved successfully: {fullname}")
        return


    def show_folder_dialog(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.ui.folder_edit.setText(folder_path + "/")
        self.folder_path = self.ui.folder_edit.text()


    def stop_button_clicked(self):
        print("Stopped")
        self.isStop = True
        self.enableButtons(True)
        self.update_frame()
        
    def snap_button_pressed(self):
        self.set_camera_settings()
        self.take_images()
        self.update_frame()

    def set_ref_button_pressed(self):
        if (self.Ref == self.img).all():
            return
        self.Ref = self.img.copy()
        self.update_frame()

    def del_ref_button_pressed(self):
        self.Ref = np.zeros(self.img.shape).astype(np.int32)
        self.ui.Diff_view.setImage(self.Ref)
        self.update_frame()

    def enableButtons(self, value):
        self.ui.StartButton.setEnabled(value)
        self.ui.Take_snap_button.setEnabled(value)
            
    def snap_loop(self, callback):
        while not self.isStop:
            self.take_images()
            callback()
            time.sleep(0.025)

    def start_button_press(self):
        self.set_camera_settings()
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

        Snapper = Worker(self.snap_loop)
        Snapper.signals.progress.connect(self.update_frame)
        Snapper.signals.finished.connect(self.finish)
        self.threadpool.start(Snapper)


    def finish(self):
        self.stop_button_clicked()

    def on_app_quit(self):
        self.stop_button_clicked()
        self.threadpool.waitForDone()
        quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    mainWindow = MainForm()
    app.aboutToQuit.connect(mainWindow.on_app_quit)
    sys.exit(app.exec())
