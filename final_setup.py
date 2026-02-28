import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'feemanagementsystem.settings')
django.setup()

from django.contrib.auth.models import User
from feesapp.models import Student, BusFee, FeePayment

def setup_final():
    print("--- Starting Final System Setup ---")
    
    # 1. Clear existing test data for a completely clean state
    User.objects.filter(username__in=['admin', 'student']).delete()
    BusFee.objects.all().delete()
    
    # 2. Create Admin (admin / admin123)
    admin = User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("✅ Admin created: admin / admin123")
    
    # 3. Create Bus Fee Area
    bus_area, _ = BusFee.objects.get_or_create(area='Hyderabad City', amount=7500.00)
    print(f"✅ Bus Area created: {bus_area.area} (Amount: ₹{bus_area.amount})")
    
    # 4. Create Student User (student / student123)
    student_user = User.objects.create_user('student', 'student@example.com', 'student123')
    print("✅ Student user created: student / student123")
    
    # 5. Create Student Profile (linked to the user)
    # This will trigger the post_save signal to create Semester 1 Fee record
    student_profile = Student.objects.create(
        user=student_user,
        name='Test Student',
        roll_number='2025-FE-001',
        admission_type='Convenor',
        residence_type='Day Scholar',
        transport_type='Bus Student',
        bus_area=bus_area,
        academic_year='2025-2026',
        semester=1
    )
    print(f"✅ Student Profile created for: {student_profile.name}")
    
    # 6. Verify Fee Record
    fee = FeePayment.objects.filter(student=student_profile, semester=1).first()
    if fee:
        print(f"✅ Fee record auto-created! Semester 1 Total: ₹{fee.total_amount}")
        print(f"   (Tuition: ₹{fee.tuition_fee}, NBA: ₹{fee.nba_fee}, JNTUH: ₹{fee.jntuh_fee}, Bus: ₹{fee.bus_fee})")
    else:
        print("❌ Error: Fee record was not created. Signal check failed.")

    print("\n--- Final Project Links ---")
    print("1. Login Page: http://127.0.0.1:8000/accounts/login/")
    print("2. Admin Dashboard: http://127.0.0.1:8000/admin-dashboard/")
    print("3. Student Dashboard: http://127.0.0.1:8000/student-dashboard/")
    print("4. Admin Site: http://127.0.0.1:8000/admin/")
    print("\nSystem ready for verification.")

if __name__ == "__main__":
    setup_final()
