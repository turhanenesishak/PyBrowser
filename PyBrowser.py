from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTabWidget, QPushButton, QToolBar, QAction
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import sys

class BrowserTab(QWebEngineView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setUrl(QUrl("https://www.google.com"))

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyBrowser")
        self.resize(1200, 800)
        self.tab_widget = QTabWidget()
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.close_tab)
        self.add_new_tab()
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tab_widget)
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
        self.toolbar = QToolBar("Toolbar")
        self.addToolBar(self.toolbar)
        back_action = QAction("Back", self)
        back_action.triggered.connect(self.go_back)
        self.toolbar.addAction(back_action)
        forward_action = QAction("Forward", self)
        forward_action.triggered.connect(self.go_forward)
        self.toolbar.addAction(forward_action)
        refresh_action = QAction("Reload", self)
        refresh_action.triggered.connect(self.reload_page)
        self.toolbar.addAction(refresh_action)
        new_tab_action = QAction("New Tab", self)
        new_tab_action.triggered.connect(self.add_new_tab)
        self.toolbar.addAction(new_tab_action)

    def add_new_tab(self, url=None):
        browser_tab = BrowserTab()
        if url:
            browser_tab.setUrl(QUrl(url))
        self.tab_widget.addTab(browser_tab, "New Tab")
        self.tab_widget.setCurrentWidget(browser_tab)

    def update_tab_title(self, browser_tab, url):
        title = browser_tab.title() if browser_tab.title() else url.toString()
        index = self.tab_widget.indexOf(browser_tab)
        if index != -1:
            self.tab_widget.setTabText(index, title)

    def close_tab(self, index):
        if self.tab_widget.count() > 1:
            self.tab_widget.removeTab(index)

    def current_browser(self):
        return self.tab_widget.currentWidget()

    def go_back(self):
        self.current_browser().back()

    def go_forward(self):
        self.current_browser().forward()

    def reload_page(self):
        self.current_browser().reload()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())
