var http = require("http")
var handler = function(request, response){
	
	//llamar con /?numero=X, deonde  x es la cantidad	
	var query = require('url').parse(request.url,true).query;
	var n = query.numero;
	if(n == "")
		n = 15;

	for (var i = 1; i <= n; i++) {
		for (var j = 0; j < n-i; j++){
			response.write("\t");
		}
		for (var j = 0; j < i; j++){
			response.write("\t#");
		}
		response.write("\n");
	}
	response.end("========== FIN PROGRAMA ==========");
}

var server = http.createServer(handler);
server.listen(8000);
