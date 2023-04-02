from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment

from .schema import AssignmentSchema, AssignmentGradeSchema
teacher_assignments_resources = Blueprint('teacher_assignments_resources',__name__)

@teacher_assignments_resources.route('/assignments',methods=['GET'],strict_slashes=False)
@decorators.auth_principal
def list_assignments(t):
    '''Return list of assignments submitted to a teacher'''
    teacher_assignments = Assignment.get_assignments_by_teacher(t.teacher_id)
    teacher_assignments_dump = AssignmentSchema().dump(teacher_assignments,many=True)
    return APIResponse.respond(teacher_assignments_dump)


@teacher_assignments_resources.route('/assignments/grade', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
@decorators.auth_principal
def grade_assignments(t, incoming_payload):
    '''Grading the assignment'''
    graded_payload = AssignmentGradeSchema().load(incoming_payload)
    # print(incoming_payload)
    graded_payload.teacher_id = t.teacher_id

    graded_assignment = Assignment.grades(
        _id=graded_payload.id,
        grade=graded_payload.grade,
        principal=t
    )
    db.session.commit()
    graded_assignment_dump = AssignmentSchema().dump(graded_assignment)
    return APIResponse.respond(data=graded_assignment_dump)


    