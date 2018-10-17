import random


class RuleController:
    def __init__(self):
        self.rules_dictionary = {}
        self.poem = ""

    def build_rules(self, rules):
        for value in rules:
            if value[0] == "POEM":
                rule = Rule(value[0], references=value[1])
                self.rules_dictionary[rule.rule_id] = rule
            elif value[0] == "LINE":
                rule = Rule(value[0], references=value[1], keyword=value[2])
                self.rules_dictionary[rule.rule_id] = rule
            else:
                rule = Rule(value[0], value[1], value[2])
                self.rules_dictionary[rule.rule_id] = rule

    def apply_rule(self, rule_id):
        rule = self.rules_dictionary.get(rule_id)
        print(rule.to_string())
        if rule.rule_id == "LINE":
            print("ENTRE A LINE")
            for reference in rule.rule_references:
                if "<" and ">" in reference:
                    rule2 = self.rules_dictionary.get(reference[1:-1])
                    return rule2
        else:
            self.poem = self.poem + " " + rule.get_definition()
            reference = rule.get_reference()
            if reference != "$END":
                if "<" and ">" in reference:
                    rule3 = self.rules_dictionary.get(reference[1:-1])
                    return rule3
            else:
                return reference


class Rule:
    def __init__(self, rule_id, definitions="", references="", keyword=""):
        self.rule_id = rule_id
        self.rule_definition = definitions.split('|')
        if rule_id == "POEM":
            self.rule_references = references.split(' ')
        else:
            self.rule_references = references.split('|')
        self.rule_keyword = keyword

    def get_definition(self):
        if self.rule_definition != "":
            return self.rule_definition[random.randint(0, len(self.rule_definition)-1)]

    def get_reference(self):
        if self.rule_references != "":
            return self.rule_references[random.randint(0, len(self.rule_references)-1)]

    def to_string(self):
        return "rule_id: " + self.rule_id + "\ndefinitions: " + str(self.rule_definition) \
               + "\nreferences: " + str(self.rule_references) + "\nkeyword: " + str(self.rule_keyword)

