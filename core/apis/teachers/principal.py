from flask import Blueprint
from core.apis import decorators
from core.models.teachers import Teacher
from core.apis.responses import APIResponse
from core.apis.teachers.schema import TeacherSchema
principal_teachers_resources = Blueprint('principal_teachers_resources', __name__)
@principal_teachers_resources.route('/teachers',methods=['GET'],strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    """Returns the list of teachers"""
    teachers_list=Teacher.get_all_teachers()
    teacher_list_dump=TeacherSchema().dump(teachers_list,many=True)
    return APIResponse.respond(data=teacher_list_dump)