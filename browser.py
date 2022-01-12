import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://duckduckgo.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # Navigation bar
        navbar = QToolBar()
        self.addToolBar(navbar)
        # Back Button
        backButton = QAction('Back', self)
        backButton.triggered.connect(self.browser.back)
        navbar.addAction(backButton)
        # Forward Button
        forwardButton = QAction('Forward', self)
        forwardButton.triggered.connect(self.browser.forward)
        navbar.addAction(forwardButton)
        # Reload Button
        reloadButton = QAction('Reload', self)
        reloadButton.triggered.connect(self.browser.reload)
        navbar.addAction(reloadButton)
        # Home Button
        homeButton = QAction("Home", self)
        homeButton.triggered.connect(self.navigate_home)
        navbar.addAction(homeButton)
        # Adding search bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())
        
    def navigate_home(self):
        self.browser.setUrl(QUrl('https://duckduckgo.com'))

app = QApplication(sys.argv)
QApplication.setApplicationName('My Browser')
window = MainWindow()
app.exec_()