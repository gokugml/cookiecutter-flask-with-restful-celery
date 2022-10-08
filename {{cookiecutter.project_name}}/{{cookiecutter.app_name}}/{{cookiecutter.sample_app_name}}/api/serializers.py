from {{cookiecutter.app_name}}.extensions import db, ma
from {{cookiecutter.app_name}}.{{cookiecutter.sample_app_name}}.models import Sample

"""
Schema classes, which is the same concept as Django Serializers

https://marshmallow.readthedocs.io/en/latest/api_reference.html#marshmallow.Schema
Serializing
序列化[可以把数据对象转化为可存储或可传输的数据类型，例如：objects/object->list/dict，dict/list->string]
Deserializing
反序列化器[把可存储或可传输的数据类型转换成数据对象，例如：list/dict->objects/object，string->dict/list]
Validation
数据校验，可以在反序列化阶段，针对要转换数据的内容进行类型验证或自定义验证。
"""


class SampleSchema(ma.SQLAlchemySchema):
    id = ma.Int(dump_only=True)
    name = ma.String()
    email = ma.String(allow_none=True)

    class Meta:
        model = Sample
        fields = ("id", "name", "email")
        # exclude = (,)
        sqla_session = db.session
        load_instance = True
