from django.contrib.auth.models import User
from feesapp.models import Student, BusFee, FeePayment

def setup():
    # 1. Ensure Bus Fee Area exists
    bus, _ = BusFee.objects.get_or_create(area='Uppal', amount=5000)

    # 2. Setup Admin (Username: admin, Pass: admin123)
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print("Admin user 'admin' created.")
    else:
        print("Admin user 'admin' already exists.")

    # 3. Setup Student (Username: student, Pass: student123)
    # If the user 'student' already exists, we will update it or ensure it has a profile
    student_user = User.objects.filter(username='student').first()
    if not student_user:
        student_user = User.objects.create_user('student', 'student@example.com', 'student123')
        print("Student user 'student' created.")
    else:
        student_user.set_password('student123')
        student_user.save()
        print("Student user 'student' updated.")

    # 4. Ensure Student Profile exists for 'student'
    student_profile = Student.objects.filter(user=student_user).first()
    if not student_profile:
        student_profile = Student.objects.create(
            user=student_user,
            name='Test Student',
            roll_number='ROLL-ST001',
            admission_type='Convenor',
            residence_type='Day Scholar',
            semester=1,
            academic_year='2025-26'
        )
        print("Student profile for 'student' created.")
    else:
        print("Student profile for 'student' already exists.")

    # 5. Instructions for New Students
    print("\n--- Project URLs ---")
    print("Login Page: http://127.0.0.1:8000/accounts/login/")
    print("Admin Page: http://127.0.0.1:8000/admin/")
    print("\n--- Rule for Adding New Students ---")
    print("Each new student MUST have a unique username (e.g., student2, student3).")
    print("You cannot use the name 'student' for two different people.")

if __name__ == "__main__":
    setup()
