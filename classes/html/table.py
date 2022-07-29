class Table:
    def __init__(self, content: dict, isBootstrap: bool = False):
        self.header = content['header']
        self.rows = content['row']
        self.table_class = ''
        self.table_id = ''
        if isBootstrap:
            self._enable_bootstrap()
        self.filters = ''
        self._row_class = ''

    def enable_row_class(self, row_calsses_list: list):
        for row_class in row_calsses_list:
            self._row_class += row_class + " "

    def add_table_id(self, id: str):
        if id:
            self.table_id = ' id="' + id + '"'

    def enable_filters(self, function_name):
        filters = ""
        for i in range(0, len(self.header)):
            filters += f'''<th> <input class="form-control w-100 rounded-0 border-0" onkeyup="{function_name}({i})" type="text" placeholder="Search" id="searchBookIn_{i}" aria-label="Search"></th>'''
        self.filters = "<tr>" + filters + "</tr>"

    def _enable_bootstrap(self):
        self.table_class = ' class="table table-striped"'

    def get_table(self):
        return "<table" + self.table_class + self.table_id + ">" + self._get_header() + self._get_content() + "</table>"

    def _get_header(self):
        head = ""
        for cell in self.header:
            head += '<th scope="col">' + cell + '</th>'
        content = ''

        if self.filters:
            content = self.filters
        return '<thead class="thead-dark"><tr>' + head + '</tr>' + content + '</thead>'

    def _get_content(self):
        content = ""

        for row in self.rows:
            if self._row_class:
                content += "<tr class='" + self._row_class + "'>"
            else:
                content += "<tr>"

            for cell in row:
                content += "<td>" + str(cell) + "</td>"
            content += "</tr>"
        return content
