from logic.filereader import FileReader
from logic.rulecontroller import RuleController

rules = FileReader.read_grammar_file("grammaticalRules.txt")
rule_controller = RuleController()
rule_controller.build_rules(rules)
poem = rule_controller.rules_dictionary.get("POEM")
for lines in poem.rule_references:
    keyword = ""
    lines = rule_controller.rules_dictionary.get(lines[1:-1])
    original_line = lines
    while lines != "$END":
      lines = rule_controller.apply_rule(lines.rule_id)
    keyword = original_line.rule_keyword
    if keyword == "$LINEBREAK":
        rule_controller.poem = rule_controller.poem + "\n"
print(rule_controller.poem)
