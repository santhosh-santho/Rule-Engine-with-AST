import ast
import json

class RuleManager:
    def __init__(self, rule_file="rules.json"):
        self.rule_file = rule_file
        self.rules = self.load_rules()

    def load_rules(self):
        try:
            with open(self.rule_file, "r") as f:
                return json.load(f)["rules"]
        except FileNotFoundError:
            return []

    def save_rules(self):
        with open(self.rule_file, "w") as f:
            json.dump({"rules": self.rules}, f, indent=4)

    def create_rule(self, rule_string):
        ast = parse_rule(rule_string)
        self.rules.append({"ast": ast})
        self.save_rules()

    def combine_rules(self, rule_ids):
        combined_ast = combine_asts([self.rules[i]["ast"] for i in rule_ids])
        self.rules.append({"ast": combined_ast})
        self.save_rules()

    def evaluate_rule(self, rule_id, data):
        return evaluate_rule(self.rules[rule_id]["ast"], data)

    def modify_rule(self, rule_id, new_rule_string):
        self.rules[rule_id]["ast"] = parse_rule(new_rule_string)
        self.save_rules()