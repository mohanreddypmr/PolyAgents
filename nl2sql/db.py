tables_descrptions = {
"Departments": "The Departments table holds academic department information. Each department may be associated with multiple students, professors, and courses. Use it when filtering by department or analyzing department-specific activity.",
"Students": "The Students table contains personal and academic enrollment details for students. Each student is associated with a department and can be enrolled in multiple courses. Use this table to filter students by department or analyze student enrollment.",
"Professors": "The Professors table stores data about academic faculty. Each professor belongs to a department and may teach one or more courses. Use this when identifying course instructors or analyzing departmental faculty.",
"Courses": "The Courses table contains the list of academic courses offered by departments. Each course is taught by a professor and belongs to a department. Use it for curriculum planning, instructor assignments, or course scheduling.",
"Enrollments": "The Enrollments table tracks which students are enrolled in which courses, including the date of enrollment. Use it to analyze student course load, popularity of courses, or to join student and course data.",
"Classrooms": "The Classrooms table defines physical classrooms, including building and room number, and capacity. It supports the scheduling system for courses. Use it to analyze classroom utilization or room assignments.",
"Schedules": "The Schedules table links courses to classrooms and timeslots, including day of the week and start/end times. Use it to retrieve timetable information or detect scheduling conflicts.",
"Grades": "The Grades table records student performance in courses by linking enrollment to a grade and grade point. Use it for GPA calculation, performance tracking, and academic reports.",
"Assignments": "The Assignments table contains homework or project records tied to specific courses. Each assignment has a title, due date, and total marks. Use this table for academic workload or submission tracking.",
"Submissions": "The Submissions table tracks which students submitted which assignments and the marks they received. Use this to evaluate assignment performance and submission timing.",
"Clubs": "The Clubs table holds information about student clubs, including their faculty advisor and founding year. Use this when analyzing extracurricular involvement or managing student organizations.",
"ClubMembers": "The ClubMembers table links students to clubs and records their role (e.g., President, Member). Use this table to retrieve club rosters, roles, or member count."
} 

columns_descrptions = {
  "Departments": [
    {
      "column_name": "department_id",
      "data_type": "INTEGER",
      "description": "Unique identifier for each academic department."
    },
    {
      "column_name": "department_name",
      "data_type": "TEXT",
      "description": "The name of the department."
    },
    {
      "column_name": "head_of_department_id",
      "data_type": "INTEGER",
      "description": "The ID of the professor who is the head of the department."
    },
    {
      "column_name": "founding_year",
      "data_type": "INTEGER",
      "description": "The year the department was founded."
    }
  ],
  "Students": [
    {
      "column_name": "student_id",
      "data_type": "INTEGER",
      "description": "Unique identifier for each student."
    },
    {
      "column_name": "first_name",
      "data_type": "TEXT",
      "description": "The student's first name."
    },
    {
      "column_name": "last_name",
      "data_type": "TEXT",
      "description": "The student's last name."
    },
    {
      "column_name": "email",
      "data_type": "TEXT",
      "description": "The student's email address."
    },
    {
      "column_name": "department_id",
      "data_type": "INTEGER",
      "description": "The ID of the department the student is enrolled in."
    },
    {
      "column_name": "enrollment_date",
      "data_type": "DATE",
      "description": "The date the student was enrolled."
    }
  ],
  "Professors": [
    {
      "column_name": "professor_id",
      "data_type": "INTEGER",
      "description": "Unique identifier for each professor."
    },
    {
      "column_name": "first_name",
      "data_type": "TEXT",
      "description": "The professor's first name."
    },
    {
      "column_name": "last_name",
      "data_type": "TEXT",
      "description": "The professor's last name."
    },
    {
      "column_name": "email",
      "data_type": "TEXT",
      "description": "The professor's email address."
    },
    {
      "column_name": "department_id",
      "data_type": "INTEGER",
      "description": "The ID of the department the professor belongs to."
    },
    {
      "column_name": "hire_date",
      "data_type": "DATE",
      "description": "The date the professor was hired."
    },
    {
      "column_name": "salary",
      "data_type": "REAL",
      "description": "The professor's annual salary."
    }
  ],
  "Courses": [
    {
      "column_name": "course_id",
      "data_type": "INTEGER",
      "description": "Unique identifier for each course."
    },
    {
      "column_name": "course_name",
      "data_type": "TEXT",
      "description": "The full name of the course."
    },
    {
      "column_name": "course_code",
      "data_type": "TEXT",
      "description": "A unique code for the course."
    },
    {
      "column_name": "department_id",
      "data_type": "INTEGER",
      "description": "The ID of the department that offers the course."
    },
    {
      "column_name": "professor_id",
      "data_type": "INTEGER",
      "description": "The ID of the professor teaching the course."
    },
    {
      "column_name": "credits",
      "data_type": "INTEGER",
      "description": "The number of credits for the course."
    }
  ],
  "Enrollments": [
    {
      "column_name": "enrollment_id",
      "data_type": "INTEGER",
      "description": "Unique identifier for each enrollment."
    },
    {
      "column_name": "student_id",
      "data_type": "INTEGER",
      "description": "The ID of the student who is enrolled."
    },
    {
      "column_name": "course_id",
      "data_type": "INTEGER",
      "description": "The ID of the course the student is enrolled in."
    },
    {
      "column_name": "enrollment_date",
      "data_type": "DATE",
      "description": "The date of enrollment."
    }
  ],
  "Classrooms": [
    {
      "column_name": "classroom_id",
      "data_type": "INTEGER",
      "description": "Unique identifier for each classroom."
    },
    {
      "column_name": "building",
      "data_type": "TEXT",
      "description": "The building name of the classroom."
    },
    {
      "column_name": "room_number",
      "data_type": "TEXT",
      "description": "The room number of the classroom."
    },
    {
      "column_name": "capacity",
      "data_type": "INTEGER",
      "description": "The maximum capacity of the classroom."
    }
  ],
  "Schedules": [
    {
      "column_name": "schedule_id",
      "data_type": "INTEGER",
      "description": "Unique identifier for each schedule entry."
    },
    {
      "column_name": "course_id",
      "data_type": "INTEGER",
      "description": "The ID of the course being scheduled."
    },
    {
      "column_name": "classroom_id",
      "data_type": "INTEGER",
      "description": "The ID of the classroom assigned for the course."
    },
    {
      "column_name": "day_of_week",
      "data_type": "TEXT",
      "description": "The day of the week for the class."
    },
    {
      "column_name": "start_time",
      "data_type": "TIME",
      "description": "The start time of the class."
    },
    {
      "column_name": "end_time",
      "data_type": "TIME",
      "description": "The end time of the class."
    }
  ],
  "Grades": [
    {
      "column_name": "grade_id",
      "data_type": "INTEGER",
      "description": "Unique identifier for each grade record."
    },
    {
      "column_name": "enrollment_id",
      "data_type": "INTEGER",
      "description": "The ID of the enrollment record this grade belongs to."
    },
    {
      "column_name": "grade_letter",
      "data_type": "TEXT",
      "description": "The final grade letter (e.g., 'A', 'B+')."
    },
    {
      "column_name": "grade_point",
      "data_type": "REAL",
      "description": "The GPA value for the grade."
    },
    {
      "column_name": "grade_date",
      "data_type": "DATE",
      "description": "The date the grade was issued."
    }
  ],
  "Assignments": [
    {
      "column_name": "assignment_id",
      "data_type": "INTEGER",
      "description": "Unique identifier for each assignment."
    },
    {
      "column_name": "course_id",
      "data_type": "INTEGER",
      "description": "The ID of the course the assignment belongs to."
    },
    {
      "column_name": "assignment_title",
      "data_type": "TEXT",
      "description": "The title of the assignment."
    },
    {
      "column_name": "due_date",
      "data_type": "DATE",
      "description": "The due date for the assignment."
    },
    {
      "column_name": "total_marks",
      "data_type": "INTEGER",
      "description": "The maximum marks for the assignment."
    }
  ],
  "Submissions": [
    {
      "column_name": "submission_id",
      "data_type": "INTEGER",
      "description": "Unique identifier for each submission."
    },
    {
      "column_name": "assignment_id",
      "data_type": "INTEGER",
      "description": "The ID of the assignment being submitted."
    },
    {
      "column_name": "student_id",
      "data_type": "INTEGER",
      "description": "The ID of the student who submitted the assignment."
    },
    {
      "column_name": "submission_date",
      "data_type": "DATE",
      "description": "The date of the submission."
    },
    {
      "column_name": "marks_obtained",
      "data_type": "INTEGER",
      "description": "The marks the student received on the assignment."
    }
  ],
  "Clubs": [
    {
      "column_name": "club_id",
      "data_type": "INTEGER",
      "description": "Unique identifier for each club."
    },
    {
      "column_name": "club_name",
      "data_type": "TEXT",
      "description": "The name of the student club."
    },
    {
      "column_name": "faculty_advisor_id",
      "data_type": "INTEGER",
      "description": "The ID of the professor who advises the club."
    },
    {
      "column_name": "founding_year",
      "data_type": "INTEGER",
      "description": "The year the club was founded."
    }
  ],
  "ClubMembers": [
    {
      "column_name": "member_id",
      "data_type": "INTEGER",
      "description": "Unique identifier for each club member record."
    },
    {
      "column_name": "student_id",
      "data_type": "INTEGER",
      "description": "The ID of the student who is a member of the club."
    },
    {
      "column_name": "club_id",
      "data_type": "INTEGER",
      "description": "The ID of the club the student is a member of."
    },
    {
      "column_name": "role",
      "data_type": "TEXT",
      "description": "The role of the student in the club (e.g., 'President')."
    },
    {
      "column_name": "join_date",
      "data_type": "DATE",
      "description": "The date the student joined the club."
    }
  ]
}


def get_table_description(table_name):
    return tables_descrptions.get(table_name, "No description available.")

def get_column_descriptions(table_name):
    return columns_descrptions.get(table_name, [])


def get_table_descriptions():
    return tables_descrptions

def get_distinct_values(table, column, limit=10):
    import sqlite3
    conn = sqlite3.connect('university.db')
    cursor = conn.cursor()
    query = f"SELECT DISTINCT {column} FROM {table} LIMIT {limit};"
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return [row[0] for row in results]

def execute_query(query):
    import sqlite3
    conn = sqlite3.connect('university.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results