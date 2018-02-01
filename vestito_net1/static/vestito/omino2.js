
var fase = document.getElementById("fase").innerHTML;
	var cappello = document.getElementById("cappello").value;
	var maglia = document.getElementById("maglietta").value;
	var pantaloni = document.getElementById("pantaloni").value;
	var guanti = document.getElementById("guanti").value;
	var scarpe = document.getElementById("scarpe").value;

function update() {
    var omino = document.getElementById("fase").innerHTML;



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
}
//function goToRegole() {
//	window.location.replace("regole.html");
	//window.localStorage.setItem("doNotUpdate", "true");
//}

//function goToPrivacy() {
//	window.location.replace("privacy.html");
	//window.localStorage.setItem("doNotUpdate", "true");
//}