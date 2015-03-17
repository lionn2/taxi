function getMethod () {
	$.ajax({
	  url: '/users/1',
	  data: data,
	  success: function(data) {
	  	console.log(data);
	  }
	});
}