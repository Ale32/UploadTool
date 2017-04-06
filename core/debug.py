__author__ = 'a.paoletti'

from PySide import QtGui


def show_info(msg):
    """
    Show an information message box.
    Use it for simple information (not alert or errors)

    Example: 'Script ends successfully'

    :param msg: string that represent message to show
    :return: None
    """
    parent_window = QtGui.QMainWindow()

    return QtGui.QMessageBox.information(
        parent_window,
        "Information",
        msg,
        QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel
    )


def show_warning(warning):
    """
    Show a warning message box.
    Use it for report warning at users.

    Example: 'Selection is empty: you MUST select items'

    :param warning: string that represent warning to show
    :return: None
    """
    parent_window = QtGui.QMainWindow()

    return QtGui.QMessageBox.warning(
        parent_window,
        "Warning",
        warning,
        QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel
    )


def show_error(error):
    """
    Show an error message box.
    Use it for report significant errors to users

    Example: 'Path not found'
    :param error: string that represent error to show
    :return: None
    """
    parent_window = QtGui.QMainWindow()

    return QtGui.QMessageBox.critical(
        parent_window,
        "Error",
        error,
        QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel
    )
