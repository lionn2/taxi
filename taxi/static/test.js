function getMethod () {
	$.ajax({
	  url: '/api/users/1',
	  data: data,
	  success: function(data) {
	  	console.log(data);
	  }
	});
}