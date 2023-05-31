/* Aktuelles Datum */
function getDate() {
    let date = new Date();
    let dday = date.getDate();
    let dmonth = date.getMonth() + 1;
    let dyear = date.getFullYear();
    date = dday + "." + dmonth + "." + dyear;
	var d = date.toString();
	document.getElementById('heutigesDatum').innerHTML = d;
}


/* Abbrechen Popup */

function popupOnA()
{
    document.getElementById("overlayAbbrechen").style.display = "block";
}

function popupOffA()
{
    document.getElementById("overlayAbbrechen").style.display = "none";
}

function popupOnL()
{
    document.getElementById("overlayLoeschen").style.display = "block";
}
function popupOffL()
{
    document.getElementById("overlayLoeschen").style.display = "none";
}

function popupOnS()
{
    document.getElementById("overlaySpeichern").style.display = "block";
}

function popupOffS()
{
    document.getElementById("overlaySpeichern").style.display = "none";
}