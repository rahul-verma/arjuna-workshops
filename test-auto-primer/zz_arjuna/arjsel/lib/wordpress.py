from arjuna import *

class WordPress(GuiApp):

    def __init__(self):
        url = C("wp.login.url")
        super().__init__(url=url, gns_dir="wordpress")
        self.launch()

    def login(self, user=None, pwd=None):
        if user is None:
            user = C("wp.admin.name")
        if pwd is None:
            pwd = C("wp.admin.pwd")

        # Login
        self.gns.user.text = user
        self.gns.pwd.text = pwd
        self.gns.submit.click()
        self.gns.view_site

    def logout(self):
        url = C("wp.logout.url")
        self.go_to_url(url)
        self.gns.logout_confirm.click()
        self.gns.logout_msg

        self.quit()