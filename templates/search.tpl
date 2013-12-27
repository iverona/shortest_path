<!DOCTYPE html>
<html>
<head>
	<title>Search for shortest path</title>
	<center><h1>Search for shortest path</h1></center>
</head>

<body>
	<h3>Select Origin and Destination City</h3>

	%cities_dict = {}
	%cities_options = ""
	%for row in cities:
		%name = row[0]		
		%cities_options += """<option value="%s">%s</option>\n\t\t""" % (name,name)		
	%end


	<form action="/test" method="post">
            Origin: 
            <select name="orig">
    		{{!cities_options}}
			</select>
			
            Destination: 
            <select name="dest">
    		{{!cities_options}}
			</select>
			<br/>
            <input value="Find path!" type="submit" />
    </form>

    <p>
    <canvas id="myCanvas" width="600" height="600" style="border:1px solid #c3c3c3;">
	Your browser does not support the HTML5 canvas tag.
	</canvas>
	</p>

	<script>

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
		
		ctx.moveTo({{pointA[0]}}, {{pointA[1]}})
		ctx.lineTo({{pointB[0]}}, {{pointB[1]}})
		ctx.stroke()
		%end

		//var background = new Image();
		//background.src = "http://2.bp.blogspot.com/_RzlA4jeAROQ/TOD3MGfHyYI/AAAAAAAAACs/fIMYTQdxAdU/s640/mapaprovincias.jpg";

		// Make sure the image is loaded first otherwise nothing will draw.
		//background.onload = function(){
		//    ctx.drawImage(background,0,0);   
		//}

	</script>


</body>
</html>