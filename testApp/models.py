# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AnalyticsDetail(models.Model):
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    eventid = models.IntegerField(db_column='EVENTID', primary_key=True)  # Field name made lowercase.
    event_type = models.CharField(db_column='EVENT_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    share_url = models.CharField(db_column='SHARE_URL', max_length=256, blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='EMAILID', max_length=100)  # Field name made lowercase.
    fb_likes = models.IntegerField(db_column='FB_LIKES', blank=True, null=True)  # Field name made lowercase.
    fb_shares = models.IntegerField(db_column='FB_SHARES', blank=True, null=True)  # Field name made lowercase.
    fb_comments = models.IntegerField(db_column='FB_COMMENTS', blank=True, null=True)  # Field name made lowercase.
    tw_tweets = models.IntegerField(db_column='TW_TWEETS', blank=True, null=True)  # Field name made lowercase.
    g_plus_ones = models.IntegerField(db_column='G_PLUS_ONES', blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ANALYTICS_DETAIL'


class AnalyticsMain(models.Model):
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    eventid = models.IntegerField(db_column='EVENTID', primary_key=True)  # Field name made lowercase.
    share_url = models.CharField(db_column='SHARE_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='EMAILID', max_length=100)  # Field name made lowercase.
    fb_likes = models.IntegerField(db_column='FB_LIKES', blank=True, null=True)  # Field name made lowercase.
    fb_shares = models.IntegerField(db_column='FB_SHARES', blank=True, null=True)  # Field name made lowercase.
    fb_comments = models.IntegerField(db_column='FB_COMMENTS', blank=True, null=True)  # Field name made lowercase.
    tw_tweets = models.IntegerField(db_column='TW_TWEETS', blank=True, null=True)  # Field name made lowercase.
    g_plus_ones = models.IntegerField(db_column='G_PLUS_ONES', blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ANALYTICS_MAIN'


class AnalyticsSummary(models.Model):
    userid = models.IntegerField(db_column='USERID', blank=True, null=True)  # Field name made lowercase.
    eventid = models.IntegerField(db_column='EVENTID', primary_key=True)  # Field name made lowercase.
    event_title = models.CharField(db_column='EVENT_TITLE', max_length=100)  # Field name made lowercase.
    host_name = models.CharField(db_column='HOST_NAME', max_length=100)  # Field name made lowercase.
    sender_emailid = models.CharField(db_column='SENDER_EMAILID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sent_count = models.IntegerField(db_column='SENT_COUNT', blank=True, null=True)  # Field name made lowercase.
    delivery_count = models.IntegerField(db_column='DELIVERY_COUNT', blank=True, null=True)  # Field name made lowercase.
    uniq_open_count = models.IntegerField(db_column='UNIQ_OPEN_COUNT', blank=True, null=True)  # Field name made lowercase.
    total_open_count = models.IntegerField(db_column='TOTAL_OPEN_COUNT', blank=True, null=True)  # Field name made lowercase.
    uniq_click_count = models.IntegerField(db_column='UNIQ_CLICK_COUNT', blank=True, null=True)  # Field name made lowercase.
    total_click_count = models.IntegerField(db_column='TOTAL_CLICK_COUNT', blank=True, null=True)  # Field name made lowercase.
    spam_count = models.IntegerField(db_column='SPAM_COUNT', blank=True, null=True)  # Field name made lowercase.
    unsubscribe_count = models.IntegerField(db_column='UNSUBSCRIBE_COUNT', blank=True, null=True)  # Field name made lowercase.
    soft_bounce_count = models.IntegerField(db_column='SOFT_BOUNCE_COUNT', blank=True, null=True)  # Field name made lowercase.
    hard_bounce_count = models.IntegerField(db_column='HARD_BOUNCE_COUNT', blank=True, null=True)  # Field name made lowercase.
    sent_dttm = models.DateTimeField(db_column='SENT_DTTM', blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ANALYTICS_SUMMARY'


class ApnsDevices(models.Model):
    pid = models.AutoField(db_column='PID', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    emailid = models.CharField(db_column='EMAILID', max_length=250)  # Field name made lowercase.
    app_name = models.CharField(db_column='APP_NAME', max_length=255)  # Field name made lowercase.
    app_version = models.CharField(db_column='APP_VERSION', max_length=25)  # Field name made lowercase.
    device_token = models.CharField(db_column='DEVICE_TOKEN', max_length=64)  # Field name made lowercase.
    device_name = models.CharField(db_column='DEVICE_NAME', max_length=255)  # Field name made lowercase.
    device_model = models.CharField(db_column='DEVICE_MODEL', max_length=100)  # Field name made lowercase.
    device_version = models.CharField(db_column='DEVICE_VERSION', max_length=25)  # Field name made lowercase.
    device_status = models.CharField(db_column='DEVICE_STATUS', max_length=1)  # Field name made lowercase.
    development = models.CharField(db_column='DEVELOPMENT', max_length=10)  # Field name made lowercase.
    create_dttm = models.DateTimeField(db_column='CREATE_DTTM')  # Field name made lowercase.
    last_login_dttm = models.DateTimeField(db_column='LAST_LOGIN_DTTM')  # Field name made lowercase.
    notification_alert = models.CharField(db_column='NOTIFICATION_ALERT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    inwiter_alert = models.CharField(db_column='INWITER_ALERT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    push_badge = models.CharField(db_column='PUSH_BADGE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    push_sound = models.CharField(db_column='PUSH_SOUND', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APNS_DEVICES'


class CntlPaymentPlans(models.Model):
    seqid = models.AutoField(db_column='SEQID', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='USERID', blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='EMAILID', max_length=100)  # Field name made lowercase.
    payment_type = models.CharField(db_column='PAYMENT_TYPE', max_length=2)  # Field name made lowercase.
    remaining_events_count = models.IntegerField(db_column='REMAINING_EVENTS_COUNT', blank=True, null=True)  # Field name made lowercase.
    customer_limit = models.IntegerField(db_column='CUSTOMER_LIMIT', blank=True, null=True)  # Field name made lowercase.
    video_length = models.CharField(db_column='VIDEO_LENGTH', max_length=45, blank=True, null=True)  # Field name made lowercase.
    plan_amount = models.FloatField(db_column='PLAN_AMOUNT')  # Field name made lowercase.
    promotion_cd = models.CharField(db_column='PROMOTION_CD', max_length=10)  # Field name made lowercase.
    create_dt = models.DateField(db_column='CREATE_DT')  # Field name made lowercase.
    expire_dt = models.DateField(db_column='EXPIRE_DT')  # Field name made lowercase.
    last_upd_dttm = models.DateTimeField(db_column='LAST_UPD_DTTM')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CNTL_PAYMENT_PLANS'


class CntlPromotionCodes(models.Model):
    seqid = models.AutoField(db_column='SEQID', primary_key=True)  # Field name made lowercase.
    promotion_cd = models.CharField(db_column='PROMOTION_CD', max_length=10)  # Field name made lowercase.
    discount_percentage = models.IntegerField(db_column='DISCOUNT_PERCENTAGE')  # Field name made lowercase.
    total_users = models.IntegerField(db_column='TOTAL_USERS')  # Field name made lowercase.
    used_users = models.IntegerField(db_column='USED_USERS')  # Field name made lowercase.
    payment_type = models.CharField(db_column='PAYMENT_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    app_type = models.CharField(db_column='APP_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    create_dt = models.DateField(db_column='CREATE_DT')  # Field name made lowercase.
    expire_dt = models.DateField(db_column='EXPIRE_DT')  # Field name made lowercase.
    last_upd_dttm = models.DateTimeField(db_column='LAST_UPD_DTTM')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CNTL_PROMOTION_CODES'


class CrmAdmComments(models.Model):
    seqid = models.AutoField(db_column='SEQID', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    eventid = models.IntegerField(db_column='EVENTID')  # Field name made lowercase.
    admin_emailid = models.CharField(db_column='ADMIN_EMAILID', max_length=45)  # Field name made lowercase.
    comments = models.CharField(db_column='COMMENTS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lastupddttm = models.DateTimeField(db_column='LASTUPDDTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CRM_ADM_COMMENTS'


class CrmEditLogs(models.Model):
    seqid = models.AutoField(db_column='SEQID', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='USERID', blank=True, null=True)  # Field name made lowercase.
    crm_user_name = models.CharField(db_column='CRM_USER_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='ACTION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    update_dttm = models.DateTimeField(db_column='UPDATE_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CRM_EDIT_LOGS'


class EmailClickAnalytics(models.Model):
    seq_id = models.AutoField(db_column='SEQ_ID', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='USERID', blank=True, null=True)  # Field name made lowercase.
    eventid = models.IntegerField(db_column='EVENTID', blank=True, null=True)  # Field name made lowercase.
    messageid = models.CharField(db_column='MESSAGEID', max_length=100)  # Field name made lowercase.
    click_url = models.CharField(db_column='CLICK_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    total_click_count = models.IntegerField(db_column='TOTAL_CLICK_COUNT', blank=True, null=True)  # Field name made lowercase.
    uniq_click_count = models.IntegerField(db_column='UNIQ_CLICK_COUNT', blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EMAIL_CLICK_ANALYTICS'


class EmailClickTracking(models.Model):
    seq_id = models.AutoField(db_column='SEQ_ID', primary_key=True)  # Field name made lowercase.
    messageid = models.CharField(db_column='MESSAGEID', max_length=45)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='TIMESTAMP', blank=True, null=True)  # Field name made lowercase.
    user_agent = models.CharField(db_column='USER_AGENT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=45, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=2083, blank=True, null=True)  # Field name made lowercase.
    event_json = models.TextField(db_column='EVENT_JSON', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EMAIL_CLICK_TRACKING'


class EmailClientAnalytics(models.Model):
    seq_id = models.AutoField(db_column='SEQ_ID', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='USERID', blank=True, null=True)  # Field name made lowercase.
    eventid = models.IntegerField(db_column='EVENTID', blank=True, null=True)  # Field name made lowercase.
    messageid = models.CharField(db_column='MESSAGEID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    client_agent = models.CharField(db_column='CLIENT_AGENT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    client_agent_ver = models.CharField(db_column='CLIENT_AGENT_VER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    client_os = models.CharField(db_column='CLIENT_OS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    client_os_ver = models.CharField(db_column='CLIENT_OS_VER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EMAIL_CLIENT_ANALYTICS'


class EmailOpenTracking(models.Model):
    seq_id = models.AutoField(db_column='SEQ_ID', primary_key=True)  # Field name made lowercase.
    messageid = models.CharField(db_column='MESSAGEID', max_length=45)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='TIMESTAMP', blank=True, null=True)  # Field name made lowercase.
    user_agent = models.CharField(db_column='USER_AGENT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=45, blank=True, null=True)  # Field name made lowercase.
    event_json = models.TextField(db_column='EVENT_JSON', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EMAIL_OPEN_TRACKING'


class EmailSuspendList(models.Model):
    susp_seqid = models.AutoField(db_column='SUSP_SEQID', primary_key=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='EMAILID', max_length=255)  # Field name made lowercase.
    messageid = models.CharField(db_column='MESSAGEID', max_length=126)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EMAIL_SUSPEND_LIST'


class EmailTracking(models.Model):
    msg_seq = models.AutoField(db_column='MSG_SEQ', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='USERID', blank=True, null=True)  # Field name made lowercase.
    eventid = models.IntegerField(db_column='EVENTID', blank=True, null=True)  # Field name made lowercase.
    transactionid = models.IntegerField(db_column='TRANSACTIONID', blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='EMAILID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sender_emailid = models.CharField(db_column='SENDER_EMAILID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    messageid = models.CharField(db_column='MESSAGEID', max_length=126)  # Field name made lowercase.
    msg_type = models.CharField(db_column='MSG_TYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    delivery_status = models.CharField(db_column='DELIVERY_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    open_status = models.CharField(db_column='OPEN_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    spam_status = models.CharField(db_column='SPAM_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    unsubscribe_status = models.CharField(db_column='UNSUBSCRIBE_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    soft_bounce_status = models.CharField(db_column='SOFT_BOUNCE_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    hard_bounce_status = models.CharField(db_column='HARD_BOUNCE_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    bounce_description = models.TextField(db_column='BOUNCE_DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    bounce_message = models.TextField(db_column='BOUNCE_MESSAGE', blank=True, null=True)  # Field name made lowercase.
    user_agent = models.CharField(db_column='USER_AGENT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ip_address = models.CharField(db_column='IP_ADDRESS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    event_json = models.TextField(db_column='EVENT_JSON', blank=True, null=True)  # Field name made lowercase.
    sent_dttm = models.DateTimeField(db_column='SENT_DTTM', blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EMAIL_TRACKING'


class EmailVerificationList(models.Model):
    seq_id = models.AutoField(db_column='SEQ_ID', primary_key=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='EMAILID', max_length=255)  # Field name made lowercase.
    messageid = models.CharField(db_column='MESSAGEID', max_length=126, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EMAIL_VERIFICATION_LIST'


class EventCheckIn(models.Model):
    check_in_id = models.AutoField(db_column='CHECK_IN_ID', primary_key=True)  # Field name made lowercase.
    eventid = models.IntegerField(db_column='EVENTID', blank=True, null=True)  # Field name made lowercase.
    transactionid = models.IntegerField(db_column='TRANSACTIONID', blank=True, null=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='FIRST_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='LAST_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='EMAILID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    invited_by = models.CharField(db_column='INVITED_BY', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rsvp_status = models.CharField(db_column='RSVP_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    guests_nbr = models.IntegerField(db_column='GUESTS_NBR', blank=True, null=True)  # Field name made lowercase.
    kids_nbr = models.IntegerField(db_column='KIDS_NBR', blank=True, null=True)  # Field name made lowercase.
    check_in_status = models.CharField(db_column='CHECK_IN_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EVENT_CHECK_IN'


class EventGuest(models.Model):
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    eventid = models.IntegerField(db_column='EVENTID')  # Field name made lowercase.
    transactionid = models.AutoField(db_column='TRANSACTIONID', primary_key=True)  # Field name made lowercase.
    contactid = models.IntegerField(db_column='CONTACTID')  # Field name made lowercase.
    first_name = models.CharField(db_column='FIRST_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='LAST_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    other_guest_names = models.TextField(db_column='OTHER_GUEST_NAMES', blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='EMAILID', max_length=100)  # Field name made lowercase.
    phone_nbr = models.CharField(db_column='PHONE_NBR', max_length=12, blank=True, null=True)  # Field name made lowercase.
    batch_nbr = models.CharField(db_column='BATCH_NBR', max_length=12, blank=True, null=True)  # Field name made lowercase.
    email_sent = models.CharField(db_column='EMAIL_SENT', max_length=1)  # Field name made lowercase.
    email_sent_dttm = models.DateTimeField(db_column='EMAIL_SENT_DTTM')  # Field name made lowercase.
    validate_email = models.CharField(db_column='VALIDATE_EMAIL', max_length=1, blank=True, null=True)  # Field name made lowercase.
    guest_view = models.CharField(db_column='GUEST_VIEW', max_length=1)  # Field name made lowercase.
    guest_view_dttm = models.DateTimeField(db_column='GUEST_VIEW_DTTM', blank=True, null=True)  # Field name made lowercase.
    rsvp_status = models.CharField(db_column='RSVP_STATUS', max_length=1)  # Field name made lowercase.
    guests_nbr = models.IntegerField(db_column='GUESTS_NBR', blank=True, null=True)  # Field name made lowercase.
    kids_nbr = models.IntegerField(db_column='KIDS_NBR', blank=True, null=True)  # Field name made lowercase.
    selected_poll_options = models.TextField(db_column='SELECTED_POLL_OPTIONS', blank=True, null=True)  # Field name made lowercase.
    selected_poll_options_json = models.TextField(db_column='SELECTED_POLL_OPTIONS_JSON', blank=True, null=True)  # Field name made lowercase.
    rsvp_dttm = models.DateTimeField(db_column='RSVP_DTTM', blank=True, null=True)  # Field name made lowercase.
    invite_fwd_by = models.CharField(db_column='INVITE_FWD_BY', max_length=100, blank=True, null=True)  # Field name made lowercase.
    is_user = models.CharField(db_column='IS_USER', max_length=1)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=256, blank=True, null=True)  # Field name made lowercase.
    received_status = models.CharField(db_column='RECEIVED_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    msg_to_host = models.CharField(db_column='MSG_TO_HOST', max_length=255, blank=True, null=True)  # Field name made lowercase.
    apns_sent = models.CharField(db_column='APNS_SENT', max_length=1)  # Field name made lowercase.
    celery_job_id = models.CharField(db_column='CELERY_JOB_ID', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EVENT_GUEST'


class EventGuestComment(models.Model):
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    eventid = models.IntegerField(db_column='EVENTID')  # Field name made lowercase.
    comment = models.CharField(db_column='COMMENT', max_length=255)  # Field name made lowercase.
    comment_dttm = models.DateTimeField(db_column='COMMENT_DTTM')  # Field name made lowercase.
    emailid = models.CharField(db_column='EMAILID', max_length=100)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EVENT_GUEST_COMMENT'


class EventJobDefn(models.Model):
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    eventid = models.IntegerField(db_column='EVENTID')  # Field name made lowercase.
    job_defnid = models.AutoField(db_column='JOB_DEFNID', primary_key=True)  # Field name made lowercase.
    timezone = models.CharField(db_column='TIMEZONE', max_length=255)  # Field name made lowercase.
    schd_option = models.CharField(db_column='SCHD_OPTION', max_length=1)  # Field name made lowercase.
    schd_status = models.CharField(db_column='SCHD_STATUS', max_length=2)  # Field name made lowercase.
    recur_start_dt = models.DateField(db_column='RECUR_START_DT', blank=True, null=True)  # Field name made lowercase.
    recur_end_dt = models.DateField(db_column='RECUR_END_DT', blank=True, null=True)  # Field name made lowercase.
    recur_freq = models.CharField(db_column='RECUR_FREQ', max_length=45, blank=True, null=True)  # Field name made lowercase.
    send_mail_in_days = models.IntegerField(db_column='SEND_MAIl_IN_DAYS', blank=True, null=True)  # Field name made lowercase.
    send_reminder_in_days = models.IntegerField(db_column='SEND_REMINDER_IN_DAYS', blank=True, null=True)  # Field name made lowercase.
    recur_descr = models.CharField(db_column='RECUR_DESCR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    recur_groupid = models.IntegerField(db_column='RECUR_GROUPID', blank=True, null=True)  # Field name made lowercase.
    create_dttm = models.DateTimeField(db_column='CREATE_DTTM')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EVENT_JOB_DEFN'


class EventJobReqst(models.Model):
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    eventid = models.IntegerField(db_column='EVENTID')  # Field name made lowercase.
    job_defnid = models.IntegerField(db_column='JOB_DEFNID')  # Field name made lowercase.
    job_reqstid = models.AutoField(db_column='JOB_REQSTID', primary_key=True)  # Field name made lowercase.
    schd_option = models.CharField(db_column='SCHD_OPTION', max_length=1)  # Field name made lowercase.
    emailid = models.CharField(db_column='EMAILID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    schedule_dt = models.DateField(db_column='SCHEDULE_DT')  # Field name made lowercase.
    schedule_tm = models.TimeField(db_column='SCHEDULE_TM')  # Field name made lowercase.
    event_start_dt = models.DateField(db_column='EVENT_START_DT')  # Field name made lowercase.
    event_end_dt = models.DateField(db_column='EVENT_END_DT')  # Field name made lowercase.
    event_start_tm = models.TimeField(db_column='EVENT_START_TM')  # Field name made lowercase.
    event_end_tm = models.TimeField(db_column='EVENT_END_TM')  # Field name made lowercase.
    schd_status = models.CharField(db_column='SCHD_STATUS', max_length=2)  # Field name made lowercase.
    create_dttm = models.DateTimeField(db_column='CREATE_DTTM', blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.
    reminder_dt = models.DateField(db_column='REMINDER_DT', blank=True, null=True)  # Field name made lowercase.
    reminder_tm = models.TimeField(db_column='REMINDER_TM', blank=True, null=True)  # Field name made lowercase.
    celery_jobid = models.CharField(db_column='CELERY_JOBID', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EVENT_JOB_REQST'


class EventMain(models.Model):
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    eventid = models.AutoField(db_column='EVENTID', primary_key=True)  # Field name made lowercase.
    rsvp_need = models.CharField(db_column='RSVP_NEED', max_length=1)  # Field name made lowercase.
    event_type = models.CharField(db_column='EVENT_TYPE', max_length=1)  # Field name made lowercase.
    event_category = models.CharField(db_column='EVENT_CATEGORY', max_length=30)  # Field name made lowercase.
    is_public = models.CharField(db_column='IS_PUBLIC', max_length=1)  # Field name made lowercase.
    event_status = models.CharField(db_column='EVENT_STATUS', max_length=2)  # Field name made lowercase.
    event_title = models.CharField(db_column='EVENT_TITLE', max_length=100)  # Field name made lowercase.
    event_descr = models.TextField(db_column='EVENT_DESCR')  # Field name made lowercase.
    event_start_dt = models.DateField(db_column='EVENT_START_DT')  # Field name made lowercase.
    event_end_dt = models.DateField(db_column='EVENT_END_DT', blank=True, null=True)  # Field name made lowercase.
    event_start_tm = models.TimeField(db_column='EVENT_START_TM')  # Field name made lowercase.
    event_end_tm = models.TimeField(db_column='EVENT_END_TM', blank=True, null=True)  # Field name made lowercase.
    timezone = models.CharField(db_column='TIMEZONE', max_length=255)  # Field name made lowercase.
    host_name = models.CharField(db_column='HOST_NAME', max_length=100)  # Field name made lowercase.
    event_host_photo_url = models.CharField(db_column='EVENT_HOST_PHOTO_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    host_email = models.CharField(db_column='HOST_EMAIL', max_length=100)  # Field name made lowercase.
    host_phone = models.CharField(db_column='HOST_PHONE', max_length=12)  # Field name made lowercase.
    rsvp_email = models.CharField(db_column='RSVP_EMAIL', max_length=100)  # Field name made lowercase.
    doing_business_as = models.CharField(db_column='DOING_BUSINESS_AS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    venue = models.CharField(db_column='VENUE', max_length=100)  # Field name made lowercase.
    event_hash_tag = models.CharField(db_column='EVENT_HASH_TAG', max_length=30, blank=True, null=True)  # Field name made lowercase.
    personalized_url = models.CharField(db_column='PERSONALIZED_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    session_id = models.CharField(db_column='SESSION_ID', max_length=12)  # Field name made lowercase.
    schd_option = models.CharField(db_column='SCHD_OPTION', max_length=1)  # Field name made lowercase.
    job_defnid = models.IntegerField(db_column='JOB_DEFNID', blank=True, null=True)  # Field name made lowercase.
    job_reqstid = models.IntegerField(db_column='JOB_REQSTID', blank=True, null=True)  # Field name made lowercase.
    schedule_dt = models.DateField(db_column='SCHEDULE_DT')  # Field name made lowercase.
    schedule_tm = models.TimeField(db_column='SCHEDULE_TM')  # Field name made lowercase.
    sent_dttm = models.DateTimeField(db_column='SENT_DTTM', blank=True, null=True)  # Field name made lowercase.
    create_final_video = models.CharField(db_column='CREATE_FINAL_VIDEO', max_length=1)  # Field name made lowercase.
    event_json_string = models.TextField(db_column='EVENT_JSON_STRING', blank=True, null=True)  # Field name made lowercase.
    final_video_file = models.CharField(db_column='FINAL_VIDEO_FILE', max_length=100)  # Field name made lowercase.
    video_thumb_file = models.CharField(db_column='VIDEO_THUMB_FILE', max_length=100)  # Field name made lowercase.
    email_thumb_file = models.CharField(db_column='EMAIL_THUMB_FILE', max_length=100)  # Field name made lowercase.
    save_draft_count = models.IntegerField(db_column='SAVE_DRAFT_COUNT', blank=True, null=True)  # Field name made lowercase.
    background_image = models.CharField(db_column='BACKGROUND_IMAGE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    push_notification = models.CharField(db_column='PUSH_NOTIFICATION', max_length=1)  # Field name made lowercase.
    apns_status = models.CharField(db_column='APNS_STATUS', max_length=1)  # Field name made lowercase.
    lang_cd = models.CharField(db_column='LANG_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    browser_os = models.CharField(db_column='BROWSER_OS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    app_type = models.CharField(db_column='APP_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fb_share = models.CharField(db_column='FB_SHARE', max_length=1)  # Field name made lowercase.
    fb_share_status = models.CharField(db_column='FB_SHARE_STATUS', max_length=1)  # Field name made lowercase.
    fb_privacy_obj = models.TextField(db_column='FB_PRIVACY_OBJ', blank=True, null=True)  # Field name made lowercase.
    fb_post_id = models.CharField(db_column='FB_POST_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tw_share = models.CharField(db_column='TW_SHARE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tw_share_status = models.CharField(db_column='TW_SHARE_STATUS', max_length=1)  # Field name made lowercase.
    share_url = models.CharField(db_column='SHARE_URL', max_length=256, blank=True, null=True)  # Field name made lowercase.
    create_dttm = models.DateTimeField(db_column='CREATE_DTTM')  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM')  # Field name made lowercase.
    celery_jobid = models.CharField(db_column='CELERY_JOBID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    from_email_verified = models.CharField(db_column='FROM_EMAIL_VERIFIED', max_length=1, blank=True, null=True)  # Field name made lowercase.
    from_email_addr = models.CharField(db_column='FROM_EMAIL_ADDR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    guest_template_id = models.CharField(db_column='GUEST_TEMPLATE_ID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    is_custom_email_tpl = models.CharField(db_column='IS_CUSTOM_EMAIL_TPL', max_length=1, blank=True, null=True)  # Field name made lowercase.
    email_template_name = models.CharField(db_column='EMAIL_TEMPLATE_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    is_custom_guest_tpl = models.CharField(db_column='IS_CUSTOM_GUEST_TPL', max_length=1, blank=True, null=True)  # Field name made lowercase.
    guest_template_name = models.CharField(db_column='GUEST_TEMPLATE_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email_subject_verified = models.CharField(db_column='EMAIL_SUBJECT_VERIFIED', max_length=1, blank=True, null=True)  # Field name made lowercase.
    email_subject = models.CharField(db_column='EMAIL_SUBJECT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customer_limit = models.IntegerField(db_column='CUSTOMER_LIMIT', blank=True, null=True)  # Field name made lowercase.
    video_length = models.CharField(db_column='VIDEO_LENGTH', max_length=45, blank=True, null=True)  # Field name made lowercase.
    payment_type = models.CharField(db_column='PAYMENT_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EVENT_MAIN'


class EventReminder(models.Model):
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    eventid = models.IntegerField(db_column='EVENTID', primary_key=True)  # Field name made lowercase.
    rsvp_status = models.CharField(db_column='RSVP_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reminder_dt = models.DateField(db_column='REMINDER_DT')  # Field name made lowercase.
    reminder_tm = models.TimeField(db_column='REMINDER_TM')  # Field name made lowercase.
    reminder_descr = models.CharField(db_column='REMINDER_DESCR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reminder_status = models.CharField(db_column='REMINDER_STATUS', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EVENT_REMINDER'


class EventRsvpPoll(models.Model):
    seq_id = models.AutoField(db_column='SEQ_ID', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    eventid = models.IntegerField(db_column='EVENTID')  # Field name made lowercase.
    transactionid = models.IntegerField(db_column='TRANSACTIONID')  # Field name made lowercase.
    questionid = models.IntegerField(db_column='QUESTIONID')  # Field name made lowercase.
    poll_option1 = models.CharField(db_column='POLL_OPTION1', max_length=1, blank=True, null=True)  # Field name made lowercase.
    poll_option2 = models.CharField(db_column='POLL_OPTION2', max_length=1, blank=True, null=True)  # Field name made lowercase.
    poll_option3 = models.CharField(db_column='POLL_OPTION3', max_length=1, blank=True, null=True)  # Field name made lowercase.
    poll_option4 = models.CharField(db_column='POLL_OPTION4', max_length=1, blank=True, null=True)  # Field name made lowercase.
    poll_option5 = models.CharField(db_column='POLL_OPTION5', max_length=1, blank=True, null=True)  # Field name made lowercase.
    poll_option6 = models.CharField(db_column='POLL_OPTION6', max_length=1, blank=True, null=True)  # Field name made lowercase.
    poll_option7 = models.CharField(db_column='POLL_OPTION7', max_length=1, blank=True, null=True)  # Field name made lowercase.
    poll_option8 = models.CharField(db_column='POLL_OPTION8', max_length=1, blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EVENT_RSVP_POLL'


class EventRsvpReport(models.Model):
    seqid = models.AutoField(db_column='SEQID', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    eventid = models.IntegerField(db_column='EVENTID')  # Field name made lowercase.
    report_type = models.CharField(db_column='REPORT_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    report_status = models.CharField(db_column='REPORT_STATUS', max_length=2)  # Field name made lowercase.
    host_emailid = models.CharField(db_column='HOST_EMAILID', max_length=100)  # Field name made lowercase.
    other_emailid = models.CharField(db_column='OTHER_EMAILID', max_length=100)  # Field name made lowercase.
    report_start_dt = models.DateTimeField(db_column='REPORT_START_DT')  # Field name made lowercase.
    report_end_dt = models.DateTimeField(db_column='REPORT_END_DT')  # Field name made lowercase.
    report_format = models.CharField(db_column='REPORT_FORMAT', max_length=2)  # Field name made lowercase.
    report_freq = models.CharField(db_column='REPORT_FREQ', max_length=10)  # Field name made lowercase.
    sort_order = models.CharField(db_column='SORT_ORDER', max_length=2)  # Field name made lowercase.
    report_last_sent_dttm = models.DateTimeField(db_column='REPORT_LAST_SENT_DTTM')  # Field name made lowercase.
    report_next_sch_dttm = models.DateTimeField(db_column='REPORT_NEXT_SCH_DTTM')  # Field name made lowercase.
    time_zone = models.CharField(db_column='TIME_ZONE', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EVENT_RSVP_REPORT'


class EventSettings(models.Model):
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    eventid = models.IntegerField(db_column='EVENTID', primary_key=True)  # Field name made lowercase.
    notify_rsvp = models.CharField(db_column='NOTIFY_RSVP', max_length=1)  # Field name made lowercase.
    notify_guest_comment = models.CharField(db_column='NOTIFY_GUEST_COMMENT', max_length=1)  # Field name made lowercase.
    notify_guest_view = models.CharField(db_column='NOTIFY_GUEST_VIEW', max_length=1)  # Field name made lowercase.
    hide_host_logo = models.CharField(db_column='HIDE_HOST_LOGO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    hide_comments = models.CharField(db_column='HIDE_COMMENTS', max_length=1)  # Field name made lowercase.
    hide_guest_list = models.CharField(db_column='HIDE_GUEST_LIST', max_length=1)  # Field name made lowercase.
    total_guests = models.IntegerField(db_column='TOTAL_GUESTS')  # Field name made lowercase.
    allow_kids = models.CharField(db_column='ALLOW_KIDS', max_length=1)  # Field name made lowercase.
    allow_adults = models.CharField(db_column='ALLOW_ADULTS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    allow_forward_to_others = models.CharField(db_column='ALLOW_FORWARD_TO_OTHERS', max_length=1)  # Field name made lowercase.
    allow_to_share = models.CharField(db_column='ALLOW_TO_SHARE', max_length=1)  # Field name made lowercase.
    allow_fb_share = models.CharField(db_column='ALLOW_FB_SHARE', max_length=1)  # Field name made lowercase.
    allow_g_plus_share = models.CharField(db_column='ALLOW_G_PLUS_SHARE', max_length=1)  # Field name made lowercase.
    allow_tw_share = models.CharField(db_column='ALLOW_TW_SHARE', max_length=1)  # Field name made lowercase.
    allow_linkedin_share = models.CharField(db_column='ALLOW_LINKEDIN_SHARE', max_length=1)  # Field name made lowercase.
    guest_name_req = models.CharField(db_column='GUEST_NAME_REQ', max_length=1)  # Field name made lowercase.
    other_guest_name_req = models.CharField(db_column='OTHER_GUEST_NAME_REQ', max_length=1)  # Field name made lowercase.
    event_reminder = models.CharField(db_column='EVENT_REMINDER', max_length=1)  # Field name made lowercase.
    ask_rsvp_poll_question = models.CharField(db_column='ASK_RSVP_POLL_QUESTION', max_length=1)  # Field name made lowercase.
    rsvp_poll_question = models.CharField(db_column='RSVP_POLL_QUESTION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rsvp_poll_options = models.TextField(db_column='RSVP_POLL_OPTIONS', blank=True, null=True)  # Field name made lowercase.
    rsvp_poll_options_type = models.CharField(db_column='RSVP_POLL_OPTIONS_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EVENT_SETTINGS'


class EventStatsVw(models.Model):
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    eventid = models.IntegerField(db_column='EVENTID', primary_key=True)  # Field name made lowercase.
    total_guests = models.IntegerField(db_column='TOTAL_GUESTS')  # Field name made lowercase.
    yes = models.IntegerField(db_column='YES', blank=True, null=True)  # Field name made lowercase.
    no = models.IntegerField(db_column='NO', blank=True, null=True)  # Field name made lowercase.
    maybe = models.IntegerField(db_column='MAYBE', blank=True, null=True)  # Field name made lowercase.
    views = models.IntegerField(db_column='VIEWS', blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EVENT_STATS_VW'


class EventTemplates(models.Model):
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    eventid = models.IntegerField(db_column='EVENTID', primary_key=True)  # Field name made lowercase.
    guest_template_json = models.TextField(db_column='GUEST_TEMPLATE_JSON', blank=True, null=True)  # Field name made lowercase.
    email_template_json = models.TextField(db_column='EMAIL_TEMPLATE_JSON', blank=True, null=True)  # Field name made lowercase.
    email_template_source = models.TextField(db_column='EMAIL_TEMPLATE_SOURCE', blank=True, null=True)  # Field name made lowercase.
    email_template_thumb = models.CharField(db_column='EMAIL_TEMPLATE_THUMB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    host_lbl = models.CharField(db_column='HOST_LBL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    about_lbl = models.CharField(db_column='ABOUT_LBL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    comment_lbl = models.CharField(db_column='COMMENT_LBL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    forward_to_lbl = models.CharField(db_column='FORWARD_TO_LBL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    location_lbl = models.CharField(db_column='LOCATION_LBL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rsvp_lbl = models.CharField(db_column='RSVP_LBL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rsvp_option1 = models.CharField(db_column='RSVP_OPTION1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rsvp_option2 = models.CharField(db_column='RSVP_OPTION2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rsvp_option3 = models.CharField(db_column='RSVP_OPTION3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    first_name_lbl = models.CharField(db_column='FIRST_NAME_LBL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    last_name_lbl = models.CharField(db_column='LAST_NAME_LBL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    adults_lbl = models.CharField(db_column='ADULTS_LBL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    kids_lbl = models.CharField(db_column='KIDS_LBL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    msg_to_host_lbl = models.CharField(db_column='MSG_TO_HOST_LBL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    submit_rsvp_lbl = models.CharField(db_column='SUBMIT_RSVP_LBL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    post_your_comments_lbl = models.CharField(db_column='POST_YOUR_COMMENTS_LBL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    comments_heading_lbl = models.CharField(db_column='COMMENTS_HEADING_LBL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    font_family = models.CharField(db_column='FONT_FAMILY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    font_color = models.CharField(db_column='FONT_COLOR', max_length=45, blank=True, null=True)  # Field name made lowercase.
    background_color = models.CharField(db_column='BACKGROUND_COLOR', max_length=45, blank=True, null=True)  # Field name made lowercase.
    background_theme_color = models.CharField(db_column='BACKGROUND_THEME_COLOR', max_length=45, blank=True, null=True)  # Field name made lowercase.
    main_headings_color = models.CharField(db_column='MAIN_HEADINGS_COLOR', max_length=45, blank=True, null=True)  # Field name made lowercase.
    buttons_color = models.CharField(db_column='BUTTONS_COLOR', max_length=45, blank=True, null=True)  # Field name made lowercase.
    buttons_text_color = models.CharField(db_column='BUTTONS_TEXT_COLOR', max_length=45, blank=True, null=True)  # Field name made lowercase.
    labels_color = models.CharField(db_column='LABELS_COLOR', max_length=45, blank=True, null=True)  # Field name made lowercase.
    event_title_color = models.CharField(db_column='EVENT_TITLE_COLOR', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EVENT_TEMPLATES'


class FbSocialShare(models.Model):
    userid = models.IntegerField(db_column='USERID', primary_key=True)  # Field name made lowercase.
    fb_emailid = models.CharField(db_column='FB_EMAILID', max_length=250)  # Field name made lowercase.
    fb_userid = models.BigIntegerField(db_column='FB_USERID')  # Field name made lowercase.
    fb_access_token = models.TextField(db_column='FB_ACCESS_TOKEN')  # Field name made lowercase.
    expire_dt = models.DateTimeField(db_column='EXPIRE_DT')  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.
    share_enable = models.CharField(db_column='SHARE_ENABLE', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FB_SOCIAL_SHARE'


class GnlContactUs(models.Model):
    user_name = models.CharField(db_column='USER_NAME', max_length=100)  # Field name made lowercase.
    user_email = models.CharField(db_column='USER_EMAIL', max_length=100)  # Field name made lowercase.
    user_phone = models.CharField(db_column='USER_PHONE', max_length=12, blank=True, null=True)  # Field name made lowercase.
    primary_use = models.CharField(db_column='PRIMARY_USE', max_length=45)  # Field name made lowercase.
    contact_reason = models.CharField(db_column='CONTACT_REASON', max_length=45)  # Field name made lowercase.
    contact_subject = models.CharField(db_column='CONTACT_SUBJECT', max_length=255)  # Field name made lowercase.
    contact_text = models.TextField(db_column='CONTACT_TEXT')  # Field name made lowercase.
    contact_dttm = models.DateTimeField(db_column='CONTACT_DTTM')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GNL_CONTACT_US'


class InvSubscribers(models.Model):
    seq_id = models.AutoField(db_column='SEQ_ID', primary_key=True)  # Field name made lowercase.
    subscription_type = models.CharField(db_column='SUBSCRIPTION_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='EMAILID', max_length=100)  # Field name made lowercase.
    first_name = models.CharField(db_column='FIRST_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='LAST_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    company = models.CharField(db_column='COMPANY', max_length=100, blank=True, null=True)  # Field name made lowercase.
    phone_nbr = models.CharField(db_column='PHONE_NBR', max_length=14, blank=True, null=True)  # Field name made lowercase.
    active = models.CharField(db_column='ACTIVE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    subscribe_dttm = models.DateTimeField(db_column='SUBSCRIBE_DTTM', blank=True, null=True)  # Field name made lowercase.
    last_upd_dttm = models.DateTimeField(db_column='LAST_UPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INV_SUBSCRIBERS'


class LoginTbl(models.Model):
    emailid = models.CharField(db_column='EMAILID', primary_key=True, max_length=50)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOGIN_TBL'


class RestapiAccess(models.Model):
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    appid = models.CharField(db_column='APPID', max_length=100, primary_key=True)# Field name made lowercase.
    app_secret = models.CharField(db_column='APP_SECRET', max_length=45)  # Field name made lowercase.
    device_id = models.CharField(db_column='DEVICE_ID', max_length=100)  # Field name made lowercase.
    device_type = models.CharField(db_column='DEVICE_TYPE', max_length=1)  # Field name made lowercase.
    created_dttm = models.DateTimeField(db_column='CREATED_DTTM')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RESTAPI_ACCESS'


class RestapiKeys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    access_token = models.CharField(db_column='ACCESS_TOKEN', max_length=40)  # Field name made lowercase.
    level = models.IntegerField(db_column='LEVEL')  # Field name made lowercase.
    ignore_limits = models.IntegerField(db_column='IGNORE_LIMITS')  # Field name made lowercase.
    is_private_key = models.IntegerField(db_column='IS_PRIVATE_KEY')  # Field name made lowercase.
    ip_address = models.TextField(db_column='IP_ADDRESS', blank=True, null=True)  # Field name made lowercase.
    created_dttm = models.DateTimeField(db_column='CREATED_DTTM')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RESTAPI_KEYS'


class RestapiLimits(models.Model):
    uri = models.CharField(max_length=255)
    count = models.IntegerField()
    hour_started = models.IntegerField()
    api_key = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'RESTAPI_LIMITS'


class SendEmailMaster(models.Model):
    emailid = models.CharField(db_column='EMAILID', primary_key=True, max_length=100)  # Field name made lowercase.
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    device_type = models.CharField(db_column='DEVICE_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    browser_type = models.CharField(db_column='BROWSER_TYPE', max_length=100)  # Field name made lowercase.
    is_user = models.CharField(db_column='IS_USER', max_length=1)  # Field name made lowercase.
    is_guest = models.CharField(db_column='IS_GUEST', max_length=1)  # Field name made lowercase.
    is_test_user = models.CharField(db_column='IS_TEST_USER', max_length=1)  # Field name made lowercase.
    unsubscribe = models.CharField(db_column='UNSUBSCRIBE', max_length=1)  # Field name made lowercase.
    create_dttm = models.DateTimeField(db_column='CREATE_DTTM')  # Field name made lowercase.
    last_sync_dttm = models.DateTimeField(db_column='LAST_SYNC_DTTM')  # Field name made lowercase.
    language_cd = models.CharField(db_column='LANGUAGE_CD', max_length=3)  # Field name made lowercase.
    alt_emailid = models.CharField(db_column='ALT_EMAILID', max_length=100)  # Field name made lowercase.
    country_code = models.CharField(db_column='COUNTRY_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SEND_EMAIL_MASTER'


class SesTracking(models.Model):
    ses_messageid = models.CharField(db_column='SES_MESSAGEID', primary_key=True, max_length=126)  # Field name made lowercase.
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    eventid = models.IntegerField(db_column='EVENTID')  # Field name made lowercase.
    event_type = models.CharField(db_column='EVENT_TYPE', max_length=30)  # Field name made lowercase.
    transactionid = models.IntegerField(db_column='TRANSACTIONID')  # Field name made lowercase.
    emailid = models.CharField(db_column='EMAILID', max_length=250)  # Field name made lowercase.
    sender_emailid = models.CharField(db_column='SENDER_EMAILID', max_length=250)  # Field name made lowercase.
    bounce_status = models.CharField(db_column='BOUNCE_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    bounce_type = models.CharField(db_column='BOUNCE_TYPE', max_length=126, blank=True, null=True)  # Field name made lowercase.
    verified = models.CharField(db_column='VERIFIED', max_length=1)  # Field name made lowercase.
    retry = models.CharField(db_column='RETRY', max_length=1)  # Field name made lowercase.
    retry_sent = models.CharField(db_column='RETRY_SENT', max_length=1)  # Field name made lowercase.
    block = models.CharField(db_column='BLOCK', max_length=1)  # Field name made lowercase.
    ignore = models.CharField(db_column='IGNORE', max_length=1)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM')  # Field name made lowercase.
    complaint_status = models.CharField(db_column='COMPLAINT_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    complaint_type = models.CharField(db_column='COMPLAINT_TYPE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    delivery_status = models.CharField(db_column='DELIVERY_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    delivery_time = models.DateTimeField(db_column='DELIVERY_TIME', blank=True, null=True)  # Field name made lowercase.
    bounce_sub_type = models.CharField(db_column='BOUNCE_SUB_TYPE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ses_notification_body = models.TextField(db_column='SES_NOTIFICATION_BODY', blank=True, null=True)  # Field name made lowercase.
    ses_delivery_body = models.TextField(db_column='SES_DELIVERY_BODY', blank=True, null=True)  # Field name made lowercase.
    ses_bounce_body = models.TextField(db_column='SES_BOUNCE_BODY', blank=True, null=True)  # Field name made lowercase.
    ses_complaint_body = models.TextField(db_column='SES_COMPLAINT_BODY', blank=True, null=True)  # Field name made lowercase.
    ses_delivery_upd_dttm = models.DateTimeField(db_column='SES_DELIVERY_UPD_DTTM', blank=True, null=True)  # Field name made lowercase.
    ses_bounce_upd_dttm = models.DateTimeField(db_column='SES_BOUNCE_UPD_DTTM', blank=True, null=True)  # Field name made lowercase.
    ses_complaint_upd_dttm = models.DateTimeField(db_column='SES_COMPLAINT_UPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SES_TRACKING'


class SesTrackingDump(models.Model):
    ses_notification_type = models.CharField(db_column='SES_NOTIFICATION_TYPE', max_length=50)  # Field name made lowercase.
    notification_json = models.TextField(db_column='NOTIFICATION_JSON', blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SES_TRACKING_DUMP'


class ShortUrls(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    long_url = models.CharField(db_column='LONG_URL', max_length=255)  # Field name made lowercase.
    short_code = models.CharField(db_column='SHORT_CODE', max_length=12)  # Field name made lowercase.
    create_dttm = models.DateTimeField(db_column='CREATE_DTTM')  # Field name made lowercase.
    link_viewed_count = models.IntegerField(db_column='LINK_VIEWED_COUNT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SHORT_URLS'


class TwSocialShare(models.Model):
    userid = models.IntegerField(db_column='USERID', primary_key=True)  # Field name made lowercase.
    tw_userid = models.BigIntegerField(db_column='TW_USERID')  # Field name made lowercase.
    tw_user_name = models.CharField(db_column='TW_USER_NAME', max_length=50)  # Field name made lowercase.
    tw_access_token = models.CharField(db_column='TW_ACCESS_TOKEN', max_length=100)  # Field name made lowercase.
    tw_access_token_secret = models.CharField(db_column='TW_ACCESS_TOKEN_SECRET', max_length=100)  # Field name made lowercase.
    expire_dt = models.DateTimeField(db_column='EXPIRE_DT', blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.
    share_enable = models.CharField(db_column='SHARE_ENABLE', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TW_SOCIAL_SHARE'


class UsrAddress(models.Model):
    userid = models.IntegerField(db_column='USERID', primary_key=True)  # Field name made lowercase.
    address_type = models.IntegerField(db_column='ADDRESS_TYPE', blank=True, null=True)  # Field name made lowercase.
    address1 = models.CharField(db_column='ADDRESS1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='ADDRESS2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='CITY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='STATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='COUNTRY', max_length=45, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZIPCODE', max_length=8, blank=True, null=True)  # Field name made lowercase.
    phone_nbr = models.CharField(db_column='PHONE_NBR', max_length=12, blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USR_ADDRESS'


class UsrContacts(models.Model):
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    contact_id = models.AutoField(db_column='CONTACT_ID', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='FIRST_NAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='LAST_NAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    middle_name = models.CharField(db_column='MIDDLE_NAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    nickname = models.CharField(db_column='NICKNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='GENDER', max_length=1, blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='EMAILID', max_length=100)  # Field name made lowercase.
    phone_nbr = models.CharField(db_column='PHONE_NBR', max_length=12, blank=True, null=True)  # Field name made lowercase.
    import_from = models.CharField(db_column='IMPORT_FROM', max_length=1, blank=True, null=True)  # Field name made lowercase.
    create_dttm = models.DateTimeField(db_column='CREATE_DTTM', blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USR_CONTACTS'


class UsrGroups(models.Model):
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    group_id = models.AutoField(db_column='GROUP_ID', primary_key=True)  # Field name made lowercase.
    group_name = models.CharField(db_column='GROUP_NAME', max_length=50)  # Field name made lowercase.
    group_status = models.CharField(db_column='GROUP_STATUS', max_length=1)  # Field name made lowercase.
    create_dttm = models.DateTimeField(db_column='CREATE_DTTM')  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USR_GROUPS'


class UsrGrpContacts(models.Model):
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    group_id = models.IntegerField(db_column='GROUP_ID')  # Field name made lowercase.
    contact_id = models.AutoField(db_column='CONTACT_ID', primary_key=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='EMAILID', max_length=100)  # Field name made lowercase.
    first_name = models.CharField(db_column='FIRST_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='LAST_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    middle_name = models.CharField(db_column='MIDDLE_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nickname = models.CharField(db_column='NICKNAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    phone_nbr = models.CharField(db_column='PHONE_NBR', max_length=12, blank=True, null=True)  # Field name made lowercase.
    key_date = models.DateField(db_column='KEY_DATE', blank=True, null=True)  # Field name made lowercase.
    sch_date = models.DateTimeField(db_column='SCH_DATE', blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM')  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1)  # Field name made lowercase.
    ignore = models.CharField(db_column='IGNORE', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USR_GRP_CONTACTS'


class UsrPaymentHdr(models.Model):
    userid = models.IntegerField(db_column='USERID', primary_key=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='EMAILID', max_length=100)  # Field name made lowercase.
    payment_type = models.CharField(db_column='PAYMENT_TYPE', max_length=2)  # Field name made lowercase.
    remaining_events_count = models.IntegerField(db_column='REMAINING_EVENTS_COUNT', blank=True, null=True)  # Field name made lowercase.
    customer_limit = models.IntegerField(db_column='CUSTOMER_LIMIT', blank=True, null=True)  # Field name made lowercase.
    video_length = models.CharField(db_column='VIDEO_LENGTH', max_length=45, blank=True, null=True)  # Field name made lowercase.
    payment_status = models.CharField(db_column='PAYMENT_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    coupon_cd = models.CharField(db_column='COUPON_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    payment_schedule = models.CharField(db_column='PAYMENT_SCHEDULE', max_length=1)  # Field name made lowercase.
    enroll_dt = models.DateField(db_column='ENROLL_DT')  # Field name made lowercase.
    expire_dt = models.DateField(db_column='EXPIRE_DT')  # Field name made lowercase.
    discount_cd = models.CharField(db_column='DISCOUNT_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    last_upd_dttm = models.DateTimeField(db_column='LAST_UPD_DTTM')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USR_PAYMENT_HDR'


class UsrPaymentLine(models.Model):
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    seqid = models.AutoField(db_column='SEQID', primary_key=True)  # Field name made lowercase.
    payment_type = models.CharField(db_column='PAYMENT_TYPE', max_length=2)  # Field name made lowercase.
    remaining_events_count = models.IntegerField(db_column='REMAINING_EVENTS_COUNT', blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='AMOUNT', blank=True, null=True)  # Field name made lowercase.
    payment = models.FloatField(db_column='PAYMENT')  # Field name made lowercase.
    payment_status = models.CharField(db_column='PAYMENT_STATUS', max_length=1)  # Field name made lowercase.
    payment_schedule = models.CharField(db_column='PAYMENT_SCHEDULE', max_length=1)  # Field name made lowercase.
    transactionid = models.CharField(db_column='TRANSACTIONID', max_length=256, blank=True, null=True)  # Field name made lowercase.
    correlationid = models.CharField(db_column='CORRELATIONID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    token = models.CharField(db_column='TOKEN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    payerid = models.CharField(db_column='PAYERID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    coupon_cd = models.CharField(db_column='COUPON_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    discount_cd = models.CharField(db_column='DISCOUNT_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    paid_by = models.CharField(db_column='PAID_BY', max_length=30, blank=True, null=True)  # Field name made lowercase.
    paid_dttm = models.DateTimeField(db_column='PAID_DTTM')  # Field name made lowercase.
    currencycode = models.CharField(db_column='CURRENCYCODE', max_length=3, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=256, blank=True, null=True)  # Field name made lowercase.
    enroll_dt = models.DateField(db_column='ENROLL_DT')  # Field name made lowercase.
    expire_dt = models.DateField(db_column='EXPIRE_DT')  # Field name made lowercase.
    last_upd_dttm = models.DateTimeField(db_column='LAST_UPD_DTTM')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USR_PAYMENT_LINE'


class UsrProfile(models.Model):
    userid = models.IntegerField(db_column='USERID', primary_key=True)  # Field name made lowercase.
    user_type = models.CharField(db_column='USER_TYPE', max_length=1)  # Field name made lowercase.
    business_name = models.CharField(db_column='BUSINESS_NAME', max_length=30)  # Field name made lowercase.
    doing_business_as = models.CharField(db_column='DOING_BUSINESS_AS', max_length=30)  # Field name made lowercase.
    personalized_url = models.CharField(db_column='PERSONALIZED_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='FIRST_NAME', max_length=30)  # Field name made lowercase.
    last_name = models.CharField(db_column='LAST_NAME', max_length=30)  # Field name made lowercase.
    middle_name = models.CharField(db_column='MIDDLE_NAME', max_length=30)  # Field name made lowercase.
    nick_name = models.CharField(db_column='NICK_NAME', max_length=50)  # Field name made lowercase.
    birthdt = models.DateField(db_column='BIRTHDT')  # Field name made lowercase.
    gender = models.CharField(db_column='GENDER', max_length=1)  # Field name made lowercase.
    user_photo_name = models.CharField(db_column='USER_PHOTO_NAME', max_length=100)  # Field name made lowercase.
    user_photo_url = models.CharField(db_column='USER_PHOTO_URL', max_length=225)  # Field name made lowercase.
    timezone = models.CharField(db_column='TIMEZONE', max_length=225)  # Field name made lowercase.
    alt_emailid = models.CharField(db_column='ALT_EMAILID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    host_email_addr = models.CharField(db_column='HOST_EMAIL_ADDR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rsvp_email_addr = models.CharField(db_column='RSVP_EMAIL_ADDR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    host_email_verified = models.CharField(db_column='HOST_EMAIL_VERIFIED', max_length=1, blank=True, null=True)  # Field name made lowercase.
    profile_status = models.CharField(db_column='PROFILE_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    language_cd = models.CharField(db_column='LANGUAGE_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    country_code = models.CharField(db_column='COUNTRY_CODE', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USR_PROFILE'


class UsrSecModuleHdr(models.Model):
    userid = models.IntegerField(db_column='USERID', blank=True, null=True)  # Field name made lowercase.
    access = models.CharField(db_column='ACCESS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    last_upd_dttm = models.DateTimeField(db_column='LAST_UPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USR_SEC_MODULE_HDR'


class UsrSecModuleLine(models.Model):
    userid = models.IntegerField(db_column='USERID', blank=True, null=True)  # Field name made lowercase.
    access = models.CharField(db_column='ACCESS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    module = models.CharField(db_column='MODULE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    menu_item = models.CharField(db_column='MENU_ITEM', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USR_SEC_MODULE_LINE'


class UsrSignon(models.Model):
    userid = models.AutoField(db_column='USERID', primary_key=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='EMAILID', max_length=100)  # Field name made lowercase.
    passwd = models.CharField(db_column='PASSWD', max_length=100)  # Field name made lowercase.
    user_type = models.CharField(db_column='USER_TYPE', max_length=1)  # Field name made lowercase.
    payment_type = models.CharField(db_column='PAYMENT_TYPE', max_length=2)  # Field name made lowercase.
    user_auth_type = models.CharField(db_column='USER_AUTH_TYPE', max_length=1)  # Field name made lowercase.
    acct_lock = models.CharField(db_column='ACCT_LOCK', max_length=1)  # Field name made lowercase.
    alt_emailid = models.CharField(db_column='ALT_EMAILID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    forgot_pwd_session = models.DateField(db_column='FORGOT_PWD_SESSION')  # Field name made lowercase.
    user_verification = models.CharField(db_column='USER_VERIFICATION', max_length=1)  # Field name made lowercase.
    user_verification_session = models.DateField(db_column='USER_VERIFICATION_SESSION')  # Field name made lowercase.
    user_ip = models.CharField(db_column='USER_IP', max_length=45)  # Field name made lowercase.
    latitude = models.FloatField(db_column='LATITUDE', blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='LONGITUDE', blank=True, null=True)  # Field name made lowercase.
    app_type = models.CharField(db_column='APP_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    last_signon_dttm = models.DateTimeField(db_column='LAST_SIGNON_DTTM')  # Field name made lowercase.
    create_dttm = models.DateField(db_column='CREATE_DTTM')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USR_SIGNON'


class VersionData(models.Model):
    version_id = models.IntegerField(db_column='VERSION_ID', primary_key=True)  # Field name made lowercase.
    version_name = models.CharField(db_column='VERSION_NAME', max_length=10)  # Field name made lowercase.
    force_update = models.CharField(db_column='FORCE_UPDATE', max_length=1)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION')  # Field name made lowercase.
    created_dttm = models.DateField(db_column='CREATED_DTTM')  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VERSION_DATA'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class SchemaVersion(models.Model):
    version_rank = models.IntegerField()
    installed_rank = models.IntegerField()
    version = models.CharField(primary_key=True, max_length=50)
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=20)
    script = models.CharField(max_length=1000)
    checksum = models.IntegerField(blank=True, null=True)
    installed_by = models.CharField(max_length=100)
    installed_on = models.DateTimeField()
    execution_time = models.IntegerField()
    success = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'schema_version'
