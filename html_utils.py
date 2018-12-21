html_head = ' '.join("""
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
            
            #myInput {
              background-position: 10px 12px; /* Position the search icon */
              background-repeat: no-repeat; /* Do not repeat the icon image */
              width: 100%; /* Full-width */
              font-size: 16px; /* Increase font-size */
              padding: 12px 20px 12px 40px; /* Add some padding */
              border: 1px solid #ddd; /* Add a grey border */
              margin-bottom: 12px; /* Add some space below the input */
            }

            #myTable {
              border-collapse: collapse; /* Collapse borders */
              width: 100%; /* Full-width */
              border: 1px solid #ddd; /* Add a grey border */
              font-size: 18px; /* Increase font-size */
            }

            #myTable th, #myTable td {
              text-align: left; /* Left-align text */
              padding: 12px; /* Add padding */
            }

            #myTable tr {
              /* Add a bottom border to all table rows */
              border-bottom: 1px solid #ddd; 
            }

            #myTable tr.header, #myTable tr:hover {
              /* Add a grey background color to the table header and on hover */
              background-color: #f1f1f1;
            }
        </style>
    </head>
""".split())

html_body_header = ' '.join("""
    <body>
        <input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search for groups..">
        
        <table class="table table-hover" id="xlstable">
          <thead>
            <tr>
              <th scope="col">group</th>
              <th scope="col">type</th>
              <th scope="col">name</th>
              <th scope="col">label</th>
              <th scope="col">choices</th>
            </tr>
          </thead>
    <tbody>
""".split())

html_body_tail = ' '.join("""
        </tbody>
    </table>
    <script>
            function myFunction() {
              var input, filter, table, tr, td, i, txtValue;
              input = document.getElementById("myInput");
              filter = input.value.toUpperCase();
              table = document.getElementById("xlstable");
              tr = table.getElementsByTagName("tr");
            
              for (i = 0; i < tr.length; i++) {
                td = tr[i].getElementsByTagName("td")[0];
                if (td) {
                  txtValue = td.textContent || td.innerText;
                  if (txtValue.toUpperCase().indexOf(filter) > -1) {
                    tr[i].style.display = "";
                  } else {
                    tr[i].style.display = "none";
                  }
                } 
              }
            }
    </script>
</body>""".split())