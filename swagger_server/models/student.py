# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Student(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, student_id: int=None, first_name: str=None, laste_name: str=None, grades: object=None):  # noqa: E501
        """Student - a model defined in Swagger

        :param student_id: The student_id of this Student.  # noqa: E501
        :type student_id: int
        :param first_name: The first_name of this Student.  # noqa: E501
        :type first_name: str
        :param laste_name: The laste_name of this Student.  # noqa: E501
        :type laste_name: str
        :param grades: The grades of this Student.  # noqa: E501
        :type grades: object
        """
        self.swagger_types = {
            'student_id': int,
            'first_name': str,
            'laste_name': str,
            'grades': object
        }

        self.attribute_map = {
            'student_id': 'student_id',
            'first_name': 'first_name',
            'laste_name': 'laste_name',
            'grades': 'grades'
        }

        self._student_id = student_id
        self._first_name = first_name
        self._laste_name = laste_name
        self._grades = grades

    @classmethod
    def from_dict(cls, dikt) -> 'Student':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Student of this Student.  # noqa: E501
        :rtype: Student
        """
        return util.deserialize_model(dikt, cls)

    @property
    def student_id(self) -> int:
        """Gets the student_id of this Student.


        :return: The student_id of this Student.
        :rtype: int
        """
        return self._student_id

    @student_id.setter
    def student_id(self, student_id: int):
        """Sets the student_id of this Student.


        :param student_id: The student_id of this Student.
        :type student_id: int
        """

        self._student_id = student_id

    @property
    def first_name(self) -> str:
        """Gets the first_name of this Student.


        :return: The first_name of this Student.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        """Sets the first_name of this Student.


        :param first_name: The first_name of this Student.
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def laste_name(self) -> str:
        """Gets the laste_name of this Student.


        :return: The laste_name of this Student.
        :rtype: str
        """
        return self._laste_name

    @laste_name.setter
    def laste_name(self, laste_name: str):
        """Sets the laste_name of this Student.


        :param laste_name: The laste_name of this Student.
        :type laste_name: str
        """

        self._laste_name = laste_name

    @property
    def grades(self) -> object:
        """Gets the grades of this Student.


        :return: The grades of this Student.
        :rtype: object
        """
        return self._grades

    @grades.setter
    def grades(self, grades: object):
        """Sets the grades of this Student.


        :param grades: The grades of this Student.
        :type grades: object
        """

        self._grades = grades