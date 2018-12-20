"""
Reading an xls form into an HTML bootstrap table.
"""


class Question:
    def __init__(self, type, name, group, label=None, choices=None):
        self.type = type
        self.name = name
        self.group = group

        if label is not None:
            self.label = label
        else:
            self.label = None

        if choices is not None:
            self.choices = choices
        else:
            self.choices = None

    def to_html(self):
        """ transforms the question into a html row ... (<tr>)"""

        if self.choices:
            choices = ""
            for c in self.choices:
                choices = choices + """<li><a href="#">{}</a></li>""".format(c['name'])
        else:
            choices = ""

        return """
        <tr class="dropdown">
            <td>{group}</td>
            <td>{type}</td>
            <td>{name}</td>
            <td>{label}</td>
            <td>
                <div> 
                <button class="btn btn-primary dropdown-toggle" type="button" data-toggle="dropdown">Choices <span class="caret"></span>
                <ul class="dropdown-menu">
                {choices}
                </ul>
                </div>
            </td>
        </tr>
        """.format(
            group=self.group,
            type=self.type,
            name=self.name,
            label=self.label,
            choices=choices
        )


def add_question(vals):
    """ takes a dict of values and feeds them to the attrs of the object."""
    if 'choices' in vals:
        return Question(type=vals['type'], name=vals['name'], label=vals['label'], group=vals['group'], choices=vals['choices'])
    else:
        return Question(type=vals['type'], name=vals['name'], group=vals['group'], label=vals['label'])


def feed_workbook(wb):
    """given a json workbook from pyxform it decomposes each question."""
    l = []
    for i in wb:
        if 'group' in i:
            g = i['group']
        else:
            g = None
        if 'label' in i:
            if 'children' in i:
                for j in i['children']:
                    print(j)
                    if 'label' in j:
                        j['group'] = g
                        l.append(add_question(j))

            else:
                i['group'] = g
                l.append(add_question(i))
    return l


if __name__ == '__main__':
    XLS_FILE = 'data/mvam_car_test1.xls'
    # we can convert the xls to a better shaped json with pyxform
    from pyxform.xls2json_backends import xls_to_dict
    workbook_dict = xls_to_dict(XLS_FILE)
    from pyxform.xls2json import workbook_to_json
    workbook_json = workbook_to_json(workbook_dict, form_name=None, default_language=u"default", warnings=None)

    # cast the questions into a list of object, each with type, name, label, group and choices
    l = feed_workbook(workbook_json['children'])

    rows = ""
    for i in l:
        print(i.__dict__.keys())
        rows = rows + i.to_html()

    html = """
    <head>
        <script src="https://code.jquery.com/jquery-3.3.1.min.js" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" crossorigin="anonymous"></script>
        <!-- Latest compiled and minified CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
        <!-- Latest compiled and minified JavaScript -->
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
        <style>
            .open ul.dropdown-menu {
                display: block;
                position: relative;
            }
        </style>
    </head>
    <body>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">group</th>
              <th scope="col">type</th>
              <th scope="col">name</th>
              <th scope="col">label</th>
              <th scope="col">choices</th>
            </tr>
          </thead>
          <tbody>"""+' '.join(rows.split())+"</tbody></table></body>"




