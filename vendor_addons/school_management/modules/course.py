# -*- coding: utf-8 -*-

from openerp import fields, models


class Course(models.Model):
    _name = "course"
    _rec_name = "name"

    name = fields.Char(string=u"Tên môn học", required=True)
    description = fields.Text(string=u"Mô tả")
    subject_id = fields.One2many("subject", "course_id", string="Danh sách lớp học")

