function getToken () {
	var token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
	return 'csrfmiddlewaretoken=' + token;
}

function post_route_data(data) {
	$.ajax({
		url:"/route_data/",
		type:"POST",
		data: getToken() + "&distance=" + data.distance + "&duration=" + data.duration,
		cached: false,
		success: function(){
			alert("ok");
		}
	});
}

