from arjuna import *

@test(drive_with=records(
        record(user=None, pwd=None),
        record(user="user", pwd="bitnami"),
))
def check_wp_login(request, data, wordpress):
    wordpress.login(user=data.user, pwd=data.pwd)
    wordpress.logout()