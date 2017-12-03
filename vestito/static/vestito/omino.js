document.addEventListener('DOMContentLoaded', checkActiveState(false), false);

function save() {
	if ($("#hint-alert").hasClass("show")) {
		$("#hint-alert").addClass("hidden");  //nasconte l'hint al primo tocco dei vestiti dell'omino
	}

	var fase = document.getElementById("fase").innerHTML;
	var cappello = document.getElementById("cappello").value;
	var maglia = document.getElementById("maglietta").value;
	var pantaloni = document.getElementById("pantaloni").value;
	var guanti = document.getElementById("guanti").value;
	var scarpe = document.getElementById("scarpe").value;

	var data = "fase=" + fase + "&" +
				"cappello=" + cappello + "&" +
				"maglia=" + maglia + "&" +
				"pantaloni=" + pantaloni + "&" +
				"guanti=" + guanti + "&" +
				"scarpe=" + scarpe;

	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (xhttp.readyState == 4 && xhttp.status == 200) {
			var value = xhttp.responseText;
			if (value == "1") {
				if ($("#warning-alert").hasClass("show")) {
					$("#warning-alert").removeClass("show");
					$("#warning-alert").addClass("hidden");
				}
				$("#success-alert").removeClass("hidden");
				$("#success-alert").addClass("show");
			} else {
				if ($("#success-alert").hasClass("show")) {
					$("#success-alert").removeClass("show");
					$("#success-alert").addClass("hidden");
				}
				$("#warning-alert").removeClass("hidden");
				$("#warning-alert").addClass("show");
			}
		}
	};
	//xhttp.open("POST", "http://www.mytito.it/zfor/saveTito.php", true);
	//xhttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded"); // setto gli Header
	//xhttp.send(getLog() + data);
}

function update() {
	var omino = document.getElementById("fase").innerHTML;
	var data = "omino=" + omino;
	//var name = document.getElementById("span").options[document.getElementById("omino").selectedIndex].innerHTML;
	//document.getElementById("name").innerHTML = name;

	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (xhttp.readyState == 4 && xhttp.status == 200) {
			var data = xhttp.responseText.split(",");
			var hat = data[0];
			var shirt = data[1];
			var pant = data[2];
			var shoe = data[3];
			var glove = data[4];
			document.getElementById("cappello").value = hat;
			document.getElementById("maglietta").value = shirt;
			document.getElementById("pantaloni").value = pant;
			document.getElementById("guanti").value = glove;
			document.getElementById("scarpe").value = shoe;
			
			document.getElementById("hat").setAttribute("fill", idToColor(hat));
			document.getElementById("mag").setAttribute("fill", idToColor(shirt));
			document.getElementById("pant").setAttribute("fill", idToColor(pant));
			document.getElementById("hat").setAttribute("fill", idToColor(hat));
			document.getElementById("shoe1").setAttribute("fill", idToColor(shoe));
			document.getElementById("shoe2").setAttribute("fill", idToColor(shoe));
			document.getElementById("glove1").setAttribute("fill", idToColor(glove));
			document.getElementById("glove2").setAttribute("fill", idToColor(glove));

			//window.plugins.spinnerDialog.hide();
			navigator.splashscreen.hide();
		}
	};
	//xhttp.open("POST", "http://www.mytito.it/zfor/updateOmino.php", true);
	//xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded"); // setto gli Header
	//xhttp.send(getLog() + data);
}

//function checkActiveState(onlyCheck) {
	//window.plugins.spinnerDialog.show();
//	var xhttp = new XMLHttpRequest();
//	xhttp.onreadystatechange = function() {
//		if (this.readyState == 4 && this.status == 200) {
//	        var data = xhttp.responseText.split(",");
//			var active = data[0];
//			var phase = data[1];
//			var oldPhase = window.localStorage.getItem("phase");
//			if (active == '1') {
//				if (oldPhase != phase && oldPhase != null) {
//					alert("La fase " + oldPhase + " del gioco è terminata. Completa il breve questionario e fai il login di nuovo per iniziare la fase successiva.");
//					window.location.replace("fineFase.html");
//					//logout();
//				} else {
//					if (onlyCheck) {
//						save();
//						return;
//					}
//					initializeData();
//				}
//			} else {
//				if (oldPhase < 3) {
//					alert("La fase " + oldPhase + " del gioco è terminata. Completa il breve questionario. Presto inizierà la prossima fase.");
//				} else if (oldPhase == 3) {
//					alert("Anche la fase " + oldPhase + " del gioco è terminata. Completa l'ultimo questionario. Grazie per aver partecipato. Presto conoscerai i risultati del gioco.");
//				}
//				window.location.replace("fineFase.html");
				//logout();
//			}
//		}
//	};
//	xhttp.open("POST", "http://www.mytito.it/zfor/checkActiveState.php", true);
//	xhttp.send();
//}


function initializeData() {
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (xhttp.readyState == 4 && xhttp.status == 200) {
			var data = xhttp.responseText.split(",");
			var name = data[0];
			var phase = data[1];
			document.getElementById("name").innerHTML = name;
			document.getElementById("fase").innerHTML = phase;
			window.localStorage.setItem("phase", phase);
			//getSurveyState();
			getHint(phase);
			update();
		}
	};
//	xhttp.open("POST", "http://www.mytito.it/zfor/getOmini.php", true);
//	xhttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded");// setto gli Header
//	xhttp.send(getLog());
}

//function getHint(phase) {
//	var xhttp = new XMLHttpRequest();
//	var data = "&phase=" + phase;
//	xhttp.onreadystatechange = function() {
//		if (xhttp.readyState == 4 && xhttp.status == 200) {
//			var result = xhttp.responseText;
//			var data = result.split(",");
//			var idnetwork = data[0];
//			var pos_a = data[1];
//			var pos_b = data[2];
//			var pos_c = data[3];
//			var pos_d = data[4];
//			var pos_e = data[5];
//			var hint = data[6];

//			if (hint != '1') {
//				$("#hint-text").html(hint);
//				$("#hint-alert-1").removeClass("hidden");
//				$("#hint-alert-1").addClass("show");
//			}
			
//			if (idnetwork == 1) {
//				$("#networkImage").attr("src", "img/Network1.png");
//			} else if (idnetwork == 2) {
//				$("#networkImage").attr("src", "img/Network2.png");
//			} else if (idnetwork == 3) {
//				$("#networkImage").attr("src", "img/Network3.png");
//			}
//			$("#listItem1").html("[A] " + pos_a);
//			$("#listItem2").html("[B] " + pos_b);
//			$("#listItem3").html("[C] " + pos_c);
//			$("#listItem4").html("[D] " + pos_d);
//			$("#listItem5").html("[E] " + pos_e);

//			$("#hint-alert-2").removeClass("hidden");
//			$("#hint-alert-2").addClass("show");
//		}
//	};
//	xhttp.open("POST", "http://www.mytito.it/zfor/getHint.php", true);
//	xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded"); // setto gli Header
//	xhttp.send(getLog() + data);
//}

/*function getSurveyState() {
	var url = "http://www.mytito.it/zfor/game/getSurveyState.php";
	var credentials = {username: "", password: "", id: ""};
	credentials.username = window.localStorage.getItem("username");
	credentials.password = window.localStorage.getItem("password");
	credentials.id = window.localStorage.getItem("id");
	var postData = { credentials: credentials, surveyID: 1 };

	$.post(url, postData).done(function(data) {
		data = JSON.parse(data);
		if (data['surveyState']) {
			$('#regole').hide();
		}
	});
}*/

	
var lastelements;

function magclick() {
	lastelements = [document.getElementById('mag'), 0, document.getElementById("maglietta")];
	$('#colors').modal('toggle');
}

function pantclick() {
	lastelements = [document.getElementById('pant'), 0, document.getElementById("pantaloni")];
	$('#colors').modal('toggle');
}

function shoeclick() {
	lastelements = [document.getElementById('shoe1'), document.getElementById("shoe2"), document.getElementById("scarpe")];
	$('#colors').modal('toggle');
}

function gloveclick() {
	lastelements = [document.getElementById('glove1'), document.getElementById('glove2'), document.getElementById("guanti")];
	$('#colors').modal('toggle');
}

function hatclick() {
	lastelements = [document.getElementById('hat'), 0, document.getElementById("cappello")];
	$('#colors').modal('toggle');
}	

function changeColor(color) {
	$('#colors').modal('toggle');
	lastelements[0].setAttribute("fill", idToColor(color));
	if (lastelements[1] != 0)
		lastelements[1].setAttribute("fill", idToColor(color));
	lastelements[2].value = color;
	checkActiveState(true); //check if active before saving
}

function idToColor(color) {
	if (color == "1")
		return "#f44336";
	if (color == "2")
		return "#ff9800";
	if (color == "3")
		return "#ffeb3b";
	if (color == "4")
		return "#8bc34a";
	if (color == "5")
		return "#3f51b5";
	if (color == "6")
		return "#29b6f6";
	if (color == "7")
		return "#ce93d8";
	if (color == "8")
		return "#ffffff";
	if (color == "9")
		return "#000000";
	if (color == "10")
		return "#9e9e9e";
}

//function getLog() {
//	return window.localStorage.getItem("log");
//}

//function goToRegole() {
//	window.location.replace("regole.html");
	//window.localStorage.setItem("doNotUpdate", "true");
//}

//function goToPrivacy() {
//	window.location.replace("privacy.html");
	//window.localStorage.setItem("doNotUpdate", "true");
//}