from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {"id": 1, "name": "Ravi", "course": "BSc CS"},
    {"id": 2, "name": "Ayesha", "course": "BSc CS"}
]


@app.route("/")
def home():
    return "Student Microservice is Running"


@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)


@app.route("/students/<int:id>", methods=["GET"])
def get_student(id):
    for student in students:
        if student["id"] == id:
            return jsonify(student)
    return jsonify({"message": "Student not found"}), 404

 
@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()
    student = {
        "id": len(students) + 1,
        "name": data["name"],
        "course": data["course"]
    }
    students.append(student)
    return jsonify(student), 201
 
 
if __name__ == "__main__":
    app.run(debug=True)
