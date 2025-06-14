from django.db import migrations

def add_account_types(apps, schema_editor):
    BankAccountType = apps.get_model('accounts', 'BankAccountType')
    
    # Create Savings Account
    BankAccountType.objects.create(
        name='Savings Account',
        maximum_withdrawal_amount=5000000.00,  # 5 million rupiah
        annual_interest_rate=2.50,
        interest_calculation_per_year=12
    )
    
    # Create Current Account
    BankAccountType.objects.create(
        name='Current Account',
        maximum_withdrawal_amount=10000000.00,  # 10 million rupiah
        annual_interest_rate=1.50,
        interest_calculation_per_year=12
    )

def remove_account_types(apps, schema_editor):
    BankAccountType = apps.get_model('accounts', 'BankAccountType')
    BankAccountType.objects.filter(
        name__in=['Savings Account', 'Current Account']
    ).delete()

class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0001_initial'),  # Replace with your latest migration
    ]

    operations = [
        migrations.RunPython(add_account_types, remove_account_types),
    ]