@app.route('/principal/teachers', methods=['GET'])
def get_teachers():
    # Extract principal_id from headers
    principal_id = request.headers['X-Principal']['principal_id']
    
    # Query to fetch all teachers
    teachers = db.session.query(Teacher).all()
    
    # Convert teachers to a serializable format
    teachers_data = [
        {
            "id": teacher.id,
            "created_at": teacher.created_at.isoformat(),
            "updated_at": teacher.updated_at.isoformat(),
            "user_id": teacher.user_id
        }
        for teacher in teachers
    ]
    
    return jsonify({"data": teachers_data}), 200
