# -*- coding: utf-8 -*-

from openerp import fields, models


class Subject(models.Model):
    _name = "subject"
    _rec_name = "name"

    name = fields.Char(string=u"Tên lớp học", required=True)
    description = fields.Text(string=u"Mô tả")
    course_id = fields.Many2one("course", required=True, string=u"Danh sách khoá học")
    teacher_id = fields.Many2one("teacher", required=True, string=u"Giáo viên")
    student_id = fields.One2many("student", "subject_id", string=u"Danh sách sinh viên")

