""" Problem description:

--- Day 19: Monster Messages ---
You land in an airport surrounded by dense forest. As you walk to your high-speed train, the Elves at the Mythical Information Bureau contact you again. They think their satellite has collected an image of a sea monster! Unfortunately, the connection to the satellite is having problems, and many of the messages sent back from the satellite have been corrupted.

They sent you a list of the rules valid messages should obey and a list of received messages they've collected so far (your puzzle input).

The rules for valid messages (the top part of your puzzle input) are numbered and build upon each other. For example:

0: 1 2
1: "a"
2: 1 3 | 3 1
3: "b"
Some rules, like 3: "b", simply match a single character (in this case, b).

The remaining rules list the sub-rules that must be followed; for example, the rule 0: 1 2 means that to match rule 0, the text being checked must match rule 1, and the text after the part that matched rule 1 must then match rule 2.

Some of the rules have multiple lists of sub-rules separated by a pipe (|). This means that at least one list of sub-rules must match. (The ones that match might be different each time the rule is encountered.) For example, the rule 2: 1 3 | 3 1 means that to match rule 2, the text being checked must match rule 1 followed by rule 3 or it must match rule 3 followed by rule 1.

Fortunately, there are no loops in the rules, so the list of possible matches will be finite. Since rule 1 matches a and rule 3 matches b, rule 2 matches either ab or ba. Therefore, rule 0 matches aab or aba.

Here's a more interesting example:

0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"
Here, because rule 4 matches a and rule 5 matches b, rule 2 matches two letters that are the same (aa or bb), and rule 3 matches two letters that are different (ab or ba).

Since rule 1 matches rules 2 and 3 once each in either order, it must match two pairs of letters, one pair with matching letters and one pair with different letters. This leaves eight possibilities: aaab, aaba, bbab, bbba, abaa, abbb, baaa, or babb.

Rule 0, therefore, matches a (rule 4), then any of the eight options from rule 1, then b (rule 5): aaaabb, aaabab, abbabb, abbbab, aabaab, aabbbb, abaaab, or ababbb.

The received messages (the bottom part of your puzzle input) need to be checked against the rules so you can determine which are valid and which are corrupted. Including the rules and the messages together, this might look like:

0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
Your goal is to determine the number of messages that completely match rule 0. In the above example, ababbb and abbbab match, but bababa, aaabbb, and aaaabbb do not, producing the answer 2. The whole message must match all of rule 0; there can't be extra unmatched characters in the message. (For example, aaaabbb might appear to match rule 0 above, but it has an extra unmatched b on the end.)

How many messages completely match rule 0?

Resume:

Puzzle: Message Matching with Rules

Objective:
Determine the number of messages that completely match rule 0.

Example:
Given the rules and messages:
- Rules: (example rules not provided in the excerpt)
- Messages: ababbb, abbbab, bababa, aaabbb, aaaabbb

Matching Results:
- Matches: ababbb, abbbab
- Non-matches: bababa, aaabbb, aaaabbb

Goal:
Count the number of messages that fully match rule 0 without any extra characters.

Solution Approach:
1. Read and separate the input into two parts: rules and messages.
2. Parse the rules and build a dictionary
3. Transform complex rules into simple message patterns
4. Iterate through all the messages and count how many of them match rule 0. This is the result.


--- Part Two ---
As you look over the list of messages, you realize your matching rules aren't quite right. To fix them, completely replace rules 8: 42 and 11: 42 31 with the following:

8: 42 | 42 8
11: 42 31 | 42 11 31
This small change has a big impact: now, the rules do contain loops, and the list of messages they could hypothetically match is infinite. You'll need to determine how these changes affect which messages are valid.

Fortunately, many of the rules are unaffected by this change; it might help to start by looking at which rules always match the same set of values and how those rules (especially rules 42 and 31) are used by the new versions of rules 8 and 11.

(Remember, you only need to handle the rules you have; building a solution that could handle any hypothetical combination of rules would be significantly more difficult.)

For example:

42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
Without updating rules 8 and 11, these rules only match three messages: bbabbbbaabaabba, ababaaaaaabaaab, and ababaaaaabbbaba.

However, after updating rules 8 and 11, a total of 12 messages match:

bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
After updating rules 8 and 11, how many messages completely match rule 0?

Resume:
Part Two: Updated Rules Matching

Objective:
Determine the number of messages that completely match rule 0 after updating rules 8 and 11.

Example:
Given the updated rules and messages:
- Updated Rules: (example rules not provided in the excerpt)
- Messages: (example messages provided in the excerpt)

Matching Results:
- Matches: bbabbbbaabaabba, babbbbaabbbbbabbbbbbaabaaabaaa, aaabbbbbbaaaabaababaabababbabaaabbababababaaa, bbbbbbbaaaabbbbaaabbabaaa, bbbababbbbaaaaaaaabbababaaababaabab, ababaaaaaabaaab, ababaaaaabbbaba, baabbaaaabbaaaababbaababb, abbbbabbbbaaaababbbbbbaaaababb, aaaaabbaabaaaaababaa, aaaabbaabbaaaaaaabbbabbbaaabbaabaaa, aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba

Goal:
Count the number of messages that fully match rule 0 after updating rules 8 and 11.

Solution Approach:
1. Parse the input to separate rules and messages.
2. Update rules 8 and 11 according to the new specifications.
3. Implement a function to check if a message matches rule 0 with the updated rules.
4. Count and return the number of matching messages.
"""

import re

def read_input(file_path):
    """
    Reads the input file and splits it into rules and messages sections.

    Args:
        file_path (str): The path to the input file.

    Returns:
        tuple: A tuple containing two lists:
            - rules_section (list): A list of strings representing the rules.
            - messages_section (list): A list of strings representing the messages.
    """
    with open(file_path, 'r') as file:
        sections = file.read().split('\n\n')
        rules_section = sections[0].split('\n')
        messages_section = sections[1].split('\n')
        return rules_section, messages_section

def parse_rule(rule):
    """
    Parses a single rule from the input format.

    Args:
        rule (str): A string representing a rule in the format "num: rule".

    Returns:
        tuple: A tuple where the first element is the rule number (int) and the second element is either:
               - a string if the rule is a terminal rule (e.g., "a" or "b")
               - a list of lists of integers if the rule is a non-terminal rule (e.g., [[1, 2], [3, 4]])

    Example:
        >>> parse_rule('1: "a"')
        (1, 'a')
        >>> parse_rule('2: 1 3 | 3 1')
        (2, [[1, 3], [3, 1]])
    """
    num, rule = rule.split(': ')
    if '"' in rule:
        return int(num), rule.strip('"')
    parts = rule.split(' | ')
    sub_rules = [list(map(int, part.split())) for part in parts]
    return int(num), sub_rules

regex_pattern = {}
def build_regex(rules, rule_num=0):
    """
    Recursively builds a regular expression pattern from a set of rules.

    Args:
        rules (dict): A dictionary where keys are rule numbers and values are either strings or lists of lists of integers.
                      Strings represent terminal symbols, while lists of lists represent sub-rules.
        rule_num (int, optional): The rule number to start building the regex from. Defaults to 0.

    Returns:
        str: A string representing the regular expression pattern for the given rule number.
    """
    rule = rules[rule_num]
    if isinstance(rule, str):
        return rule
    parts = []
    for sub_rule in rule:
        part = ''.join(build_regex(rules, num) for num in sub_rule)
        parts.append(part)
    return '(' + '|'.join(parts) + ')'

# read the input-19.txt file 
rules, messages = read_input('input-19.txt')
# print (rules)

# parse rules
parsed_rules = dict(parse_rule(rule) for rule in rules)
# print (parsed_rules)

# build regex pattern
regex_pattern = build_regex(parsed_rules)
regex_pattern = '^' + regex_pattern + '$'
# print (regex_pattern)

# count matching messages
matching_messages = sum(1 for message in messages if re.match(regex_pattern, message))
print(matching_messages)

def print_rule(rule_num):
    print(f"Rule {rule_num}: {parsed_rules[rule_num]}")

print_rule(0)
print_rule(8)
print_rule(11)
regex_42 = build_regex(parsed_rules, 42)
# print(42, regex_42[:50]+'...)')
regex_31 = build_regex(parsed_rules, 31)
# print(31, regex_31)

# Update rules 8 and 11 to handle loops
regex_8 = f"({regex_42})+"
regex_11 = "|".join(["((" + regex_42 + "){" + str(n) + "}(" + regex_31 + "){" + str(n) + "})" for n in range(1, 10)])

# Build the new regex pattern for rule 0
regex_pattern = f"^{regex_8}{regex_11}$"
print(regex_pattern)

# Count matching messages with the updated rules
matching_messages = sum(1 for message in messages if re.match(regex_pattern, message))
print(matching_messages)