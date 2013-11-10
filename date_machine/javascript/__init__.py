import json


def generate_js(patterns):
    def _generate(patterns):
        for pattern in patterns:
            order, tree, regex = pattern
            regex = regex.replace("\n", "").replace(" ", "")
            yield {'order': order, 'tree': tree, 'regex': regex}
    output = "parser_description = {};".format(json.dumps(list(_generate(patterns))))
    with open('javascript/parser_description.js', 'w') as f:
        f.write(output)
    return 'OK'