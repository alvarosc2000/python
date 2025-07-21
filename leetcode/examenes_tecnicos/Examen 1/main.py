import json
import csv

def load_transactions(filename):
    with open(filename,'r') as file:
        return json.load(file)


def filter_successful(transactions):
    return [t for t in transactions if t['status'] == 'SUCCESS']

def group_and_sum(transactions):
    totals = {}
    for t in transactions:
        user = t['user_id']
        amount = t['amount']
        totals[user] = totals.get(user,0) + amount
    return totals

def save_to_csv(totals,output_filename):
    with open(output_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['user_id', 'total_amount'])
        for user_id, amount in totals.items():
            writer.writerow([user_id, round(amount,2)])

def main():
    try:
        transactions = load_transactions('transactions.json')
        successful = filter_successful(transactions)
        totals = group_and_sum(successful)
        save_to_csv(totals, 'report.csv')
        print("✅ Reporte generado exitosamente.")
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == '__main__':
    main()