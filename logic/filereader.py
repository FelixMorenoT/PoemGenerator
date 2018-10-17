class FileReader:
    @classmethod
    def read_grammar_file(cls, file_path):
        lines = [line.rstrip("\n") for line in open(file_path)]
        for line in lines:
            print(cls.parse_grammar(line))

    @classmethod
    def parse_grammar(cls, line):
        if line:
            rule_split = line.split(":")
            if len(rule_split) == 2:
                if rule_split[0] != "POEM":
                    definitions_references = rule_split[1].strip().split(" ")
                    rule = [rule_split[0], definitions_references[0], definitions_references[1]]
                    return rule
                else:
                    rule = [rule_split[0], rule_split[1].strip()]
                    return rule

