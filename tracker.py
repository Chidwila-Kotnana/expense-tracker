import json
import os


class ExpenseTracker:
    def __init__(self):
        self.expense_list = self.load()

    def load(self):
        try:
            with open("expenses.json", "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save(self):
        tmp = "expenses.json.tmp"
        with open(tmp, "w") as f:
            json.dump(self.expense_list, f)
        os.replace(tmp, "expenses.json")

    def _prompt_or_cancel(self, message):
        """Prompt the user and return their input, or None if they abort."""
        print(message)
        text = input().strip()
        if text.lower() in ('cancel', 'q'):
            print("Add cancelled — nothing was saved.")
            return None
        return text

    def add(self):
        single_exp_dict = {}
        while True:
            raw = self._prompt_or_cancel("Please provide the amount you've spent ('cancel' or 'q' to abort):")
            if raw is None:
                return
            try:
                Amount = float(raw)
                break
            except ValueError:
                print("That's not a valid number. Please try again.")
        Category = self._prompt_or_cancel("Please provide a relevant category you've spent it for ('cancel' or 'q' to abort):")
        if Category is None:
            return
        single_exp_dict['Amount'] = Amount
        single_exp_dict['Category'] = Category
        self.expense_list.append(single_exp_dict)
        self.save()

    def list_all(self):
        return self.expense_list

    def summary(self):
        summary = {}
        for expense in self.expense_list:
            category = expense.get("Category", "Uncategorized")
            amount = expense.get("Amount", 0)
            summary[category] = summary.get(category, 0) + amount

        return summary

    def total(self):
        total = 0
        for expense in self.expense_list:
            total += expense.get("Amount", 0)
        return round(total, 2)


def main():
    tracker = ExpenseTracker()

    try:
        while True:

            print("Choose one : Add/List/Summary/Total/Quit:")
            to_do = input().lower()

            if to_do == "add":
                tracker.add()
            elif to_do == "list":
                expenses = tracker.list_all()
                if not expenses:
                    print("No expenses yet.")
                else:
                    for i, exp in enumerate(expenses, 1):
                        print(f"{i}. {exp['Category']}: {exp['Amount']:.2f}")
            elif to_do == "total":
                print(tracker.total())
            elif to_do == "summary":
                summary = tracker.summary()
                if not summary:
                    print("No expenses yet.")
                else:
                    for category, amount in summary.items():
                        print(f"{category}:{amount:.2f}")
            elif to_do == "quit":
                break
            else:
                print("Sorry, only these options are supported.\nChoose from: Add/List/Summary/Total/Quit.\nBut don't worry, we're developing the application as we talk.")
    except (EOFError, KeyboardInterrupt):
        print()

    print("Thanks for using this app.")


if __name__ == "__main__":
    main()
