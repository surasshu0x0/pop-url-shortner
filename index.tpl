% #template to generate html table of urls and homepage
<h1>Pop url shortner </h1>
<p>Url shortener database</p>
<table border="1">
<th>Original</th>
<th>Short link</th>
%for row in rows:
    <tr>
    <td>{{row[1]}}</td>
    <td><a href="http://localhost:8080/{{row[2]}}">localhost:8080/{{row[2]}}</a></td>
    </tr>
%end
</table>

<br />
<small>Built by @surasshu0x0 </small>
