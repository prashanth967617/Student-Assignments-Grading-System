@app.route('/principal/assignments', methods=['GET'])
def get_assignments():
    # Extract principal_id from headers
    principal_id = request.headers['X-Principal']['principal_id']
    
    # Query to fetch assignments that are submitted and graded
    assignments = db.session.query(Assignment).filter(
        Assignment.state == 'GRADED'
    ).all()
    
    # Convert assignments to a serializable format
    assignments_data = [
        {
            "id": assignment.id,
            "content": assignment.content,
            "created_at": assignment.created_at.isoformat(),
            "grade": assignment.grade,
            "state": assignment.state,
            "student_id": assignment.student_id,
            "teacher_id": assignment.teacher_id,
            "updated_at": assignment.updated_at.isoformat(),
        }
        for assignment in assignments
    ]
    
    return jsonify({"data": assignments_data}), 200
