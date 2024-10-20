from rule_manager import RuleManager

def main():
    rule_manager = RuleManager()

    # Example usage
    rule_manager.create_rule("age > 30 AND department = 'Sales'")
    rule_manager.create_rule("age < 25 AND department = 'Marketing'")

    combined_rule_id = rule_manager.combine_rules([0, 1])

    data = {"age": 35, "department": "Sales"}
    result = rule_manager.evaluate_rule(combined_rule_id, data)
    print(result)

if __name__ == "__main__":
    main()