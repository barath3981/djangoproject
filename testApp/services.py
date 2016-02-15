from models import LoginTbl, EventMain, UsrProfile, RestapiKeys, RestapiAccess


def getAllEvents(emailid):
    allEvents = None
    try:
        allEvents = EventMain.objects.filter()
    except Exception, ex:
        raise ex
    return allEvents


def get_login(email, password):
    try:
        return LoginTbl.objects.get(emailid=email, password=password)
    except Exception, ex:
        return None


def getUserID(emailid):
    userRecord = UsrProfile.objects.get(host_email_addr=emailid)
    return userRecord.userid


def getAccessToken(userID):
    return RestapiKeys.objects.get(userid=userID)


def getToken(userid):
    return RestapiKeys.objects.get(userid=userid)


def getAppIDAndSecret(userID):
    return RestapiAccess.objects.get(userid=userID)


def save_data():
    login_tbl = LoginTbl()
    login_tbl.emailid = "ravikant@inviter.com"
    login_tbl.password = "ravikant"
    try:
        login_tbl.save()
    except Exception, ex:
        print "GOT ERROR WHILE SAVIMG %s " % ex
