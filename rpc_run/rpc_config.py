from wisdoms.config import c
from wisdoms.ms import ms_base, permit, add_user, add_uid

CONFIG = c.get("MS_HOST")
MsBase = ms_base(CONFIG)
auth_ = permit(CONFIG)
user_ = add_user(CONFIG)
uid_ = add_uid(CONFIG)
