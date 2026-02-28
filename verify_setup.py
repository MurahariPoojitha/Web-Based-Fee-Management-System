from django.contrib.auth.models import User
from feesapp.models import Student, BusFee, FeePayment

def verify():
    print("--- System Verification ---")
    s = Student.objects.filter(roll_number='25FE001').first()
    if s:
        print(f"✅ Found Student: {s.name}")
        print(f"✅ Roll Number: {s.roll_number}")
        print(f"✅ Linked Username: {s.user.username}")
        print(f"✅ Password for test: student001123")
    else:
        print("❌ Student 25FE001 not found. Please run bulk population.")

if __name__ == "__main__":
    verify()
