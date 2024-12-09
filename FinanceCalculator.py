class FinanceCalculator:
    def _init_(self):
        """Inisialisasi kalkulator keuangan tanpa properti awal."""
        pass

    def calculate_monthly_expenses(self, fixed_expenses, variable_expenses):
        """Menghitung total pengeluaran bulanan."""
        return fixed_expenses + variable_expenses

    def calculate_savings(self, income, expenses):
        """Menghitung tabungan bulanan."""
        return income - expenses

    def calculate_investment(self, initial_investment, monthly_contribution, annual_rate, years):
        """Menghitung nilai investasi setelah periode tertentu."""
        months = years * 12
        monthly_rate = annual_rate / 12
        future_value = initial_investment * ((1 + monthly_rate) ** months)

        for month in range(1, months + 1):
            future_value += monthly_contribution * ((1 + monthly_rate) ** (months - month))

        return future_value
def main():
    calc = FinanceCalculator()

    print("=== Aplikasi Kalkulator Keuangan Sederhana ===")
    print("1. Hitung Pengeluaran Bulanan")
    print("2. Hitung Tabungan Bulanan")
    print("3. Hitung Nilai Investasi")
    try:
        choice = int(input("Pilih opsi (1/2/3): "))
    except ValueError:
        print("Input tidak valid. Masukkan angka 1, 2, atau 3.")
        return

    if choice == 1:
        try:
            fixed_expenses = float(input("Masukkan pengeluaran tetap bulanan (Rp): "))
            variable_expenses = float(input("Masukkan pengeluaran variabel bulanan (Rp): "))
            total_expenses = calc.calculate_monthly_expenses(fixed_expenses, variable_expenses)
            print(f"Total pengeluaran bulanan Anda adalah: Rp{total_expenses:,.2f}")
        except ValueError:
            print("Input tidak valid. Masukkan angka yang benar.")

    elif choice == 2:
        try:
            income = float(input("Masukkan pendapatan bulanan (Rp): "))
            expenses = float(input("Masukkan total pengeluaran bulanan (Rp): "))
            print(f"DEBUG: income={income}, expenses={expenses}")  # Debugging nilai input
            savings = calc.calculate_savings(income, expenses)
            print(f"Tabungan bulanan Anda adalah: Rp{savings:,.2f}")
        except ValueError:
            print("Input tidak valid. Masukkan angka yang benar.")

    elif choice == 3:
        try:
            initial_investment = float(input("Masukkan investasi awal (Rp): "))
            monthly_contribution = float(input("Masukkan kontribusi bulanan (Rp): "))
            annual_rate = float(input("Masukkan suku bunga tahunan (dalam persen): ")) / 100
            years = int(input("Masukkan durasi investasi (dalam tahun): "))
            future_value = calc.calculate_investment(initial_investment, monthly_contribution, annual_rate, years)
            print(f"Nilai investasi Anda setelah {years} tahun adalah: Rp{future_value:,.2f}")
        except ValueError:
            print("Input tidak valid. Pastikan angka yang dimasukkan benar.")

    else:
        print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()