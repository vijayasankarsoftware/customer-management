setTimeout(() => {
    const message = document.getElementById("message");
    message.style.display = 'none';
}, 2000)

function printTable()
{

    var newWindow = window.open('', 'Print Customer Details');
    newWindow.document.open('', "Customer Details");
    var rows = document.getElementsByTagName('tr');

    newWindow.document.write('<table border=1><tr><th>ID</th><th>NAME</th><th>GENDER</th><th>EMAIL</th></tr>')
    for(var i = 1; i < rows.length; i++)
    {
        row = rows[i];
        newWindow.document.write('<tr border=1>');
        newWindow.document.write("<td>"+row.getElementsByTagName('td')[0].innerHTML+"</td>")
        newWindow.document.write("<td>"+row.getElementsByTagName('td')[1].innerHTML+"</td>")
        newWindow.document.write("<td>"+row.getElementsByTagName('td')[2].innerHTML+"</td>")
        newWindow.document.write("<td>"+row.getElementsByTagName('td')[3].innerHTML+"</td>")
        newWindow.document.write("</tr>");
    }
    newWindow.document.write("</table>");
    newWindow.print();

}
