# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DataTag(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'name': 'str',
        'tag': 'str',
        'statement_code': 'str',
        'statement_type': 'str',
        'parent': 'str',
        'factor': 'str',
        'balance': 'str',
        'type': 'str',
        'unit': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'tag': 'tag',
        'statement_code': 'statement_code',
        'statement_type': 'statement_type',
        'parent': 'parent',
        'factor': 'factor',
        'balance': 'balance',
        'type': 'type',
        'unit': 'unit'
    }

    def __init__(self, id=None, name=None, tag=None, statement_code=None, statement_type=None, parent=None, factor=None, balance=None, type=None, unit=None):  # noqa: E501
        """DataTag - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._tag = None
        self._statement_code = None
        self._statement_type = None
        self._parent = None
        self._factor = None
        self._balance = None
        self._type = None
        self._unit = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if tag is not None:
            self.tag = tag
        if statement_code is not None:
            self.statement_code = statement_code
        if statement_type is not None:
            self.statement_type = statement_type
        if parent is not None:
            self.parent = parent
        if factor is not None:
            self.factor = factor
        if balance is not None:
            self.balance = balance
        if type is not None:
            self.type = type
        if unit is not None:
            self.unit = unit

    @property
    def id(self):
        """Gets the id of this DataTag.  # noqa: E501

        The Intrinio ID for the Data Tag  # noqa: E501

        :return: The id of this DataTag.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataTag.

        The Intrinio ID for the Data Tag  # noqa: E501

        :param id: The id of this DataTag.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DataTag.  # noqa: E501

        The readable name of the Data Tag  # noqa: E501

        :return: The name of this DataTag.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DataTag.

        The readable name of the Data Tag  # noqa: E501

        :param name: The name of this DataTag.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def tag(self):
        """Gets the tag of this DataTag.  # noqa: E501

        The code-name of the Data Tag  # noqa: E501

        :return: The tag of this DataTag.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this DataTag.

        The code-name of the Data Tag  # noqa: E501

        :param tag: The tag of this DataTag.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def statement_code(self):
        """Gets the statement_code of this DataTag.  # noqa: E501

        The code of the financial statement to which this Data Tag belongs  # noqa: E501

        :return: The statement_code of this DataTag.  # noqa: E501
        :rtype: str
        """
        return self._statement_code

    @statement_code.setter
    def statement_code(self, statement_code):
        """Sets the statement_code of this DataTag.

        The code of the financial statement to which this Data Tag belongs  # noqa: E501

        :param statement_code: The statement_code of this DataTag.  # noqa: E501
        :type: str
        """

        self._statement_code = statement_code

    @property
    def statement_type(self):
        """Gets the statement_type of this DataTag.  # noqa: E501

        The format of the financial statment to which this Data Tag belongs  # noqa: E501

        :return: The statement_type of this DataTag.  # noqa: E501
        :rtype: str
        """
        return self._statement_type

    @statement_type.setter
    def statement_type(self, statement_type):
        """Sets the statement_type of this DataTag.

        The format of the financial statment to which this Data Tag belongs  # noqa: E501

        :param statement_type: The statement_type of this DataTag.  # noqa: E501
        :type: str
        """
        allowed_values = ["financial", "industrial"]  # noqa: E501
        if statement_type not in allowed_values:
            raise ValueError(
                "Invalid value for `statement_type` ({0}), must be one of {1}"  # noqa: E501
                .format(statement_type, allowed_values)
            )

        self._statement_type = statement_type

    @property
    def parent(self):
        """Gets the parent of this DataTag.  # noqa: E501

        The parent Data Tag forming the statement relationship with the factor  # noqa: E501

        :return: The parent of this DataTag.  # noqa: E501
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this DataTag.

        The parent Data Tag forming the statement relationship with the factor  # noqa: E501

        :param parent: The parent of this DataTag.  # noqa: E501
        :type: str
        """

        self._parent = parent

    @property
    def factor(self):
        """Gets the factor of this DataTag.  # noqa: E501

        The operator forming the statement relationship between the child Data Tag (or Data Tags) and the parent Data Tag  # noqa: E501

        :return: The factor of this DataTag.  # noqa: E501
        :rtype: str
        """
        return self._factor

    @factor.setter
    def factor(self, factor):
        """Sets the factor of this DataTag.

        The operator forming the statement relationship between the child Data Tag (or Data Tags) and the parent Data Tag  # noqa: E501

        :param factor: The factor of this DataTag.  # noqa: E501
        :type: str
        """

        self._factor = factor

    @property
    def balance(self):
        """Gets the balance of this DataTag.  # noqa: E501

        Whether the Data Tag represents a credit or debit  # noqa: E501

        :return: The balance of this DataTag.  # noqa: E501
        :rtype: str
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this DataTag.

        Whether the Data Tag represents a credit or debit  # noqa: E501

        :param balance: The balance of this DataTag.  # noqa: E501
        :type: str
        """

        self._balance = balance

    @property
    def type(self):
        """Gets the type of this DataTag.  # noqa: E501

        The nature of the Data Tag, operating or nonoperating  # noqa: E501

        :return: The type of this DataTag.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DataTag.

        The nature of the Data Tag, operating or nonoperating  # noqa: E501

        :param type: The type of this DataTag.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def unit(self):
        """Gets the unit of this DataTag.  # noqa: E501

        The unit of the Data Tag  # noqa: E501

        :return: The unit of this DataTag.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this DataTag.

        The unit of the Data Tag  # noqa: E501

        :param unit: The unit of this DataTag.  # noqa: E501
        :type: str
        """

        self._unit = unit

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DataTag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
