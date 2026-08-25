% Student - Teacher - Subject Code

student_teacher(pavithra, teacher1, ai101).
student_teacher(rahul, teacher2, cs102).
student_teacher(anitha, teacher1, cs103).

% Rule
details(Student, Teacher, SubjectCode) :-
    student_teacher(Student, Teacher, SubjectCode).
