from flask import Flask, jsonify, request

app = Flask(__name__) # Creates the flask application

# Sample data
students = [
    {"id": 1, "name": "Ravi", "course": "BSc CS"},
    {"id": 2, "name": "Ayesha", "course": "BSc CS"}
]

# Home Route - displays the default message when the app is running
@app.route("/")
def home():
    return "Student Microservice is Running"

# GET /students - returns all the students records in JSON format
@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)

# GET /students/<id>/ -  Returns a specific student based on their ID
@app.route("/students/<int:id>", methods=["GET"])
def get_student(id):

    # Search the student with the given id
    for student in students:
        if student["id"] == id:
            return jsonify(student)

    # Return an error message if the student is not found
    return jsonify({"message": "Student not found"}), 404


# POST /students - adds a new student to the student list
@app.route("/students", methods=["POST"])
def add_student():

    # Get the JSON data 
    data = request.get_json()
    student = {
        "id": len(students) + 1,
        "name": data["name"],
        "course": data["course"]
    }
    students.append(student)
    return jsonify(student), 201
 
# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
