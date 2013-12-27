<!DOCTYPE html>
<html>
<head>
	<title>Search for shortest path</title>
	<center><h1>Shortest Path Result</h1></center>
</head>

<body>
	<h3><p>Origing: {{orig}}</p></h3>
	<h3><p>Destination: {{dest}}</p></h3>
	<h3><p>Distance: {{dist}}</p></h3>
	<h3><p>Path: 
		%for node in path[:-1]:
			{{node}} ->
		%end

		{{path[-1]}}
	</p></h3>

    <p>
    <canvas id="myCanvas" width="600" height="600" style="border:1px solid #c3c3c3;">
	Your browser does not support the HTML5 canvas tag.
	</canvas>
	</p>

	<script>
		%cities_dict = {}
		var c=document.getElementById("myCanvas");
		var ctx=c.getContext("2d");
		ctx.translate(300,300)
		ctx.font="15px Arial";
		

		%for row in cities:
		ctx.fillRect({{float(row[1]/3)}}, {{float(-row[2]/3)}}, 10, 10)
		ctx.fillText("{{row[0]}}", {{float(row[1]/3)}}, {{float(-row[2]/3-4)}})
		%cities_dict[row[0]] = [float(row[1]/3),float(-row[2]/3)]		
		%end

		%for row in roads:
		%pointA = [cities_dict[row[0]][0], cities_dict[row[0]][1]]
		%pointB = [cities_dict[row[1]][0], cities_dict[row[1]][1]]

		%print path
		%print row
		
		ctx.beginPath()
		%if row[0] in path and row[1] in path:
		ctx.strokeStyle="#FF0000"
		ctx.lineWidth="5";
		%else:
		ctx.strokeStyle="#000000"
		ctx.lineWidth="2";
		%end
		ctx.moveTo({{pointA[0]}}, {{pointA[1]}})
		ctx.lineTo({{pointB[0]}}, {{pointB[1]}})
		ctx.stroke()
		%end



	</script>
</body>
</html>