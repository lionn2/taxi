function getMethod () {
	/*$.ajax({
	  url: '/api/users',
	  data: getToken(),
	  method: 'GET',
	  success: function(data) {
	  	console.log(data);
	  },
	  
	});*/
	var user = {
		email: 'hello@gmail.com',
		password: "12",
		username: "alex"
	}
	$.ajax({
	  url: '/api/users',
	  data: getToken() + '&email=' + user.email + '&password=' + user.password + '&username=' + user.username,
	  method: 'POST',
	  success: function(data) {
	  	console.log(data);
	  },
	  error: function (error) {
	  	console.log(error);
	  }
	  
	});
}

function getToken() {
	var token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
	return 'csrfmiddlewaretoken=' + token;
}