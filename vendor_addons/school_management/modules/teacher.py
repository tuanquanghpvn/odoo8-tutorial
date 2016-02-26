# -*- coding: utf-8 -*-

from openerp import fields, models


class Teacher(models.Model):
    GENDER_CHOICE = [(1, 'Nam'), (2, 'Nữ')]

    _name = "teacher"
    _rec_name = "full_name"

    full_name = fields.Char(string=u"Họ tên", required=True)
    home_town = fields.Char(string=u"Quê quán", required=True)
    date_of_birth = fields.Date(string=u"Ngày tháng năm sinh", required=True)
    gender = fields.Selection(GENDER_CHOICE, string=u"Giới tính", required=True)
    phone_number = fields.Char(string=u"Điện thoại")
    subject_id = fields.One2many("subject", 'teacher_id', string=u"Lớp học")
